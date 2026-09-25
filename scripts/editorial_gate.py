#!/usr/bin/env python3
"""
Deterministic editorial gate for Lisa morning candidates.

The gate is intentionally stricter than the minimum historical contract:
- every candidate must carry the core V6.5 metadata
- Vrstva 1 candidates must be true CREATE slots with 3 labelled headline variants
- CREATE candidates must pass duplicate + intent overlap checks
- Vrstva 2 cannot hide hard duplicates or unverified claims

The script writes a Markdown audit next to the input and exits non-zero on FAIL.
"""
import argparse
import datetime
import json
from pathlib import Path


ACTIONS = {
    "CREATE",
    "UPDATE",
    "REWRITE",
    "MERGE",
    "FOLLOW-UP",
    "MONITOR",
    "DROP",
    "WAIT_FOR_PEG",
    "GOOD_SIGNAL_WEAK_TODAY",
    "INSPIRATION_ONLY",
}
SITES = {"letemsvetemapplem.eu", "androidmagazine.eu", "samsungmagazine.eu"}
ROMAN_TEST_KEYS = ("is_today", "our_angle", "roman_would_click", "verified")
WRITE_ACTIONS = {"CREATE", "UPDATE", "REWRITE", "MERGE", "FOLLOW-UP"}
LAYER1_VALUES = {"VRSTVA 1", "LAYER 1", "LAYER_1", "PRIORITY", "PRIORITIES"}
LAYER2_VALUES = {"VRSTVA 2", "LAYER 2", "LAYER_2", "INSPIRATION", "INSPIRACE"}
TITLE_TARGETS = {"DISCOVER", "SEARCH", "BALANCED"}
PASS_VALUES = {"PASS", "OK", "CLEAR", "NO_OVERLAP", "NONE"}
FAIL_VALUES = {"FAIL", "OVERLAP", "SAME_INTENT", "DUPLICATE", "MATCH"}


def fail(reason: str) -> tuple[bool, str]:
    return False, reason


def first_present(candidate: dict, *keys: str):
    for key in keys:
        if key in candidate and candidate.get(key) not in (None, ""):
            return candidate.get(key)
    return None


def normalize_token(value) -> str:
    if value is None:
        return ""
    return str(value).strip().upper().replace("-", "_")


def classify_layer(candidate: dict) -> str | None:
    value = first_present(candidate, "layer", "brief_layer", "output_layer")
    token = normalize_token(value).replace("_", " ")
    if token in LAYER1_VALUES:
        return "LAYER_1"
    if token in LAYER2_VALUES:
        return "LAYER_2"
    return None


def is_pass_like(value) -> bool:
    return normalize_token(value) in PASS_VALUES


def is_fail_like(value) -> bool:
    return normalize_token(value) in FAIL_VALUES


def validate_title_variants(candidate: dict) -> list[str]:
    reasons: list[str] = []
    variants = first_present(candidate, "title_variants", "headline_variants", "headlines")
    if not isinstance(variants, list) or len(variants) < 3:
        return ["Vrstva 1 requires at least 3 title variants"]

    labelled = 0
    recommended = 0
    for idx, variant in enumerate(variants[:3], start=1):
        if isinstance(variant, str):
            reasons.append(f"title variant {idx} must include target label Discover/Search/Balanced")
            continue
        if not isinstance(variant, dict):
            reasons.append(f"title variant {idx} has invalid shape")
            continue
        title = first_present(variant, "title", "headline", "text")
        target = normalize_token(first_present(variant, "target", "use", "type", "label", "channel"))
        if not title:
            reasons.append(f"title variant {idx} missing title")
        if target not in TITLE_TARGETS:
            reasons.append(f"title variant {idx} missing valid target")
        else:
            labelled += 1
        if variant.get("recommended") is True:
            recommended += 1

    recommended_index = first_present(candidate, "recommended_title_index", "recommended_headline_index")
    if recommended_index not in (None, ""):
        try:
            if int(recommended_index) in {1, 2, 3}:
                recommended = max(recommended, 1)
        except (TypeError, ValueError):
            reasons.append("recommended title index must be numeric")

    if labelled < 3:
        reasons.append("Vrstva 1 requires 3 labelled title variants")
    if recommended != 1:
        reasons.append("Vrstva 1 requires exactly one recommended title variant")
    if not first_present(candidate, "recommended_title_reason", "headline_choice_reason", "recommended_title_why"):
        reasons.append("Vrstva 1 requires a short reason for the recommended title")
    return reasons


def validate_candidate(candidate: dict) -> list[str]:
    reasons: list[str] = []

    if not candidate.get("candidate_id"):
        reasons.append("missing candidate_id")
    if candidate.get("site") not in SITES:
        reasons.append("invalid or missing site")
    if not candidate.get("exact_topic"):
        reasons.append("missing exact_topic")

    action = candidate.get("action")
    if action not in ACTIONS:
        reasons.append("invalid or missing action")

    if not first_present(candidate, "proposed_title", "recommended_title"):
        reasons.append("missing proposed_title")
    if not first_present(candidate, "primary_lane", "lane"):
        reasons.append("missing primary_lane")
    if not first_present(candidate, "why_now"):
        reasons.append("missing why_now")
    if not first_present(candidate, "unique_value"):
        reasons.append("missing unique_value")
    if not first_present(candidate, "reality_status"):
        reasons.append("missing reality_status")
    if not first_present(candidate, "information_age_status"):
        reasons.append("missing information_age_status")
    if not first_present(candidate, "wp_check_status"):
        reasons.append("missing wp_check_status")
    if first_present(candidate, "opportunity_score") is None:
        reasons.append("missing opportunity_score")
    if first_present(candidate, "predictive_score") is None:
        reasons.append("missing predictive_score")
    if first_present(candidate, "confidence") is None:
        reasons.append("missing confidence")
    if "fail_reasons" not in candidate:
        reasons.append("missing fail_reasons")

    roman = candidate.get("roman_test")
    if not isinstance(roman, dict):
        reasons.append("missing roman_test")
    else:
        missing = [key for key in ROMAN_TEST_KEYS if key not in roman]
        if missing:
            reasons.append("roman_test missing: " + ", ".join(missing))
        yes_count = sum(1 for key in ROMAN_TEST_KEYS if roman.get(key) is True)
        if action in WRITE_ACTIONS and yes_count < 3:
            reasons.append(f"Roman Test {yes_count}/4 is too low for {action}")
        if action in WRITE_ACTIONS and roman.get("verified") is not True:
            reasons.append("verified=false blocks write action")

    evidence = candidate.get("evidence")
    hard_evidence = first_present(candidate, "hard_evidence")
    if action in WRITE_ACTIONS and (not isinstance(evidence, list) or not evidence):
        reasons.append("write action requires evidence[]")
    if action in WRITE_ACTIONS and not hard_evidence:
        reasons.append("write action requires hard_evidence")

    duplicate_status = candidate.get("duplicate_status")
    if duplicate_status not in {"PASS", "DUPLICATE", "UNCERTAIN"}:
        reasons.append("invalid or missing duplicate_status")
    if action == "CREATE" and duplicate_status != "PASS":
        reasons.append(f"CREATE requires duplicate_status=PASS, got {duplicate_status}")

    intent_overlap_status = first_present(candidate, "intent_overlap_status", "intent_overlap_check", "intent_status")
    if action == "CREATE" and intent_overlap_status is None:
        reasons.append("CREATE requires intent_overlap_status")
    if action == "CREATE" and is_fail_like(intent_overlap_status):
        reasons.append(f"CREATE blocked by intent overlap: {intent_overlap_status}")
    if action == "CREATE" and not is_pass_like(intent_overlap_status):
        reasons.append(f"CREATE requires pass-like intent overlap status, got {intent_overlap_status}")

    rejected_status = first_present(
        candidate,
        "rejected_topics_status",
        "rejected_topic_check",
        "rejected_topics_checked",
    )
    rejected_match = first_present(candidate, "rejected_topics_match", "rejected_topic_match")
    if action == "CREATE" and rejected_status is None and rejected_match is None:
        reasons.append("CREATE requires rejected topics check")
    if is_fail_like(rejected_status):
        reasons.append(f"rejected topics check failed: {rejected_status}")
    if rejected_match not in (None, False, "false", "FALSE", "", []):
        reasons.append("candidate overlaps a previously rejected topic")

    final_write_gate = candidate.get("final_write_gate")
    if action in WRITE_ACTIONS and final_write_gate != "PASS":
        reasons.append(f"{action} requires final_write_gate=PASS")

    layer = classify_layer(candidate)
    if action == "CREATE" and layer != "LAYER_1":
        reasons.append("CREATE candidate must be assigned to Vrstva 1")
    if layer == "LAYER_1":
        if action != "CREATE":
            reasons.append("Vrstva 1 can contain only CREATE candidates")
        reasons.extend(validate_title_variants(candidate))
    elif layer == "LAYER_2":
        layer_reason = first_present(candidate, "layer_reason", "secondary_reason", "inspiration_reason")
        if not layer_reason:
            reasons.append("Vrstva 2 requires layer_reason")
        if duplicate_status == "DUPLICATE":
            reasons.append("Vrstva 2 cannot contain hard duplicates")
        if isinstance(roman, dict) and roman.get("verified") is not True:
            reasons.append("Vrstva 2 cannot contain unverified claims")
    else:
        reasons.append("missing or invalid layer assignment")

    return reasons


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", help="Path to morning candidates JSON")
    parser.add_argument("--audit-out", help="Optional Markdown audit output path")
    args = parser.parse_args()

    input_path = Path(args.input_json).expanduser()
    if not input_path.exists():
        print(f"EDITORIAL_GATE_FAIL missing input: {input_path}")
        return 2

    try:
        data = json.loads(input_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"EDITORIAL_GATE_FAIL invalid JSON: {exc}")
        return 2

    candidates = data.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        print("EDITORIAL_GATE_FAIL candidates[] missing or empty")
        return 2

    rows = []
    failed = 0
    layer1_count = 0
    layer2_count = 0
    for candidate in candidates:
        reasons = validate_candidate(candidate)
        if reasons:
            failed += 1
        layer = classify_layer(candidate)
        if layer == "LAYER_1":
            layer1_count += 1
        elif layer == "LAYER_2":
            layer2_count += 1
        rows.append((candidate, reasons))

    if args.audit_out:
        audit_path = Path(args.audit_out).expanduser()
    elif input_path.exists() and input_path.parent.exists() and str(input_path).startswith("/dev/fd/") is False:
        audit_path = input_path.with_suffix(".gate.md")
    else:
        audit_path = Path.home() / ".openclaw" / "workspace" / "cache" / f"editorial_gate_audit_{datetime.datetime.now():%Y%m%d_%H%M%S}.md"
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Editorial Gate Audit — {datetime.date.today():%Y-%m-%d}",
        "",
        f"Input: `{input_path}`",
        f"Result: {'FAIL' if failed else 'PASS'}",
        f"Layer 1 count: `{layer1_count}`",
        f"Layer 2 count: `{layer2_count}`",
        "",
    ]
    for candidate, reasons in rows:
        status = "FAIL" if reasons else "PASS"
        title_variants = first_present(candidate, "title_variants", "headline_variants", "headlines")
        lines.extend(
            [
                f"## {status} — {candidate.get('candidate_id', '(missing id)')}",
                f"- site: {candidate.get('site', '(missing)')}",
                f"- action: {candidate.get('action', '(missing)')}",
                f"- layer: {first_present(candidate, 'layer', 'brief_layer', 'output_layer') or '(missing)'}",
                f"- topic: {candidate.get('exact_topic', '(missing)')}",
                f"- title variants: {len(title_variants) if isinstance(title_variants, list) else 0}",
                f"- reasons: {', '.join(reasons) if reasons else 'none'}",
                "",
            ]
        )
    audit_path.write_text("\n".join(lines), encoding="utf-8")

    if failed:
        print(f"EDITORIAL_GATE_FAIL {failed}/{len(candidates)} candidates failed audit: {audit_path}")
        return 1

    print(f"EDITORIAL_GATE_PASS {len(candidates)} candidates passed audit: {audit_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

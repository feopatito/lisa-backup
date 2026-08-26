#!/usr/bin/env python3
"""
Deterministic editorial gate for Lisa morning candidates.

Input JSON contract:
{
  "run_date": "YYYY-MM-DD",
  "candidates": [
    {
      "candidate_id": "...",
      "site": "letemsvetemapplem.eu|androidmagazine.eu|samsungmagazine.eu",
      "exact_topic": "...",
      "action": "CREATE|UPDATE|REWRITE|MERGE|FOLLOW-UP|MONITOR|DROP",
      "roman_test": {
        "is_today": true,
        "our_angle": true,
        "roman_would_click": true,
        "verified": true
      },
      "evidence": ["source 1", "source 2"],
      "duplicate_status": "PASS|DUPLICATE|UNCERTAIN",
      "final_write_gate": "PASS|FAIL"
    }
  ]
}

The script writes a Markdown audit next to the input and exits non-zero on FAIL.
"""
import argparse
import datetime
import json
from pathlib import Path


ACTIONS = {"CREATE", "UPDATE", "REWRITE", "MERGE", "FOLLOW-UP", "MONITOR", "DROP"}
SITES = {"letemsvetemapplem.eu", "androidmagazine.eu", "samsungmagazine.eu"}
ROMAN_TEST_KEYS = ("is_today", "our_angle", "roman_would_click", "verified")
WRITE_ACTIONS = {"CREATE", "UPDATE", "REWRITE", "MERGE", "FOLLOW-UP"}


def fail(reason: str) -> tuple[bool, str]:
    return False, reason


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
    if action in WRITE_ACTIONS and (not isinstance(evidence, list) or not evidence):
        reasons.append("write action requires evidence[]")

    duplicate_status = candidate.get("duplicate_status")
    if duplicate_status not in {"PASS", "DUPLICATE", "UNCERTAIN"}:
        reasons.append("invalid or missing duplicate_status")
    if action == "CREATE" and duplicate_status != "PASS":
        reasons.append(f"CREATE requires duplicate_status=PASS, got {duplicate_status}")

    final_write_gate = candidate.get("final_write_gate")
    if action in WRITE_ACTIONS and final_write_gate != "PASS":
        reasons.append(f"{action} requires final_write_gate=PASS")

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
    for candidate in candidates:
        reasons = validate_candidate(candidate)
        if reasons:
            failed += 1
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
        "",
    ]
    for candidate, reasons in rows:
        status = "FAIL" if reasons else "PASS"
        lines.extend(
            [
                f"## {status} — {candidate.get('candidate_id', '(missing id)')}",
                f"- site: {candidate.get('site', '(missing)')}",
                f"- action: {candidate.get('action', '(missing)')}",
                f"- topic: {candidate.get('exact_topic', '(missing)')}",
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

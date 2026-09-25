#!/usr/bin/env python3
"""
Local image SEO audit runner for AndroidMagazine.

Batch size defaults to 500, checkpointing every 50 images.
Outputs:
- CSV
- JSONL log
- HTML report
- manifest.json
"""

from __future__ import annotations

import base64
import csv
import html
import json
import math
import os
import time
from datetime import datetime
import re
import unicodedata
from pathlib import Path
from typing import Any

import requests


ROOT = Path("/Users/lisa/.openclaw/workspace")
AUDIT_DIR = ROOT / "image-audit"
RUNS_DIR = AUDIT_DIR / "runs"
PROMPT_PATH = AUDIT_DIR / "prompt_gpt4o_mini_500.md"
LATEST_HTML = AUDIT_DIR / "gpt4o_mini_image_audit.html"
LATEST_MANIFEST = AUDIT_DIR / "gpt4o_mini_manifest.json"

WP_URL = "https://androidmagazine.eu/wp-json/wp/v2"
WP_USER = "Lisa"
MODEL = "gpt-4o-mini"
DEFAULT_BATCH_SIZE = 500
DEFAULT_CHECKPOINT_EVERY = 50

MODEL_BASE_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bnote\s*4\b|\bnote4\b"), "Samsung Galaxy Note 4"),
    (re.compile(r"\bnote\s*3\b|\bnote3\b"), "Samsung Galaxy Note 3"),
    (re.compile(r"\bnote\s*2\b|\bnote2\b"), "Samsung Galaxy Note 2"),
    (re.compile(r"\bnote\s*8\.0\b|\bnote8\.0\b|\bnote\s*8\b"), "Samsung Galaxy Note 8.0"),
    (re.compile(r"\bs\s*5\b|\bs5\b"), "Samsung Galaxy S5"),
    (re.compile(r"\bs\s*4\b|\bs4\b"), "Samsung Galaxy S4"),
    (re.compile(r"\bs\s*3\b|\bs3\b"), "Samsung Galaxy S3"),
    (re.compile(r"\bs\s*2\b|\bs2\b"), "Samsung Galaxy S2"),
    (re.compile(r"\bs\s*1\b|\bs1\b"), "Samsung Galaxy S"),
    (re.compile(r"\btab\s*4\b|\btab4\b"), "Samsung Galaxy Tab 4"),
    (re.compile(r"\btab\s*3\b|\btab3\b"), "Samsung Galaxy Tab 3"),
    (re.compile(r"\bgear\s*2\b|\bgear2\b"), "Samsung Gear 2"),
    (re.compile(r"\bgear\b"), "Samsung Galaxy Gear"),
    (re.compile(r"\bgrand\s*neo\b"), "Samsung Galaxy Grand Neo"),
    (re.compile(r"\bgrand\s*lite\b"), "Samsung Galaxy Grand Lite"),
    (re.compile(r"\bgrand\b"), "Samsung Galaxy Grand"),
    (re.compile(r"\bmega\b"), "Samsung Galaxy Mega"),
    (re.compile(r"\bfame\b"), "Samsung Galaxy Fame"),
    (re.compile(r"\bcore\b"), "Samsung Galaxy Core"),
    (re.compile(r"\btrend\b"), "Samsung Galaxy Trend"),
]

VARIANT_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\belectric\s+blue\b"), "Electric Blue"),
    (re.compile(r"\bcharcoal\s+black\b"), "Charcoal Black"),
    (re.compile(r"\bcopper\s+gold\b"), "Copper Gold"),
    (re.compile(r"\bspace\s+gray\b"), "Space Gray"),
    (re.compile(r"\bspace\s+grey\b"), "Space Gray"),
    (re.compile(r"\bgold\b"), "Gold"),
    (re.compile(r"\bred\b"), "Red"),
    (re.compile(r"\bblue\b"), "Blue"),
    (re.compile(r"\bblack\b"), "Black"),
    (re.compile(r"\bwhite\b"), "White"),
    (re.compile(r"\bsilver\b"), "Silver"),
    (re.compile(r"\bgreen\b"), "Green"),
    (re.compile(r"\bpink\b"), "Pink"),
    (re.compile(r"\bpurple\b"), "Purple"),
    (re.compile(r"\byellow\b"), "Yellow"),
    (re.compile(r"\borange\b"), "Orange"),
]

GENERIC_TITLE_RE = re.compile(
    r"^(?:"
    r"smartphone|mobil(?:n[ií])? telefon|telefon|tablet|za[ií]zen[ií]|"
    r"displej|fotoapar[aá]t|hodinky|kryt|obal|logo|screenshot|obrazovka"
    r")(?:\b|$)",
    re.IGNORECASE,
)


def load_openai_key() -> str | None:
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key
    try:
        with open(Path.home() / ".openclaw" / "openclaw.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        return config.get("env", {}).get("vars", {}).get("OPENAI_API_KEY")
    except Exception:
        return None


def load_wp_password() -> str | None:
    key = os.getenv("WP_ANDROID_PASS")
    if key:
        return key
    try:
        with open(Path.home() / ".openclaw" / "openclaw.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        return config.get("env", {}).get("WP_ANDROID_PASS")
    except Exception:
        return None


def load_prompt() -> str:
    if PROMPT_PATH.exists():
        return PROMPT_PATH.read_text(encoding="utf-8")
    return (
        "Analyze this image for SEO metadata. Return only JSON with keys "
        "alt_text, title, confidence, action, reason. Write in Czech."
    )


def ensure_dirs() -> None:
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)


def esc(value: Any) -> str:
    return html.escape("" if value is None else str(value))


def normalized(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text or "")
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    stripped = re.sub(r"[_\-]+", " ", stripped)
    stripped = re.sub(r"[^a-zA-Z0-9]+", " ", stripped)
    return re.sub(r"\s+", " ", stripped.lower()).strip()


def infer_model_base(*texts: str) -> str:
    combined = " ".join(texts)
    normalized_combined = normalized(combined)
    for pattern, label in MODEL_BASE_PATTERNS:
        if pattern.search(normalized_combined):
            return label
    return ""


def infer_variant(*texts: str) -> str:
    combined = " ".join(texts)
    normalized_combined = normalized(combined)
    for pattern, label in VARIANT_PATTERNS:
        if pattern.search(normalized_combined):
            return label
    return ""


def title_has_meaningful_model(title: str) -> bool:
    return bool(infer_model_base(title))


def refine_title(raw_title: str, orig_title: str, filename: str, orig_alt: str) -> str:
    title = (raw_title or "").strip()
    base = infer_model_base(orig_title, filename, orig_alt, title)
    variant = infer_variant(orig_title, filename, orig_alt, title)

    if base:
        if variant:
            if normalized(variant) not in normalized(title) and normalized(variant) not in normalized(base):
                return f"{base} {variant}"
        if not title or GENERIC_TITLE_RE.search(title) or not title_has_meaningful_model(title):
            return base

    if variant and title and normalized(variant) not in normalized(title) and not title_has_meaningful_model(title):
        return f"{title} {variant}"

    return title


def load_attachments(limit: int, wp_pass: str) -> list[dict[str, Any]]:
    session = requests.Session()
    session.auth = (WP_USER, wp_pass)
    attachments: list[dict[str, Any]] = []
    page = 1

    while len(attachments) < limit and page <= 20:
        url = f"{WP_URL}/media?per_page=100&page={page}&order=asc&orderby=date"
        resp = session.get(url, timeout=20)
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break

        for item in batch:
            if len(attachments) >= limit:
                break
            mime = item.get("mime_type", "")
            if mime not in {"image/jpeg", "image/png", "image/webp", "image/gif"}:
                continue
            attachments.append(
                {
                    "id": item.get("id"),
                    "filename": item.get("media_details", {}).get("file", ""),
                    "alt_text": (item.get("alt_text", "") or "").strip(),
                    "title": item.get("title", {}).get("rendered", ""),
                    "source_url": item.get("source_url", ""),
                    "mime_type": mime,
                }
            )
        page += 1

    return attachments[:limit]


def build_payload(prompt: str, mime: str, image_bytes: bytes) -> dict[str, Any]:
    img_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    return {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{mime};base64,{img_b64}"},
                    },
                    {"type": "text", "text": prompt},
                ],
            }
        ],
        "max_tokens": 400,
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
    }


def analyze_image(openai_key: str, prompt: str, source_url: str) -> tuple[dict[str, Any], int]:
    session = requests.Session()
    image_resp = session.get(source_url, timeout=30)
    image_resp.raise_for_status()
    mime = image_resp.headers.get("content-type", "image/jpeg")

    payload = build_payload(prompt, mime, image_resp.content)
    api_resp = session.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {openai_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )
    api_resp.raise_for_status()
    content = api_resp.json()["choices"][0]["message"]["content"]
    data = json.loads(content)
    return data, 200


def normalize_result(raw: dict[str, Any], existing_alt: str) -> dict[str, Any]:
    action = (raw.get("action") or "").strip().upper()
    if action not in {"UPDATE", "KEEP", "MANUAL_REVIEW"}:
        action = "UPDATE" if existing_alt and len(existing_alt.strip()) >= 20 else "MANUAL_REVIEW"

    confidence = raw.get("confidence", 0)
    try:
        confidence = int(confidence)
    except Exception:
        confidence = 0
    confidence = max(0, min(5, confidence))

    return {
        "alt_text": (raw.get("alt_text") or "").strip(),
        "title": (raw.get("title") or "").strip(),
        "confidence": confidence,
        "action": action,
        "reason": (raw.get("reason") or "").strip(),
    }


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    headers = [
        "index",
        "media_id",
        "filename",
        "source_url",
        "orig_alt",
        "orig_title",
        "new_alt",
        "new_title",
        "confidence",
        "action",
        "reason",
        "status",
        "elapsed_sec",
        "updated_at",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in headers})


def row_class(action: str) -> str:
    action = (action or "").upper()
    if action == "UPDATE":
        return "update"
    if action == "KEEP":
        return "keep"
    return "review"


def build_html(rows: list[dict[str, Any]], manifest: dict[str, Any]) -> str:
    total = len(rows)
    update_count = sum(1 for row in rows if row.get("action") == "UPDATE")
    keep_count = sum(1 for row in rows if row.get("action") == "KEEP")
    review_count = sum(1 for row in rows if row.get("action") == "MANUAL_REVIEW")

    rows_html = []
    for row in rows:
        rows_html.append(
            f"""
            <tr class="{row_class(row.get('action', ''))}">
              <td>{esc(row.get('index', ''))}</td>
              <td>{esc(row.get('media_id', ''))}</td>
              <td class="thumb"><img src="{esc(row.get('source_url', ''))}" alt="" loading="lazy"></td>
              <td class="mono">{esc(row.get('filename', ''))}</td>
              <td>{esc(row.get('orig_alt', ''))}</td>
              <td>{esc(row.get('orig_title', ''))}</td>
              <td>{esc(row.get('new_alt', ''))}</td>
              <td>{esc(row.get('new_title', ''))}</td>
              <td>{esc(row.get('confidence', ''))}</td>
              <td>{esc(row.get('action', ''))}</td>
              <td class="reason">{esc(row.get('reason', ''))}</td>
            </tr>
            """
        )

    return f"""<!doctype html>
<html lang="cs">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AndroidMagazine image audit - GPT-4o-mini</title>
  <style>
    :root {{
      --bg: #0b0f14;
      --panel: #131922;
      --line: rgba(255,255,255,.08);
      --text: #e5edf5;
      --muted: #97a6b7;
      --accent: #7dd3fc;
      --update: rgba(59,130,246,.10);
      --keep: rgba(34,197,94,.10);
      --review: rgba(245,158,11,.10);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: radial-gradient(circle at top, #12263b 0, var(--bg) 55%);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
    }}
    .wrap {{ max-width: 1600px; margin: 0 auto; padding: 24px; }}
    .hero {{
      background: linear-gradient(180deg, rgba(125,211,252,.12), rgba(19,25,34,.94));
      border: 1px solid var(--line);
      border-radius: 20px;
      padding: 22px;
      margin-bottom: 18px;
    }}
    h1 {{ margin: 0 0 8px; font-size: clamp(26px, 3vw, 40px); }}
    .sub {{ color: var(--muted); max-width: 1000px; }}
    .stats {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 14px; }}
    .pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 12px;
      border-radius: 999px;
      border: 1px solid var(--line);
      background: rgba(255,255,255,.04);
      font-size: 13px;
    }}
    .section {{
      background: rgba(19,25,34,.94);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 18px;
      margin-top: 18px;
    }}
    h2 {{ margin: 0 0 12px; font-size: 20px; }}
    .meta {{ color: var(--muted); font-size: 13px; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      overflow: hidden;
      border-radius: 14px;
      border: 1px solid var(--line);
      background: rgba(255,255,255,.02);
    }}
    th, td {{
      border-bottom: 1px solid var(--line);
      padding: 10px;
      text-align: left;
      vertical-align: top;
      font-size: 13px;
    }}
    th {{
      position: sticky;
      top: 0;
      background: #111827;
      z-index: 1;
      text-transform: uppercase;
      letter-spacing: .04em;
      font-size: 12px;
    }}
    tr.update {{ background: var(--update); }}
    tr.keep {{ background: var(--keep); }}
    tr.review {{ background: var(--review); }}
    td.thumb img {{
      width: 110px;
      height: 78px;
      object-fit: cover;
      border-radius: 10px;
      display: block;
      background: #0f1722;
    }}
    td.mono {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 12px;
      word-break: break-word;
      min-width: 190px;
    }}
    td.reason {{ min-width: 220px; color: #dce4ee; }}
    .scroll {{ overflow: auto; max-height: 78vh; border-radius: 14px; }}
    .footer {{ color: var(--muted); font-size: 12px; padding-top: 12px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="hero">
      <h1>AndroidMagazine image audit - GPT-4o-mini</h1>
      <div class="sub">Lokavni batch pro nejstarsi media. Tento report se prepisuje po kazdem checkpointu a slouzi jako jeden sdileny HTML soubor pro kontrolu.</div>
      <div class="stats">
        <span class="pill"><strong>Run</strong> {esc(manifest.get("run_id", ""))}</span>
        <span class="pill"><strong>Status</strong> {esc(manifest.get("status", ""))}</span>
        <span class="pill"><strong>Total</strong> {total}</span>
        <span class="pill"><strong>Update</strong> {update_count}</span>
        <span class="pill"><strong>Keep</strong> {keep_count}</span>
        <span class="pill"><strong>Review</strong> {review_count}</span>
        <span class="pill"><strong>Model</strong> {esc(manifest.get("model", ""))}</span>
      </div>
      <div class="meta">Checkpoint every {esc(manifest.get("checkpoint_every", ""))} items | Batch target {esc(manifest.get("batch_size", ""))} | Started {esc(manifest.get("started_at", ""))}</div>
    </div>

    <div class="section">
      <h2>Manifest</h2>
      <pre style="white-space:pre-wrap; margin:0; color:#dce4ee;">{esc(json.dumps(manifest, ensure_ascii=False, indent=2))}</pre>
    </div>

    <div class="section">
      <h2>Rows</h2>
      <div class="scroll">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>ID</th>
              <th>Preview</th>
              <th>Filename</th>
              <th>Orig ALT</th>
              <th>Orig Title</th>
              <th>New ALT</th>
              <th>New Title</th>
              <th>Conf</th>
              <th>Action</th>
              <th>Reason</th>
            </tr>
          </thead>
          <tbody>
            {''.join(rows_html)}
          </tbody>
        </table>
      </div>
    </div>

    <div class="footer">Generated from {esc(str(LATEST_MANIFEST))} and refreshed from the running batch.</div>
  </div>
</body>
</html>
"""


def save_checkpoint(
    rows: list[dict[str, Any]],
    manifest: dict[str, Any],
    csv_path: Path,
    html_path: Path,
    manifest_path: Path,
) -> None:
    write_csv(csv_path, rows)
    html_path.write_text(build_html(rows, manifest), encoding="utf-8")
    write_json(manifest_path, manifest)
    write_json(LATEST_MANIFEST, manifest)


def main() -> None:
    ensure_dirs()
    openai_key = load_openai_key()
    wp_pass = load_wp_password()
    if not openai_key:
        raise SystemExit("OPENAI_API_KEY not found")
    if not wp_pass:
        raise SystemExit("WP_ANDROID_PASS not found")

    batch_size = int(os.getenv("IMAGE_AUDIT_BATCH_SIZE", str(DEFAULT_BATCH_SIZE)))
    checkpoint_every = int(os.getenv("IMAGE_AUDIT_CHECKPOINT_EVERY", str(DEFAULT_CHECKPOINT_EVERY)))
    prompt = load_prompt()

    run_id = f"{MODEL}-{datetime.now().strftime('%Y%m%d_%H%M%S')}-n{batch_size}"
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    csv_path = run_dir / f"{run_id}.csv"
    jsonl_path = run_dir / f"{run_id}.jsonl"
    html_path = LATEST_HTML
    manifest_path = run_dir / "manifest.json"

    attachments = load_attachments(batch_size, wp_pass)

    started_at = datetime.now().isoformat(timespec="seconds")
    manifest: dict[str, Any] = {
        "run_id": run_id,
        "status": "running",
        "model": MODEL,
        "batch_size": batch_size,
        "checkpoint_every": checkpoint_every,
        "target_count": len(attachments),
        "processed": 0,
        "updated": 0,
        "kept": 0,
        "manual_review": 0,
        "started_at": started_at,
        "last_checkpoint_at": started_at,
        "prompt_path": str(PROMPT_PATH),
        "csv_path": str(csv_path),
        "jsonl_path": str(jsonl_path),
        "html_path": str(html_path),
        "manifest_path": str(manifest_path),
        "latest_checkpoint_index": 0,
        "last_media_id": None,
        "last_error": None,
    }

    rows: list[dict[str, Any]] = []
    save_checkpoint(rows, manifest, csv_path, html_path, manifest_path)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Run: {run_id}")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Loaded {len(attachments)} images")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Output HTML: {html_path}")

    checkpoint_markers = {x for x in range(checkpoint_every, batch_size + 1, checkpoint_every)}

    try:
        for idx, att in enumerate(attachments, start=1):
            started = time.time()
            status = 0
            try:
                raw, status = analyze_image(openai_key, prompt, att["source_url"])
                result = normalize_result(raw, att.get("alt_text", ""))
            except Exception as exc:
                result = {
                    "alt_text": "",
                    "title": "",
                    "confidence": 0,
                    "action": "MANUAL_REVIEW",
                    "reason": f"ERROR: {exc}",
                }
                status = 500

            elapsed = round(time.time() - started, 2)

            row = {
                "index": idx,
                "media_id": att.get("id"),
                "filename": att.get("filename", ""),
                "source_url": att.get("source_url", ""),
                "orig_alt": att.get("alt_text", ""),
                "orig_title": att.get("title", ""),
                "new_alt": result["alt_text"],
                "new_title": refine_title(
                    result["title"],
                    att.get("title", ""),
                    att.get("filename", ""),
                    att.get("alt_text", ""),
                ),
                "confidence": result["confidence"],
                "action": result["action"],
                "reason": result["reason"],
                "status": status,
                "elapsed_sec": elapsed,
                "updated_at": datetime.now().isoformat(timespec="seconds"),
            }
            rows.append(row)

            manifest["processed"] = len(rows)
            manifest["updated"] = sum(1 for r in rows if r["action"] == "UPDATE")
            manifest["kept"] = sum(1 for r in rows if r["action"] == "KEEP")
            manifest["manual_review"] = sum(1 for r in rows if r["action"] == "MANUAL_REVIEW")
            manifest["last_checkpoint_at"] = datetime.now().isoformat(timespec="seconds")
            manifest["latest_checkpoint_index"] = idx
            manifest["last_media_id"] = att.get("id")
            manifest["last_error"] = None if status == 200 else f"status={status}"

            with jsonl_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")

            if idx in checkpoint_markers or idx == len(attachments):
                save_checkpoint(rows, manifest, csv_path, html_path, manifest_path)
                print(
                    f"[{datetime.now().strftime('%H:%M:%S')}] checkpoint {idx}/{len(attachments)} "
                    f"(update={manifest['updated']}, keep={manifest['kept']}, review={manifest['manual_review']})"
                )

        manifest["status"] = "completed"
        manifest["completed_at"] = datetime.now().isoformat(timespec="seconds")
        save_checkpoint(rows, manifest, csv_path, html_path, manifest_path)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] completed {len(rows)} items")
        print(f"HTML: {html_path}")
        print(f"CSV: {csv_path}")

    except Exception as exc:
        manifest["status"] = "failed"
        manifest["last_error"] = str(exc)
        manifest["failed_at"] = datetime.now().isoformat(timespec="seconds")
        save_checkpoint(rows, manifest, csv_path, html_path, manifest_path)
        raise


if __name__ == "__main__":
    main()

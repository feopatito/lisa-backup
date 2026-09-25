#!/usr/bin/env python3
"""
Local LLaVA audit for the last 50 items from the GPT-4o SEO audit.
Creates a 50-item local report and compares it with the previous GPT-4o output.
"""

import base64
import csv
import json
import os
from datetime import datetime

import requests


WP_URL = "https://androidmagazine.eu/wp-json/wp/v2"
WP_USER = "Lisa"
WP_PASS = os.getenv("WP_ANDROID_PASS")
OLLAMA_URL = "http://localhost:11434/api/generate"

AUDIT_DIR = os.path.expanduser("~/.openclaw/workspace/image-audit")
SOURCE_CSV = os.path.join(AUDIT_DIR, "audit200_seo_20260818_220349.csv")

RUN_DIR = os.path.join(AUDIT_DIR, "runs", f"llava-local-50-{datetime.now().strftime('%Y%m%d_%H%M%S')}")
os.makedirs(RUN_DIR, exist_ok=True)

LOCAL_CSV = os.path.join(RUN_DIR, "llava-local-50.csv")
LOCAL_JSONL = os.path.join(RUN_DIR, "llava-local-50.jsonl")
COMPARE_MD = os.path.join(RUN_DIR, "llava-vs-gpt4o-compare.md")
HTML_FILE = os.path.join(RUN_DIR, "llava-local-50.html")


def load_source_rows():
    rows = []
    with open(SOURCE_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)
    return all_rows[-50:]


def analyze_llava(image_url):
    img_resp = requests.get(image_url, timeout=20)
    img_resp.raise_for_status()
    img_b64 = base64.standard_b64encode(img_resp.content).decode("utf-8")

    prompt = """Analyze this image for SEO metadata and return ONLY valid JSON.

Return:
{
  "brand": "brand if visible or empty string",
  "model": "model if visible or empty string",
  "technical_detail": "key visible detail or empty string",
  "alt_text": "Czech descriptive alt text, 80-140 chars, specific and factual",
  "title_seo": "Czech SEO title, ideally 2-7 words, concise",
  "confidence": 1-5
}

Rules:
- Describe only what you can see.
- Use brand/model/color/position if visible and useful.
- If uncertain, keep it generic and lower confidence.
- Do not invent details.
- Return JSON only.
"""

    payload = {
        "model": "llava:latest",
        "prompt": prompt,
        "images": [img_b64],
        "stream": False,
        "format": "json",
    }

    resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
    resp.raise_for_status()
    text = resp.json().get("response", "{}")
    return json.loads(text)


def make_filename(title):
    base = (title or "").strip().lower()
    if not base:
        return ""
    import re
    base = re.sub(r"[^\w\s-]", "", base, flags=re.UNICODE)
    base = re.sub(r"[\s_]+", "-", base)
    base = re.sub(r"-+", "-", base).strip("-")
    return base[:60]


def render_html(rows, summary):
    parts = [
        "<!DOCTYPE html>",
        "<html><head><meta charset='utf-8'>",
        "<title>LLaVA Local 50 Audit</title>",
        "<style>",
        "body{font-family:sans-serif;font-size:12px;margin:20px;color:#222}",
        "h1{font-size:18px;margin-bottom:4px}",
        ".summary{margin:10px 0 16px;padding:10px 14px;background:#f0f0f0;border-radius:4px;font-size:13px}",
        "table{border-collapse:collapse;width:100%}",
        "th{background:#222;color:#fff;padding:7px 8px;text-align:left;font-size:11px;white-space:nowrap}",
        "td{padding:5px 8px;border-bottom:1px solid #ddd;vertical-align:top;font-size:11px}",
        "tr:nth-child(even){background:#f7f7f7}",
        ".UPDATE{color:#c00;font-weight:bold}",
        ".MANUAL_REVIEW{color:#b36b00;font-weight:bold}",
        ".KEEP{color:#060;font-weight:bold}",
        ".match{color:#060}",
        ".diff{color:#c00}",
        "</style></head><body>",
        "<h1>AndroidMagazine.eu &mdash; Local LLaVA 50 Audit</h1>",
        "<div class='summary'>",
        f"Datum: {summary['generated_at']} &nbsp;&bull;&nbsp; ",
        f"Celkem: <b>{summary['total']}</b> &nbsp;&bull;&nbsp; ",
        f"<span class='UPDATE'>UPDATE: {summary['update']}</span> &nbsp;&bull;&nbsp; ",
        f"<span class='KEEP'>KEEP: {summary['keep']}</span> &nbsp;&bull;&nbsp; ",
        f"<span class='MANUAL_REVIEW'>MANUAL: {summary['manual']}</span><br>",
        f"Shoda s GPT-4o: <b>{summary['exact_match_pct']}%</b> &nbsp;&bull;&nbsp; ",
        f"Model: {summary['model']} &nbsp;&bull;&nbsp; <i>Local dry-run</i>",
        "</div><table>",
        "<tr><th>#</th><th>WP ID</th><th>Orig filename</th><th>Orig ALT</th><th>Orig title</th><th>Navrhovaný ALT</th><th>Navrhovaný title</th><th>Conf</th><th>Akce</th></tr>",
    ]
    for row in rows:
        parts.append(
            "<tr>"
            f"<td>{row['index']}</td>"
            f"<td>{row['wp_id']}</td>"
            f"<td>{row['orig_filename']}</td>"
            f"<td>{row['orig_alt']}</td>"
            f"<td>{row['orig_title']}</td>"
            f"<td>{row['new_alt']}</td>"
            f"<td>{row['new_title']}</td>"
            f"<td>{row['confidence']}</td>"
            f"<td class='{row['action']}'>{row['action']}</td>"
            "</tr>"
        )
    parts.append("</table></body></html>")
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write("".join(parts))


def compare_with_gpt4o(local_rows, gpt_rows):
    by_id = {r["wp_id"]: r for r in gpt_rows}
    total = len(local_rows)
    exact = 0
    action_match = 0
    title_match = 0
    alt_match = 0
    out_lines = []
    out_lines.append("# Local LLaVA vs GPT-4o comparison")
    out_lines.append("")
    out_lines.append(f"Source: {SOURCE_CSV}")
    out_lines.append(f"Rows: {total}")
    out_lines.append("")
    out_lines.append("| WP ID | GPT-4o title | Local title | GPT-4o action | Local action | Match |")
    out_lines.append("| --- | --- | --- | --- | --- | --- |")
    for row in local_rows:
        g = by_id.get(row["wp_id"], {})
        title_ok = row["new_title"].strip() == (g.get("new_title", "") or "").strip()
        alt_ok = row["new_alt"].strip() == (g.get("new_alt", "") or "").strip()
        act_ok = row["action"] == g.get("action", "")
        if title_ok:
            title_match += 1
        if alt_ok:
            alt_match += 1
        if act_ok:
            action_match += 1
        if title_ok and alt_ok and act_ok:
            exact += 1
        match = "yes" if title_ok and alt_ok and act_ok else "no"
        out_lines.append(
            f"| {row['wp_id']} | {g.get('new_title', '')} | {row['new_title']} | {g.get('action', '')} | {row['action']} | {match} |"
        )

    out_lines.append("")
    out_lines.append("## Summary")
    out_lines.append(f"- Exact match: {exact}/{total} ({round(exact/total*100, 1)}%)")
    out_lines.append(f"- Title match: {title_match}/{total} ({round(title_match/total*100, 1)}%)")
    out_lines.append(f"- ALT match: {alt_match}/{total} ({round(alt_match/total*100, 1)}%)")
    out_lines.append(f"- Action match: {action_match}/{total} ({round(action_match/total*100, 1)}%)")

    with open(COMPARE_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))

    return {
        "exact": exact,
        "title_match": title_match,
        "alt_match": alt_match,
        "action_match": action_match,
        "total": total,
        "exact_pct": round(exact / total * 100, 1),
    }


def main():
    source_rows = load_source_rows()
    gpt4o_rows = source_rows
    local_rows = []

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Loaded {len(source_rows)} source rows (last 50).")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Running local LLaVA audit...")

    start = datetime.now()
    for idx, row in enumerate(source_rows, 1):
        analysis = analyze_llava(row["source_url"])
        confidence = int(analysis.get("confidence", 0) or 0)
        action = "UPDATE" if confidence >= 3 else "MANUAL_REVIEW"
        new_alt = analysis.get("alt_text", "").strip()
        new_title = analysis.get("title_seo", "").strip()
        local_row = {
            "index": idx,
            "wp_id": row["wp_id"],
            "source_url": row["source_url"],
            "orig_filename": row["orig_filename"],
            "orig_alt": row["orig_alt"],
            "orig_title": row["orig_title"],
            "new_alt": new_alt,
            "new_title": new_title,
            "confidence": confidence,
            "action": action,
            "reason": f"local llava conf {confidence}/5",
            "brand": analysis.get("brand", ""),
            "model": analysis.get("model", ""),
            "technical_detail": analysis.get("technical_detail", ""),
        }
        local_rows.append(local_row)
        with open(LOCAL_JSONL, "a", encoding="utf-8") as f:
            f.write(json.dumps(local_row, ensure_ascii=False) + "\n")
        if idx % 5 == 0 or idx == 1:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {idx:02d}/50 WP {row['wp_id']} conf {confidence}/5 {action}")

    with open(LOCAL_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "index",
                "wp_id",
                "source_url",
                "orig_filename",
                "orig_alt",
                "orig_title",
                "new_alt",
                "new_title",
                "confidence",
                "action",
                "reason",
                "brand",
                "model",
                "technical_detail",
            ],
        )
        writer.writeheader()
        for row in local_rows:
            writer.writerow(row)

    compare = compare_with_gpt4o(local_rows, gpt4o_rows)
    summary = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "total": len(local_rows),
        "update": len([r for r in local_rows if r["action"] == "UPDATE"]),
        "keep": len([r for r in local_rows if r["action"] == "KEEP"]),
        "manual": len([r for r in local_rows if r["action"] == "MANUAL_REVIEW"]),
        "model": "llava:latest",
        "exact_match_pct": compare["exact_pct"],
    }
    render_html(local_rows, summary)

    elapsed = (datetime.now() - start).total_seconds()
    print(f"\nDone in {elapsed/60:.1f} min")
    print(f"Local CSV: {LOCAL_CSV}")
    print(f"Local HTML: {HTML_FILE}")
    print(f"Comparison: {COMPARE_MD}")


if __name__ == "__main__":
    main()

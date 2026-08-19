#!/usr/bin/env python3
"""Generate a GitHub-friendly HTML report for the 100-image pilot audit."""

from __future__ import annotations

import csv
import html
from collections import Counter
from pathlib import Path


ROOT = Path("/Users/lisa/.openclaw/workspace")
CSV_PATH = ROOT / "reports" / "media-pilot-100-real-vision.csv"
HTML_PATH = ROOT / "reports" / "media-pilot-100-real-vision.html"


def load_rows():
    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def detect_issue(row: dict[str, str]) -> list[str]:
    issues: list[str] = []
    alt = (row.get("alt_tag_cs") or "").strip().lower()
    new = (row.get("new_filename") or "").strip().lower()
    old = (row.get("old_filename") or "").strip().lower()

    if len(alt) < 35:
        issues.append("short-alt")
    if any(term in alt for term in ("smartphone", "telefon", "obrázek", "snímek obrazovky")) and not any(
        brand in alt for brand in ("google", "samsung", "xiaomi", "motorola", "oneplus", "vivo", "oppo", "pixel", "redmi", "garmin", "watch")
    ):
        issues.append("generic-device")
    if "iphone" in alt and "pixel" in old:
        issues.append("possible-brand-mismatch")
    if "pixel-9" in new and "pixel-11" in old:
        issues.append("possible-model-mismatch")
    return issues


def esc(value: str) -> str:
    return html.escape(value or "")


def build_html(rows: list[dict[str, str]]) -> str:
    total = len(rows)
    issues = [row for row in rows if detect_issue(row)]
    issue_count = len(issues)

    brands = Counter()
    for row in rows:
        alt = (row.get("alt_tag_cs") or "").lower()
        for brand in ("google", "samsung", "xiaomi", "motorola", "oneplus", "vivo", "oppo", "garmin", "huawei", "redmi", "pixel"):
            if brand in alt or brand in (row.get("new_filename") or "").lower():
                brands[brand] += 1
                break

    rows_html = []
    for idx, row in enumerate(rows, 1):
        issue_list = detect_issue(row)
        badge_class = "warn" if issue_list else "ok"
        issue_text = ", ".join(issue_list) if issue_list else "ok"
        rows_html.append(
            f"""
            <tr class="{badge_class}">
              <td>{idx}</td>
              <td>{esc(row.get('id', ''))}</td>
              <td class="fn">{esc(row.get('old_filename', ''))}</td>
              <td class="fn">{esc(row.get('new_filename', ''))}</td>
              <td class="alt">{esc(row.get('alt_tag_cs', ''))}</td>
              <td class="desc">{esc(row.get('obsah_popis', ''))}</td>
              <td class="issue">{esc(issue_text)}</td>
            </tr>
            """
        )

    top_notes = []
    top_notes.append(f"<li><strong>{issue_count}</strong> záznamů má varování podle rychlého QA filtru</li>")
    if issue_count:
        sample = ", ".join(esc(row.get("old_filename", "")) for row in issues[:8])
        top_notes.append(f"<li>Nejčastěji jde o příliš obecné formulace nebo možné brand/model chyby</li>")
        top_notes.append(f"<li>Vzorky problematických položek: {sample}</li>")

    brand_items = "".join(
        f"<span class='pill'>{esc(name)}: {count}</span>" for name, count in brands.most_common()
    )

    return f"""<!doctype html>
<html lang="cs">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Image SEO pilot 100 - AndroidMagazine</title>
  <style>
    :root {{
      --bg: #0d1117;
      --panel: #161b22;
      --panel-2: #0f1722;
      --text: #e6edf3;
      --muted: #9da7b3;
      --line: rgba(255,255,255,.08);
      --accent: #7dd3fc;
      --good: #16a34a;
      --warn: #f59e0b;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
      background: radial-gradient(circle at top, #132238 0, var(--bg) 52%);
      color: var(--text);
      line-height: 1.45;
    }}
    .wrap {{ max-width: 1480px; margin: 0 auto; padding: 28px 18px 48px; }}
    .hero {{
      background: linear-gradient(180deg, rgba(125,211,252,.12), rgba(22,27,34,.95));
      border: 1px solid var(--line);
      border-radius: 22px;
      padding: 24px;
      box-shadow: 0 20px 60px rgba(0,0,0,.25);
    }}
    h1 {{ margin: 0 0 8px; font-size: clamp(26px, 3vw, 40px); }}
    .sub {{ color: var(--muted); max-width: 920px; margin-bottom: 16px; }}
    .stats {{ display: flex; flex-wrap: wrap; gap: 10px; margin: 16px 0 12px; }}
    .pill, .stat {{
      display: inline-flex; align-items: center; gap: 6px;
      padding: 7px 12px; border-radius: 999px;
      border: 1px solid var(--line); background: rgba(255,255,255,.04);
      font-size: 13px; color: var(--text);
    }}
    .stat strong {{ color: #fff; }}
    .good {{ color: #bbf7d0; border-color: rgba(22,163,74,.35); }}
    .warn {{ color: #fde68a; border-color: rgba(245,158,11,.35); }}
    .section {{
      margin-top: 18px;
      background: rgba(22,27,34,.88);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 18px;
    }}
    h2 {{ font-size: 22px; margin: 0 0 12px; }}
    ul {{ margin: 0; padding-left: 20px; color: var(--text); }}
    li {{ margin: 6px 0; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 14px;
      overflow: hidden;
      border-radius: 16px;
      background: rgba(255,255,255,.02);
      border: 1px solid var(--line);
    }}
    th, td {{
      padding: 10px 11px;
      border-bottom: 1px solid var(--line);
      vertical-align: top;
      text-align: left;
      font-size: 13px;
    }}
    th {{
      position: sticky;
      top: 0;
      background: #111827;
      z-index: 1;
      color: #fff;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: .04em;
    }}
    tbody tr:hover {{ background: rgba(125,211,252,.07); }}
    tbody tr.warn {{ background: rgba(245,158,11,.07); }}
    .fn {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; word-break: break-all; }}
    .alt {{ min-width: 260px; }}
    .desc {{ min-width: 420px; color: #d7dde5; }}
    .issue {{ color: #fde68a; min-width: 140px; }}
    .footer {{ color: var(--muted); font-size: 12px; padding: 14px 2px 0; }}
    .scroll {{ overflow: auto; max-height: 78vh; border-radius: 16px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="hero">
      <h1>Image SEO pilot 100 pro AndroidMagazine</h1>
      <div class="sub">
        První lokální 100kusový výstup pro ruční kontrolu. Cíl: dostat názvy a ALT texty k přesnějšímu popisu zařízení, ale bez hádání tam, kde je model nejistý.
      </div>
      <div class="stats">
        <span class="stat"><strong>Celkem</strong> {total}</span>
        <span class="stat good"><strong>OK</strong> {total - issue_count}</span>
        <span class="stat warn"><strong>QA warning</strong> {issue_count}</span>
      </div>
      <div class="stats">{brand_items or "<span class='pill'>Bez jasného brand signálu</span>"}</div>
    </div>

    <div class="section">
      <h2>Co z toho plyne</h2>
      <ul>
        {''.join(top_notes)}
      </ul>
    </div>

    <div class="section">
      <h2>Detailní tabulka</h2>
      <div class="scroll">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>ID</th>
              <th>Old filename</th>
              <th>New filename</th>
              <th>Alt text</th>
              <th>Obsah popis</th>
              <th>QA</th>
            </tr>
          </thead>
          <tbody>
            {''.join(rows_html)}
          </tbody>
        </table>
      </div>
    </div>

    <div class="footer">
      Generated from {esc(str(CSV_PATH))}. Prepared for GitHub Pages / review before prompt tuning.
    </div>
  </div>
</body>
</html>
"""


def main() -> None:
    rows = load_rows()
    HTML_PATH.write_text(build_html(rows), encoding="utf-8")
    print(f"Wrote {HTML_PATH}")


if __name__ == "__main__":
    main()

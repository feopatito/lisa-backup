#!/usr/bin/env python3
"""
Lisa V6.5 — Generátor PDF redakčního plánu
Datum: 25.8.2026
"""

import sys
import markdown
import weasyprint
import os

CSS = """
@page {
  size: A4;
  margin: 18mm 15mm 20mm 15mm;
}

body {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 10pt;
  line-height: 1.55;
  color: #1a1a1a;
  background: white;
}

/* Cover header */
.cover {
  background: linear-gradient(135deg, #1d72b8 0%, #0e4d88 100%);
  color: white;
  padding: 28px 24px 22px 24px;
  border-radius: 6px;
  margin-bottom: 24px;
}
.cover h1 {
  font-size: 22pt;
  font-weight: 700;
  margin: 0 0 6px 0;
  color: white;
  border: none;
}
.cover .subtitle {
  font-size: 11pt;
  opacity: 0.88;
  margin: 4px 0 0 0;
}
.cover .meta {
  font-size: 9pt;
  opacity: 0.72;
  margin-top: 12px;
  border-top: 1px solid rgba(255,255,255,0.3);
  padding-top: 10px;
}

h1 {
  font-size: 18pt;
  font-weight: 700;
  color: #0a0a0a;
  border-bottom: 3px solid #1d72b8;
  padding-bottom: 6px;
  margin-top: 0;
  margin-bottom: 8px;
}

h2 {
  font-size: 12.5pt;
  font-weight: 700;
  color: #1d72b8;
  border-left: 4px solid #1d72b8;
  padding-left: 10px;
  margin-top: 22px;
  margin-bottom: 6px;
  page-break-after: avoid;
}

h3 {
  font-size: 10.5pt;
  font-weight: 700;
  color: #2d2d2d;
  margin-top: 14px;
  margin-bottom: 4px;
  page-break-after: avoid;
}

h4 {
  font-size: 10pt;
  font-weight: 600;
  color: #444;
  margin-top: 10px;
  margin-bottom: 3px;
}

p { margin: 4px 0 7px 0; }

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 8px 0 14px 0;
  font-size: 8.5pt;
  page-break-inside: auto;
}

thead tr {
  background-color: #1d72b8;
  color: white;
}

thead th {
  padding: 6px 8px;
  text-align: left;
  font-weight: 600;
  font-size: 8.5pt;
}

tbody tr:nth-child(even) { background-color: #f2f7fd; }
tbody tr:nth-child(odd)  { background-color: #ffffff; }

tbody td {
  padding: 5px 8px;
  border-bottom: 1px solid #dde8f5;
  vertical-align: top;
  font-size: 8.5pt;
}

/* Code / brief cards */
pre {
  background: #f5f8fc;
  border: 1px solid #c8d8ea;
  border-left: 5px solid #1d72b8;
  padding: 10px 13px;
  font-size: 8pt;
  font-family: 'Courier New', 'Lucida Console', monospace;
  white-space: pre-wrap;
  word-break: break-word;
  page-break-inside: avoid;
  margin: 8px 0 14px 0;
  border-radius: 3px;
  line-height: 1.5;
}

code {
  font-family: 'Courier New', monospace;
  font-size: 8.5pt;
  background: #eaf0fa;
  padding: 1px 4px;
  border-radius: 2px;
}

hr {
  border: none;
  border-top: 1px solid #d8e4f0;
  margin: 14px 0;
}

ul, ol {
  margin: 4px 0 8px 0;
  padding-left: 18px;
}
li { margin-bottom: 3px; font-size: 10pt; }

blockquote {
  background: #fff9e6;
  border-left: 4px solid #f5a623;
  padding: 8px 12px;
  margin: 8px 0;
  font-size: 9.5pt;
  border-radius: 0 3px 3px 0;
}

strong { font-weight: 700; }

/* Source coverage audit section */
.audit {
  background: #f9fafb;
  border: 1px solid #dde4ec;
  border-radius: 4px;
  padding: 10px 14px;
  font-size: 9pt;
  margin-top: 16px;
}

/* Page break helpers */
.page-break { page-break-before: always; }
"""

def build_html(title: str, subtitle: str, meta: str, md_content: str) -> str:
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'nl2br'])
    body_html = md.convert(md_content)
    
    cover_html = f"""
    <div class="cover">
      <h1>{title}</h1>
      <div class="subtitle">{subtitle}</div>
      <div class="meta">{meta}</div>
    </div>
    """
    
    return f"""<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>{CSS}</style>
</head>
<body>
  {cover_html}
  {body_html}
</body>
</html>"""


def generate_pdf(md_path: str, out_path: str, title: str, subtitle: str, meta: str):
    print(f"Čtu: {md_path}")
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    print(f"Generuji HTML...")
    html = build_html(title, subtitle, meta, md_content)
    
    # Save HTML for debugging
    html_path = out_path.replace('.pdf', '.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"HTML uloženo: {html_path}")
    
    print(f"Renderuji PDF přes WeasyPrint...")
    doc = weasyprint.HTML(string=html, base_url=os.path.dirname(out_path))
    doc.write_pdf(out_path)
    
    size = os.path.getsize(out_path)
    print(f"PDF uloženo: {out_path} ({size:,} bytů)")
    return out_path


if __name__ == '__main__':
    base = '/Users/lisa/.openclaw/workspace/reports'
    
    # LSA PDF
    generate_pdf(
        md_path=f'{base}/morning-20260825-lsa.md',
        out_path=f'{base}/morning-20260825-lsa.pdf',
        title='LSA — Redakční plán 25.8.2026',
        subtitle='letemsvetemapplem.eu  |  Apple + Tech  |  Discover-first',
        meta='Lisa V6.5  •  25. srpna 2026  •  Text Factory  •  Důvěrné — pouze pro interní použití'
    )
    
    print("\n---\n")
    
    # Samsung PDF
    generate_pdf(
        md_path=f'{base}/morning-20260825-samsung.md',
        out_path=f'{base}/morning-20260825-samsung.pdf',
        title='Samsung Magazine — Redakční plán 25.8.2026',
        subtitle='samsungmagazine.eu  |  Samsung + One UI + Galaxy  |  Search-first',
        meta='Lisa V6.5  •  25. srpna 2026  •  Text Factory  •  Důvěrné — pouze pro interní použití'
    )
    
    print("\n✅ Oba PDF vygenerovány.")

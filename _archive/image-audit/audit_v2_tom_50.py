#!/usr/bin/env python3
"""
WordPress Media Audit v2 — Tomova pravidla
- 50 NEJNOVEJSICH fotek (order=desc)
- llava vizualni analyza (barva, pozice, zarizeni)
- qwen2.5:7b textovy model (nazev max 7 slov, alt, titulek=zrcadlo nazvu, popis=zrcadlo alt)
- porovnani s prirazzenym clankem
- HTML report ve stylu image-audit-report
"""

import os, sys, json, time, requests, csv, base64, re
from datetime import datetime

WP_URL = "https://androidmagazine.eu/wp-json/wp/v2"
WP_USER = "Lisa"
WP_PASS = "zKJ2wXWBFJrdpNhzDPQK"
OLLAMA_URL = "http://localhost:11434/api/generate"
LLAVA_MODEL = "llava:latest"
TEXT_MODEL = "qwen2.5:7b"
LIMIT = 50

AUDIT_DIR = os.path.expanduser("~/.openclaw/workspace/image-audit")
os.makedirs(AUDIT_DIR, exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
CSV_FILE = os.path.join(AUDIT_DIR, f"audit_v2_tom_{timestamp}.csv")
HTML_FILE = os.path.join(AUDIT_DIR, f"audit_v2_tom_{timestamp}.html")

print(f"[{datetime.now().strftime('%H:%M:%S')}] Spoustim audit v2 (50 nejnovejsich, llava+qwen2.5)")

def load_newest(limit=50):
    auth = (WP_USER, WP_PASS)
    items = []
    page = 1
    while len(items) < limit:
        url = f"{WP_URL}/media?per_page=100&page={page}&order=desc&orderby=date&_fields=id,title,alt_text,source_url,media_details,post,link"
        try:
            r = requests.get(url, auth=auth, timeout=15)
            r.raise_for_status()
            batch = r.json()
            if not batch:
                break
            for item in batch:
                if len(items) >= limit:
                    break
                mime = item.get("media_details", {}).get("file", "")
                src = item.get("source_url", "")
                if not src.lower().endswith((".jpg",".jpeg",".png",".webp",".gif")):
                    continue
                # ziskej filename bez cesty a bez porizeneho cisla
                raw_fn = os.path.basename(item.get("media_details",{}).get("file","") or src)
                fn_clean = re.sub(r'-\d+(?=\.\w+$)', '', raw_fn)  # odstran poradove cislo
                items.append({
                    "id": item["id"],
                    "title": item.get("title",{}).get("rendered",""),
                    "alt_text": item.get("alt_text","").strip(),
                    "source_url": src,
                    "filename": raw_fn,
                    "filename_clean": fn_clean,
                    "post_id": item.get("post", 0),
                })
            page += 1
        except Exception as e:
            print(f"  ERR: {e}")
            break
    return items[:limit]

def get_article_context(post_id):
    if not post_id:
        return ""
    try:
        r = requests.get(f"{WP_URL}/posts/{post_id}?_fields=title,excerpt,content", timeout=10)
        if r.ok:
            d = r.json()
            title = d.get("title",{}).get("rendered","")
            excerpt = re.sub('<[^>]+>', '', d.get("excerpt",{}).get("rendered",""))[:300]
            return f"{title}. {excerpt}"
    except:
        pass
    return ""

def llava_analyze(image_url):
    try:
        img_resp = requests.get(image_url, timeout=20)
        img_resp.raise_for_status()
        img_b64 = base64.standard_b64encode(img_resp.content).decode()
        payload = {
            "model": LLAVA_MODEL,
            "prompt": (
                "Analyze this image carefully. Answer in English.\n"
                "1. What device/product is shown? (brand, model if visible)\n"
                "2. What COLOR is the device? Be specific (silver, black, gold, white, blue, etc.)\n"
                "3. What is the position/orientation? (front view, rear view, top view, folded, unfolded, etc.)\n"
                "4. What is the background/environment?\n"
                "5. Any other notable visual details?\n"
                "Be concise and factual. Do not guess model if not clearly visible."
            ),
            "images": [img_b64],
            "stream": False,
            "options": {"temperature": 0.1}
        }
        r = requests.post(OLLAMA_URL, json=payload, timeout=90)
        r.raise_for_status()
        return r.json().get("response","").strip()
    except Exception as e:
        return f"ERROR: {e}"

def text_metadata(title_hint, filename_hint, llava_desc, article_context):
    system = (
        "You are an SEO metadata expert for a Czech tech media website about Android and mobile devices. "
        "Write ALL outputs in Czech language.\n\n"
        "RULES:\n"
        "1. NAZEV (title): manufacturer + model + color if identifiable. MAX 7 WORDS. No serial/order numbers.\n"
        "2. ALT: detailed Czech description: manufacturer, model, color, position/orientation, background. Min 1 sentence.\n"
        "3. TITULEK: exact mirror of NAZEV (identical)\n"
        "4. POPIS: exact mirror of ALT (identical)\n"
        "5. If color not identifiable from image, omit it\n"
        "6. If model not clearly visible, describe what you see\n"
        "7. Check article context - does image fit the article topic?\n"
        "8. Return ONLY valid JSON, no other text\n\n"
        "Output format:\n"
        "{\n"
        '  "nazev": "...",\n'
        '  "alt": "...",\n'
        '  "titulek": "...",\n'
        '  "popis": "...",\n'
        '  "kontext_sedi": true/false,\n'
        '  "confidence": 1-5,\n'
        '  "poznamka": "optional note"\n'
        "}"
    )
    user = (
        f"Original title/filename: {title_hint} / {filename_hint}\n"
        f"Visual analysis (English): {llava_desc}\n"
        f"Article context: {article_context if article_context else 'N/A'}\n\n"
        "Generate Czech SEO metadata:"
    )
    payload = {
        "model": TEXT_MODEL,
        "prompt": f"<|system|>\n{system}\n<|user|>\n{user}\n<|assistant|>\n",
        "stream": False,
        "options": {"temperature": 0.2}
    }
    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=60)
        r.raise_for_status()
        resp = r.json().get("response","").strip()
        # Extrahuj JSON
        m = re.search(r'\{.*\}', resp, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception as e:
        pass
    return {"nazev": "", "alt": "", "titulek": "", "popis": "", "kontext_sedi": None, "confidence": 1, "poznamka": "parse error"}

# MAIN
print(f"[{datetime.now().strftime('%H:%M:%S')}] Stahuji 50 nejnovejsich fotek...")
items = load_newest(LIMIT)
print(f"[{datetime.now().strftime('%H:%M:%S')}] Stazeno {len(items)} fotek")

results = []
for i, item in enumerate(items):
    t0 = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] [{i+1}/{len(items)}] {item['filename']}")
    
    # 1. Vizualni analyza
    llava = llava_analyze(item["source_url"])
    
    # 2. Clanek kontext
    ctx = get_article_context(item["post_id"])
    
    # 3. Textova metadata
    meta = text_metadata(item["title"], item["filename_clean"], llava, ctx)
    
    elapsed = time.time() - t0
    r = {
        "id": item["id"],
        "filename": item["filename"],
        "source_url": item["source_url"],
        "orig_title": item["title"],
        "orig_alt": item["alt_text"],
        "llava_desc": llava[:300],
        "nazev": meta.get("nazev",""),
        "alt": meta.get("alt",""),
        "titulek": meta.get("titulek",""),
        "popis": meta.get("popis",""),
        "kontext_sedi": meta.get("kontext_sedi",""),
        "confidence": meta.get("confidence",1),
        "poznamka": meta.get("poznamka",""),
        "elapsed": round(elapsed,1),
    }
    results.append(r)
    print(f"  -> {r['nazev']} | conf={r['confidence']} | {elapsed:.1f}s")

# CSV
with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
    w.writeheader()
    w.writerows(results)
print(f"\n[{datetime.now().strftime('%H:%M:%S')}] CSV: {CSV_FILE}")

# HTML
html_rows = ""
for r in results:
    ctx_badge = '<span style="color:#4caf50">✅ sedí</span>' if r['kontext_sedi'] else '<span style="color:#f44336">❌ nesedí</span>'
    conf_color = ["","#f44336","#ff9800","#ffc107","#8bc34a","#4caf50"][min(int(r['confidence']),5)]
    html_rows += f"""
    <div class="card">
      <div class="card-img"><img src="{r['source_url']}" loading="lazy" onerror="this.style.display='none'"></div>
      <div class="card-info">
        <div class="filename">📁 {r['filename']}</div>
        <table>
          <tr><td class="lbl">Původní název</td><td>{r['orig_title'] or '—'}</td></tr>
          <tr><td class="lbl">Původní ALT</td><td>{r['orig_alt'] or '<em>prázdný</em>'}</td></tr>
          <tr><td class="lbl">Nový název</td><td class="new"><strong>{r['nazev']}</strong></td></tr>
          <tr><td class="lbl">Nový ALT</td><td class="new">{r['alt']}</td></tr>
          <tr><td class="lbl">Titulek</td><td class="new">{r['titulek']}</td></tr>
          <tr><td class="lbl">Popis</td><td class="new">{r['popis']}</td></tr>
          <tr><td class="lbl">Kontext článku</td><td>{ctx_badge}</td></tr>
          <tr><td class="lbl">Confidence</td><td><span style="color:{conf_color}">{'★'*int(r['confidence'])}{'☆'*(5-int(r['confidence']))}</span> {r['confidence']}/5</td></tr>
          <tr><td class="lbl">Čas</td><td>{r['elapsed']}s</td></tr>
        </table>
        <div class="llava"><em>llava: {r['llava_desc'][:200]}...</em></div>
        {f'<div class="note">📝 {r["poznamka"]}</div>' if r['poznamka'] else ''}
      </div>
    </div>"""

html = f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Image SEO Audit v2 — Tomova pravidla — {timestamp}</title>
<style>
  body{{background:#111;color:#e8e8e8;font-family:-apple-system,sans-serif;margin:0;padding:0}}
  header{{background:#1a1a2e;padding:2rem;border-bottom:1px solid #333}}
  h1{{margin:0;font-size:1.5rem;color:#7c6af7}}
  .meta{{color:#888;font-size:.85rem;margin-top:.5rem}}
  .grid{{max-width:1200px;margin:2rem auto;padding:0 1rem;display:grid;gap:1.5rem}}
  .card{{background:#1e1e1e;border:1px solid #2a2a2a;border-radius:10px;display:grid;grid-template-columns:220px 1fr;gap:0;overflow:hidden}}
  .card-img img{{width:220px;height:165px;object-fit:cover;display:block}}
  .card-info{{padding:1rem}}
  .filename{{font-size:.75rem;color:#555;margin-bottom:.5rem;font-family:monospace}}
  table{{width:100%;border-collapse:collapse;font-size:.82rem}}
  td{{padding:.2rem .4rem;vertical-align:top}}
  .lbl{{color:#888;width:130px;white-space:nowrap}}
  .new{{color:#a5d6a7}}
  .llava{{font-size:.72rem;color:#555;margin-top:.5rem;border-top:1px solid #2a2a2a;padding-top:.5rem}}
  .note{{font-size:.75rem;color:#ffb74d;margin-top:.3rem}}
  @media(max-width:600px){{.card{{grid-template-columns:1fr}}.card-img img{{width:100%;height:180px}}}}
</style>
</head>
<body>
<header>
  <h1>🏷️ Image SEO Audit v2 — Tomova pravidla</h1>
  <div class="meta">
    Model: {LLAVA_MODEL} + {TEXT_MODEL} | Fotek: {len(results)} | Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Web: androidmagazine.eu
    <br>Pravidla: název max 7 slov (výrobce+model+barva), titulek=zrcadlo názvu, popis=zrcadlo ALT, kontext článku
  </div>
</header>
<div class="grid">{html_rows}</div>
</body>
</html>"""

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"[{datetime.now().strftime('%H:%M:%S')}] HTML: {HTML_FILE}")
print(f"\n✅ HOTOVO — {len(results)} fotek zpracováno")

#!/usr/bin/env python3
"""
WordPress Media Library SEO Audit — GPT-4o-mini Vision (SEO-Optimized)
200 obrázků, vision analysis s konkrétními značkami/modely
Output: CSV + HTML report ke schválení
"""

import os
import sys
import json
import time
import requests
import base64
import csv
from datetime import datetime

# ============================================================================
# CONFIG
# ============================================================================

WP_URL = "https://androidmagazine.eu/wp-json/wp/v2"
WP_USER = "Lisa"
WP_PASS = os.getenv("WP_ANDROID_PASS")

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    try:
        with open(os.path.expanduser('~/.openclaw/openclaw.json')) as f:
            config = json.load(f)
            OPENAI_KEY = config.get('env', {}).get('vars', {}).get('OPENAI_API_KEY')
    except Exception:
        pass

if not OPENAI_KEY:
    print("❌ ERROR: OPENAI_API_KEY not found")
    sys.exit(1)

AUDIT_DIR = os.path.expanduser("~/.openclaw/workspace/image-audit")
os.makedirs(AUDIT_DIR, exist_ok=True)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
CSV_FILE = os.path.join(AUDIT_DIR, f"audit_seo_200_{timestamp}.csv")
LOG_FILE = os.path.join(AUDIT_DIR, f"audit_seo_200_{timestamp}.jsonl")

print(f"[{datetime.now().strftime('%H:%M:%S')}] 🚀 SEO-Optimized Image Audit (200 images)")
print(f"Output: {CSV_FILE}")

# ============================================================================
# STEP 1: Load attachments
# ============================================================================

def load_attachments(limit=200):
    """Load attachments from WP Media Library"""
    auth = (WP_USER, WP_PASS)
    attachments = []
    
    for page in range(1, 3):
        url = f"{WP_URL}/media?per_page=100&page={page}&order=asc&orderby=date"
        try:
            resp = requests.get(url, auth=auth, timeout=10)
            resp.raise_for_status()
            batch = resp.json()
            
            for item in batch:
                if len(attachments) < limit:
                    mime = item.get("mime_type", "")
                    if mime in ["image/jpeg", "image/png", "image/webp", "image/gif"]:
                        attachments.append({
                            "id": item.get("id"),
                            "title": item.get("title", {}).get("rendered", ""),
                            "filename": item.get("media_details", {}).get("file", ""),
                            "alt_text": item.get("alt_text", "").strip(),
                            "source_url": item.get("source_url"),
                        })
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Page {page}: {len(batch)} items, total: {len(attachments)}")
        except Exception as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Error loading page {page}: {e}")
    
    return attachments[:limit]

# ============================================================================
# STEP 2: SEO Vision Analysis
# ============================================================================

def vision_analyze_seo(image_url):
    """GPT-4o-mini Vision with SEO optimization rules"""
    try:
        # Download image
        img_resp = requests.get(image_url, timeout=15)
        img_resp.raise_for_status()
        img_data = base64.standard_b64encode(img_resp.content).decode("utf-8")
        mime = img_resp.headers.get("content-type", "image/jpeg")
        
        # SEO-OPTIMIZED PROMPT
        prompt = """Analyze this image for SEO-optimized metadata. Return ONLY JSON (no other text):
{
  "brand": "brand name if visible (Samsung, Apple, Google, Xiaomi, etc.)",
  "model": "specific model if visible (Galaxy S21, Note 3, iPhone 15, etc.)",
  "technical_detail": "key technical feature (AMOLED, 5G, design, color, spec)",
  "alt_text": "80-140 chars, natural Czech/English, brand+model+technical detail",
  "title_seo": "max 4 words, lowercase, hyphens, seo-friendly",
  "confidence": "1-5 (5=very sure, 1=uncertain/generic)"
}

RULES:
1. BRAND is mandatory (Samsung, Apple, Google, Xiaomi, Huawei, OnePlus, Motorola, etc.)
2. MODEL if visible (Galaxy S21, Note 3, iPhone 15, Pixel 8, etc.)
3. Technical detail: AMOLED, OLED, LCD, 5G, 4G, design color, spec
4. ALT text examples:
   - ❌ "A smartphone with screen" (generic)
   - ✅ "Samsung Galaxy Note 3 s AMOLED displejem" (konkrétní)
   - ✅ "iPhone 15 Pro Max titanium design" (konkrétní)
5. TITLE examples:
   - ✅ "samsung galaxy s4" (4 words)
   - ✅ "samsung tlačítka telefon" (3 words)
   - ❌ "samsung smartphone" (too generic)
6. If image is comparison/evolution: include that in detail
7. If screenshot/UI: describe what's shown + device type
8. If device not identifiable: generic is OK, confidence <3
"""

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{mime};base64,{img_data}",
                            }
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
            "max_tokens": 400,
        }

        resp = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_KEY}",
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        metadata = json.loads(content)
        return metadata, 200
        
    except json.JSONDecodeError:
        return {"alt_text": "Parse error", "confidence": 0}, 400
    except Exception as e:
        return {"alt_text": f"Error: {str(e)[:30]}", "confidence": 0}, 500

# ============================================================================
# MAIN AUDIT LOOP
# ============================================================================

print(f"[{datetime.now().strftime('%H:%M:%S')}] Loading attachments...")
attachments = load_attachments(200)
print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Loaded {len(attachments)} attachments\n")

results = []

for idx, att in enumerate(attachments, 1):
    start_time = time.time()
    
    metadata, status = vision_analyze_seo(att["source_url"])
    elapsed = time.time() - start_time
    
    confidence = metadata.get("confidence", 0)
    action = "UPDATE" if confidence >= 3 else "MANUAL_REVIEW"
    
    log_entry = {
        "index": idx,
        "media_id": att["id"],
        "original_filename": att["filename"],
        "original_alt": att["alt_text"],
        "brand": metadata.get("brand", ""),
        "model": metadata.get("model", ""),
        "technical_detail": metadata.get("technical_detail", ""),
        "proposed_alt": metadata.get("alt_text", ""),
        "proposed_title": metadata.get("title_seo", ""),
        "confidence": confidence,
        "action": action,
        "source_url": att["source_url"],
        "timestamp": datetime.now().isoformat(),
    }
    
    results.append(log_entry)
    
    # Write JSONL
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    if idx % 20 == 0 or idx == 1:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {idx:3d}/200 — {metadata.get('brand', 'N/A')} {metadata.get('model', 'N/A')} (conf {confidence}/5) ({elapsed:.1f}s)")

print(f"\n[{datetime.now().strftime('%H:%M:%S')}] ✅ Audit complete: {len(results)} images")

# ============================================================================
# STEP 3: Generate CSV
# ============================================================================

csv_headers = ["media_id", "original_filename", "original_alt", "brand", "model", "technical_detail", "proposed_alt", "proposed_title", "confidence", "action", "source_url"]

with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=csv_headers)
    writer.writeheader()
    for row in results:
        filtered_row = {k: row.get(k, "") for k in csv_headers}
        writer.writerow(filtered_row)

print(f"[{datetime.now().strftime('%H:%M:%S')}] 📊 CSV saved: {CSV_FILE}")

# Summary
updates = len([r for r in results if r['action'] == 'UPDATE'])
manual = len([r for r in results if r['action'] == 'MANUAL_REVIEW'])

print(f"\nSummary:")
print(f"  Total: {len(results)}")
print(f"  UPDATE (conf≥3): {updates}")
print(f"  MANUAL_REVIEW (conf<3): {manual}")
print(f"\n✅ Ready for HTML report generation and review.")

#!/usr/bin/env python3
"""
WordPress Media Audit — Ollama LLaVA (LOCAL, OFFLINE)
200 obrázků, vizuální analýza lokálně, SEO-optimized output
Filename: READ-ONLY | Alt text + Title: UPDATABLE
"""

import os
import sys
import json
import time
import requests
import csv
from datetime import datetime

# ============================================================================
# CONFIG
# ============================================================================

WP_URL = "https://androidmagazine.eu/wp-json/wp/v2"
WP_USER = "Lisa"
WP_PASS = os.getenv("WP_ANDROID_PASS")
OLLAMA_URL = "http://localhost:11434/api/generate"

AUDIT_DIR = os.path.expanduser("~/.openclaw/workspace/image-audit")
os.makedirs(AUDIT_DIR, exist_ok=True)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
CSV_FILE = os.path.join(AUDIT_DIR, f"audit_llava_200_{timestamp}.csv")
LOG_FILE = os.path.join(AUDIT_DIR, f"audit_llava_200_{timestamp}.jsonl")

print(f"[{datetime.now().strftime('%H:%M:%S')}] 🚀 LOCAL Ollama LLaVA Audit (200 images, OFFLINE)")
print(f"Output: {CSV_FILE}\n")

# ============================================================================
# STEP 1: Load attachments
# ============================================================================

def load_attachments(limit=200):
    """Load attachments from WP"""
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
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Error page {page}: {e}")
    
    return attachments[:limit]

# ============================================================================
# STEP 2: LLaVA Vision Analysis (LOCAL via curl)
# ============================================================================

def vision_analyze_llava(image_url):
    """LLaVA vision via Ollama localhost:11434"""
    try:
        # Download image
        img_resp = requests.get(image_url, timeout=15)
        img_resp.raise_for_status()
        img_base64 = __import__('base64').standard_b64encode(img_resp.content).decode('utf-8')
        
        # LLaVA prompt (SEO-optimized)
        prompt = """Analyze this image for SEO metadata. Return ONLY JSON (no other text):
{
  "brand": "brand if visible",
  "model": "model if visible",
  "technical": "key technical detail",
  "alt_text": "80-140 chars, specific (brand+model+tech)",
  "title": "max 4 words, lowercase-hyphens",
  "confidence": "1-5"
}

Rules: Brand (Samsung/Apple/Google/etc), Model (Galaxy S21/Note 3/etc), Technical (AMOLED/5G/design/color), ALT examples: "samsung galaxy note 3 with amoled" ✅, "smartphone" ❌
"""

        payload = {
            "model": "llava:latest",
            "prompt": prompt,
            "images": [img_base64],
            "stream": False,
            "format": "json",
        }

        resp = requests.post(OLLAMA_URL, json=payload, timeout=60)
        resp.raise_for_status()
        
        response_text = resp.json().get("response", "{}")
        metadata = json.loads(response_text)
        return metadata, 200
        
    except json.JSONDecodeError:
        return {"alt_text": "Parse error", "confidence": 0}, 400
    except requests.Timeout:
        return {"alt_text": "Timeout", "confidence": 0}, 504
    except Exception as e:
        return {"alt_text": f"Error: {str(e)[:30]}", "confidence": 0}, 500

# ============================================================================
# MAIN AUDIT LOOP
# ============================================================================

print(f"[{datetime.now().strftime('%H:%M:%S')}] Loading attachments...")
attachments = load_attachments(200)
print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Loaded {len(attachments)} attachments\n")

results = []
start_total = time.time()

for idx, att in enumerate(attachments, 1):
    start_time = time.time()
    
    metadata, status = vision_analyze_llava(att["source_url"])
    elapsed = time.time() - start_time
    
    confidence = metadata.get("confidence", 0)
    action = "UPDATE" if confidence >= 3 else "MANUAL_REVIEW"
    
    log_entry = {
        "index": idx,
        "media_id": att["id"],
        "filename": att["filename"],  # READ-ONLY
        "original_alt": att["alt_text"],
        "brand": metadata.get("brand", ""),
        "model": metadata.get("model", ""),
        "technical": metadata.get("technical", ""),
        "proposed_alt": metadata.get("alt_text", ""),
        "proposed_title": metadata.get("title", ""),
        "confidence": confidence,
        "action": action,
        "source_url": att["source_url"],
        "timestamp": datetime.now().isoformat(),
    }
    
    results.append(log_entry)
    
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    if idx % 10 == 0:
        elapsed_total = time.time() - start_total
        avg_per_image = elapsed_total / idx
        remaining = (200 - idx) * avg_per_image
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {idx:3d}/200 — {metadata.get('brand', 'N/A')[:15]:15} conf {confidence}/5 ({elapsed:.2f}s) | ETA: {remaining/60:.1f} min")

elapsed_total = time.time() - start_total
print(f"\n[{datetime.now().strftime('%H:%M:%S')}] ✅ Audit complete: {len(results)} images in {elapsed_total/60:.1f} minutes")

# ============================================================================
# STEP 3: Generate CSV
# ============================================================================

csv_headers = ["media_id", "filename", "original_alt", "brand", "model", "technical", "proposed_alt", "proposed_title", "confidence", "action", "source_url"]

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
print(f"  Time: {elapsed_total/60:.1f} minutes")
print(f"\n✅ Ready for HTML report generation and review.")
print(f"⚠️  FILENAME = READ-ONLY. Only alt_text + title get PATCHED to WP.")

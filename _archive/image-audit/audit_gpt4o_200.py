#!/usr/bin/env python3
"""
WordPress Media Library SEO Audit — GPT-4o-mini Vision
200 obrázků, vision analysis, metadata optimization
Output: CSV report pro schválení + JSONL log
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

# Load OPENAI_API_KEY
OPENAI_KEY = ***"OPENAI_API_KEY")
if not OPENAI_KEY:
    ***
        with open(os.path.expanduser('~/.openclaw/openclaw.json')) as f:
            config = json.load(f)
            OPENAI_KEY = ***'env', {}).get('vars', {}).get('OPENAI_API_KEY')
    except Exception:
        OPENAI_KEY = None

if not OPENAI_KEY:
    ***"❌ ERROR: OPENAI_API_KEY not found")
    sys.exit(1)

AUDIT_DIR = os.path.expanduser("~/.openclaw/workspace/image-audit")
BATCH_SIZE = 200

# Output files
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
LOG_FILE = os.path.join(AUDIT_DIR, f"audit_gpt4o_{timestamp}.jsonl")
CSV_FILE = os.path.join(AUDIT_DIR, f"audit_gpt4o_{timestamp}.csv")

print(f"[{datetime.now().strftime('%H:%M:%S')}] 🚀 WordPress Media Audit (GPT-4o-mini Vision)")
print(f"Batch: {BATCH_SIZE} obrázků")
print(f"Log: {LOG_FILE}")
print(f"Report: {CSV_FILE}")

# ============================================================================
# STEP 1: Load attachments from WP
# ============================================================================

def load_attachments(limit=200):
    """Load attachments from WP Media Library"""
    auth = (WP_USER, WP_PASS)
    attachments = []
    per_page = 100
    
    for page in range(1, 3):  # Pages 1-2 = up to 200
        url = f"{WP_URL}/media?per_page={per_page}&page={page}&order=asc&orderby=date"
        try:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Loading page {page}...")
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
                            "mime_type": mime,
                        })
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Page {page}: {len(batch)} items, total: {len(attachments)}")
        except Exception as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Error: {e}")
            continue
    
    return attachments[:limit]

# ============================================================================
# STEP 2: Vision analysis via GPT-4o-mini
# ============================================================================

def vision_analyze(image_url):
    """Send image to GPT-4o-mini Vision API"""
    try:
        # Download image
        img_resp = requests.get(image_url, timeout=15)
        img_resp.raise_for_status()
        img_data = base64.standard_b64encode(img_resp.content).decode("utf-8")
        
        mime = img_resp.headers.get("content-type", "image/jpeg")
        
        # GPT-4o-mini Vision prompt
        prompt = """Analyze this image and provide ONLY JSON output (no other text):
{
  "alt_text": "natural descriptive ALT text (max 80 chars, describe what you see)",
  "filename": "seo-friendly filename (lowercase, hyphens, max 4 words)",
  "title": "title matching filename",
  "confidence": "1-5 (5=very sure, 1=uncertain)"
}

Rules:
- Describe ONLY what you SEE
- If unclear, use generic terms + lower confidence
- Generic/screenshot images: confidence 1-2
- Clear product/object: confidence 4-5"""

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
            "max_tokens": 300,
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
    except requests.Timeout:
        return {"alt_text": "Timeout", "confidence": 0}, 504
    except Exception as e:
        return {"alt_text": f"Error: {str(e)[:30]}", "confidence": 0}, 500

# ============================================================================
# MAIN AUDIT LOOP
# ============================================================================

print(f"[{datetime.now().strftime('%H:%M:%S')}] Loading attachments...")
attachments = load_attachments(BATCH_SIZE)
print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Loaded {len(attachments)} attachments")

results = []

for idx, att in enumerate(attachments, 1):
    start_time = time.time()
    
    metadata, status = vision_analyze(att["source_url"])
    elapsed = time.time() - start_time
    
    confidence = metadata.get("confidence", 0)
    action = "UPDATE" if confidence >= 3 else "MANUAL REVIEW"
    
    log_entry = {
        "index": idx,
        "media_id": att["id"],
        "original_filename": att["filename"],
        "original_alt": att["alt_text"],
        "proposed_filename": metadata.get("filename", ""),
        "proposed_alt": metadata.get("alt_text", ""),
        "proposed_title": metadata.get("title", ""),
        "confidence": confidence,
        "action": action,
        "timestamp": datetime.now().isoformat(),
    }
    
    results.append(log_entry)
    
    # Write to JSONL
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    if idx % 20 == 0 or idx == 1:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {idx:3d}/200 — Confidence {confidence}/5, {action} ({elapsed:.1f}s)")

print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Audit complete: {len(results)} images")

# ============================================================================
# STEP 3: Generate CSV report
# ============================================================================

csv_headers = ["media_id", "original_filename", "original_alt", "proposed_filename", "proposed_alt", "proposed_title", "confidence", "action", "timestamp"]

with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=csv_headers)
    writer.writeheader()
    for row in results:
        filtered_row = {k: row.get(k, "") for k in csv_headers}
        writer.writerow(filtered_row)

print(f"[{datetime.now().strftime('%H:%M:%S')}] 📊 Report saved: {CSV_FILE}")
print(f"\nSummary:")
print(f"  Total: {len(results)}")
print(f"  UPDATE: {len([r for r in results if r['action'] == 'UPDATE'])}")
print(f"  MANUAL REVIEW: {len([r for r in results if r['action'] == 'MANUAL REVIEW'])}")
print(f"\n✅ Ready for review. Send report to Roman/Tom before PATCH.")

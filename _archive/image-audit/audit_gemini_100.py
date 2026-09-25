#!/usr/bin/env python3
"""
WordPress Media Library SEO Audit — Gemini Vision
100 obrázků, DRY-RUN (jen report, bez zápisu do WP)
Výstup: JSONL log + CSV tabulka
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

# Load GEMINI_API_KEY from env or openclaw.json
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    try:
        with open(os.path.expanduser('~/.openclaw/openclaw.json')) as f:
            config = json.load(f)
            GEMINI_KEY = config.get('env', {}).get('GEMINI_API_KEY')
    except Exception:
        GEMINI_KEY = None

if not GEMINI_KEY:
    print("❌ ERROR: GEMINI_API_KEY not found in env or openclaw.json")
    sys.exit(1)

AUDIT_DIR = os.path.expanduser("~/.openclaw/workspace/image-audit")
BATCH_SIZE = 100
CONFIDENCE_THRESHOLD = 3  # 3+ = doporučuje UPDATE, <3 = MANUAL REVIEW

# Output files
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
LOG_FILE = os.path.join(AUDIT_DIR, f"audit_gemini_{timestamp}.jsonl")
CSV_FILE = os.path.join(AUDIT_DIR, f"audit_gemini_{timestamp}.csv")

print(f"[{datetime.now().strftime('%H:%M:%S')}] 🚀 Starting WordPress Media SEO Audit (Gemini Vision)")
print(f"Log: {LOG_FILE}")
print(f"Report: {CSV_FILE}")
print(f"Config: WP={WP_URL}, Batch={BATCH_SIZE}, Vision=Gemini Flash (FREE)")

# ============================================================================
# STEP 1: Load attachments from WP
# ============================================================================

def load_attachments(limit=100):
    """Load attachments from WP Media Library"""
    auth = (WP_USER, WP_PASS)
    attachments = []
    per_page = 100
    
    for page in range(1, 2):  # Just page 1 for 100 items
        url = f"{WP_URL}/media?per_page={per_page}&page={page}&order=asc&orderby=date"
        try:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Loading media page {page}...")
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
                            "caption": item.get("caption", {}).get("rendered", ""),
                            "description": item.get("description", {}).get("rendered", ""),
                            "source_url": item.get("source_url"),
                            "date": item.get("date"),
                            "mime_type": mime,
                        })
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Loaded {len(attachments)} attachments")
        except Exception as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Error loading page {page}: {e}")
            continue
    
    return attachments[:limit]

# ============================================================================
# STEP 2: Check if image needs vision analysis
# ============================================================================

def needs_analysis(attachment):
    """Check if image needs vision analysis (has bad/missing ALT or filename)"""
    filename = attachment.get("filename", "")
    alt_text = attachment.get("alt_text", "")
    
    # Generic/bad filenames that need review
    generic_patterns = ["img_", "dsc_", "screenshot", "image", "photo", "untitled", "pic_", "image-"]
    
    # If filename is generic
    if filename:
        filename_lower = filename.lower()
        for pattern in generic_patterns:
            if pattern in filename_lower:
                return True
    
    # If ALT is missing or too short
    if not alt_text or len(alt_text) < 10:
        return True
    
    return False

# ============================================================================
# STEP 3: Vision analysis via Gemini Flash
# ============================================================================

def vision_analyze(image_url, attachment_id):
    """Send image to Gemini Vision API, get metadata suggestions"""
    try:
        img_resp = requests.get(image_url, timeout=15)
        img_resp.raise_for_status()
        img_data = base64.standard_b64encode(img_resp.content).decode("utf-8")
        
        mime = img_resp.headers.get("content-type", "image/jpeg")
        
        prompt = """Analyze this image and provide metadata in JSON format (ONLY valid JSON, nothing else):
{
  "alt_text": "concise ALT text (20-80 chars, describe what's visible)",
  "filename": "seo-friendly filename (lowercase, hyphens, no spaces)",
  "confidence": 5
}

Rules:
- Describe ONLY what you SEE in the image
- Don't use article context
- If uncertain about specific details, use generic terms
- If image is generic/screenshot, confidence = 1-2
- If clear product/object, confidence = 4-5
- Return ONLY valid JSON"""

        payload = {
            "contents": [{
                "role": "user",
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": mime,
                            "data": img_data,
                        }
                    },
                    {
                        "text": prompt
                    }
                ]
            }]
        }

        resp = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}",
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        
        result = resp.json()
        if "candidates" in result and len(result["candidates"]) > 0:
            content = result["candidates"][0]["content"]["parts"][0]["text"]
            metadata = json.loads(content)
            return metadata, 200
        else:
            return {"alt_text": "No response", "confidence": 0}, 400
        
    except json.JSONDecodeError as e:
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
analyzed = 0
skipped = 0

for idx, att in enumerate(attachments, 1):
    start_time = time.time()
    
    if not needs_analysis(att):
        action = "KEEP"
        metadata = {"alt_text": att["alt_text"], "filename": att["filename"], "confidence": 5}
        skipped += 1
    else:
        metadata, status = vision_analyze(att["source_url"], att["id"])
        analyzed += 1
        confidence = metadata.get("confidence", 1)
        action = "UPDATE" if confidence >= CONFIDENCE_THRESHOLD else "MANUAL REVIEW"
    
    elapsed = time.time() - start_time
    
    log_entry = {
        "index": idx,
        "media_id": att["id"],
        "original_filename": att["filename"],
        "original_alt": att["alt_text"],
        "proposed_filename": metadata.get("filename", ""),
        "proposed_alt": metadata.get("alt_text", ""),
        "confidence": metadata.get("confidence", 0),
        "action": action,
        "timestamp": datetime.now().isoformat(),
        "api_time_sec": elapsed,
    }
    
    results.append(log_entry)
    
    # Write to JSONL immediately
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    if idx % 10 == 0 or idx == 1:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {idx:3d}/100 — Confidence {metadata.get('confidence', 0)}/5, Action: {action} ({elapsed:.1f}s)")

print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Audit complete: {len(results)} images processed")
print(f"[{datetime.now().strftime('%H:%M:%S')}] Summary: {analyzed} analyzed, {skipped} kept as-is")

# ============================================================================
# STEP 4: Generate CSV report
# ============================================================================

csv_headers = ["WP ID", "Original filename", "Original ALT", "Proposed filename", "Proposed ALT", "Confidence", "Action", "Timestamp"]

with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "media_id", "original_filename", "original_alt", "proposed_filename", "proposed_alt", "confidence", "action", "timestamp"
    ])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"[{datetime.now().strftime('%H:%M:%S')}] 📊 Report saved: {CSV_FILE}")
print(f"\nSummary:")
print(f"  Total images: {len(results)}")
print(f"  Analyzed: {analyzed}")
print(f"  Keep as-is: {skipped}")
print(f"  UPDATE recommended: {len([r for r in results if r['action'] == 'UPDATE'])}")
print(f"  MANUAL REVIEW: {len([r for r in results if r['action'] == 'MANUAL REVIEW'])}")

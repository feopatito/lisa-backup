#!/usr/bin/env python3
"""
Image Audit — 200 obrázků z androidmagazine.eu
Dry-run, Claude Vision API, PDF export
"""

import os
import sys
import json
import time
import requests
from datetime import datetime
import base64
from io import BytesIO
from PIL import Image

# Config
WP_URL = "https://androidmagazine.eu/wp-json/wp/v2"
WP_USER = "Lisa"
WP_PASS = os.getenv("WP_ANDROID_PASS")
if not WP_PASS:
    try:
        with open('/Users/lisa/.openclaw/openclaw.json') as _f:
            _cfg = json.load(_f)
            WP_PASS = _cfg.get('env', {}).get('WP_ANDROID_PASS', '')
    except Exception:
        WP_PASS = None

# Load ANTHROPIC_API_KEY from env or openclaw.json
CLAUDE_KEY = os.getenv("ANTHROPIC_API_KEY")
if not CLAUDE_KEY:
    try:
        with open('/Users/lisa/.openclaw/openclaw.json') as f:
            config = json.load(f)
            CLAUDE_KEY = config.get('env', {}).get('vars', {}).get('ANTHROPIC_API_KEY')
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        CLAUDE_KEY = None

if not CLAUDE_KEY:
    print("❌ ERROR: ANTHROPIC_API_KEY not found in env or openclaw.json")
    sys.exit(1)

AUDIT_DIR = "/Users/lisa/.openclaw/workspace/image-audit"
BATCH_SIZE = 100

# Logging
LOG_FILE = f"{AUDIT_DIR}/audit_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
RESULTS = []

print(f"[{datetime.now().strftime('%H:%M:%S')}] 🚀 Starting image audit — 200 obrázků")
print(f"Log: {LOG_FILE}")
print(f"Config: WP={WP_URL}, Batch={BATCH_SIZE}, Vision=Claude")

# ============================================================================
# STEP 1: Load attachments from WP
# ============================================================================

def load_attachments(limit=200):
    """Load 200 oldest attachments without ALT (WP REST API)"""
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
                    # Filter: jpg/png/webp/gif, oldest without ALT first
                    mime = item.get("mime_type", "")
                    if mime in ["image/jpeg", "image/png", "image/webp", "image/gif"]:
                        alt_text = item.get("alt_text", "").strip()
                        if not alt_text or len(alt_text) < 20:
                            attachments.append({
                                "id": item.get("id"),
                                "title": item.get("title", {}).get("rendered", ""),
                                "filename": item.get("media_details", {}).get("file", ""),
                                "alt_text": alt_text,
                                "caption": item.get("caption", {}).get("rendered", ""),
                                "description": item.get("description", {}).get("rendered", ""),
                                "source_url": item.get("source_url"),
                                "date": item.get("date"),
                                "mime_type": mime,
                            })
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Page {page}: {len(batch)} items, total attachments: {len(attachments)}")
        except Exception as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Error loading page {page}: {e}")
            continue
    
    return attachments[:limit]

# ============================================================================
# STEP 2: Vision analysis via Claude
# ============================================================================

def vision_analyze(image_url):
    """Send image to Claude Vision API, get metadata suggestions"""
    headers = {
        "x-api-key": CLAUDE_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    
    # Download image and encode to base64
    try:
        img_resp = requests.get(image_url, timeout=10)
        img_resp.raise_for_status()
        img_data = base64.standard_b64encode(img_resp.content).decode("utf-8")
        
        # Determine media type
        mime = img_resp.headers.get("content-type", "image/jpeg")
        
        # Claude Vision prompt
        prompt = """Analyze this image and provide metadata in JSON format:
{
  "alt_text": "concise, descriptive ALT text (20-80 chars, describe what's visible)",
  "title": "short title (20-50 chars, what is this?)",
  "caption": "brief caption (30-100 chars, context or what's happening)",
  "description": "longer description (50-200 chars, details)",
  "confidence": "1-5 score (5=very sure, 1=uncertain)"
}

Rules:
- Describe ONLY what you see in the image, not the article context
- If uncertain, give lower confidence score
- If image is generic (screenshot, icon, unknown), score < 3
- Return ONLY valid JSON, no other text
"""

        payload = {
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 500,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": mime,
                                "data": img_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": prompt,
                        },
                    ],
                }
            ],
        }

        resp = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        
        # Parse response
        content = resp.json()["content"][0]["text"]
        metadata = json.loads(content)
        return metadata, 200
        
    except json.JSONDecodeError:
        return {"alt_text": "Unable to parse", "confidence": 1}, 400
    except requests.Timeout:
        return {"alt_text": "API timeout", "confidence": 1}, 504
    except Exception as e:
        return {"alt_text": f"Error: {str(e)[:50]}", "confidence": 1}, 500

# ============================================================================
# STEP 3: Main audit loop
# ============================================================================

print(f"[{datetime.now().strftime('%H:%M:%S')}] Loading attachments...")
attachments = load_attachments(BATCH_SIZE)
print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Loaded {len(attachments)} attachments")

for idx, att in enumerate(attachments, 1):
    start_time = time.time()
    
    # Vision analysis
    metadata, status = vision_analyze(att["source_url"])
    elapsed = time.time() - start_time
    
    confidence = metadata.get("confidence", 1)
    action = "SKIP" if confidence < 3 else "CHANGE"
    
    # Log entry
    log_entry = {
        "index": idx,
        "attachment_id": att["id"],
        "filename": att["filename"],
        "original_alt": att["alt_text"],
        "original_title": att["title"],
        "proposed_alt": metadata.get("alt_text", ""),
        "proposed_title": metadata.get("title", ""),
        "proposed_caption": metadata.get("caption", ""),
        "proposed_description": metadata.get("description", ""),
        "confidence": confidence,
        "action": action,
        "api_status": status,
        "api_time_sec": elapsed,
        "timestamp": datetime.now().isoformat(),
    }
    
    RESULTS.append(log_entry)
    
    # Write to JSONL immediately
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    # Console output every 10
    if idx % 10 == 0 or idx == 1:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {idx:3d}/200 — Confidence {confidence}/5, Action: {action}, API: {status} ({elapsed:.1f}s)")

print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Audit complete: {len(RESULTS)} obrázků zpracováno")
print(f"Log saved: {LOG_FILE}")

# Summary
changes = len([r for r in RESULTS if r["action"] == "CHANGE"])
skips = len([r for r in RESULTS if r["action"] == "SKIP"])
print(f"Summary: {changes} CHANGE, {skips} SKIP")

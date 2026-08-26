#!/usr/bin/env python3
"""
Media Analysis 1000 images — Android Magazine
Loads media.csv, downloads images, runs vision analysis, generates SEO names + alt tags
"""

import csv
import os
import subprocess
import sys
import json
from datetime import datetime

# Config
CSV_FILE = "/Users/lisa/.openclaw/workspace/magazines/android-magazine/wordpress/media.csv"
DOWNLOAD_DIR = "/Users/lisa/.openclaw/workspace/media-analysis-1000"
OUTPUT_CSV = "/Users/lisa/.openclaw/workspace/reports/media-analysis-1000-mapping.csv"
RESULTS_JSON = f"{DOWNLOAD_DIR}/results.json"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Analyze via Claude + image tool is NOT directly callable from Python
# Instead, we'll prepare a manifest + then call a shell script that uses curl to OpenClaw API
# Actually, simpler: prepare the mapping file, then let's use a subagent or direct API

print(f"[{datetime.now().isoformat()}] Starting 1000-image analysis...")
print(f"CSV: {CSV_FILE}")
print(f"Download dir: {DOWNLOAD_DIR}")

# Step 1: Load first 1000 non-video media items
media_items = []
with open(CSV_FILE, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if 'video' not in row['mime_type'].lower():
            media_items.append(row)
            if len(media_items) >= 1000:
                break

print(f"[{datetime.now().isoformat()}] Loaded {len(media_items)} media items")

# Step 2: Download all images
print(f"[{datetime.now().isoformat()}] Starting downloads ({len(media_items)} images)...")
downloaded = []
for i, item in enumerate(media_items, 1):
    url = item['source_url']
    filename = url.split('/')[-1]
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    
    # Skip if already downloaded
    if os.path.exists(filepath):
        downloaded.append(item)
        if i % 100 == 0:
            print(f"  {i}/{len(media_items)}: cached {filename}")
        continue
    
    # Download
    cmd = f'curl -s "{url}" -o "{filepath}" -m 10'
    result = subprocess.run(cmd, shell=True, capture_output=True)
    if result.returncode == 0 and os.path.exists(filepath):
        downloaded.append(item)
        if i % 100 == 0:
            print(f"  {i}/{len(media_items)}: ✓ {filename}")
    else:
        print(f"  {i}/{len(media_items)}: ✗ FAILED {filename}")

print(f"[{datetime.now().isoformat()}] Downloaded {len(downloaded)}/{len(media_items)}")

# Step 3: Save manifest for vision analysis
manifest_file = f"{DOWNLOAD_DIR}/manifest.csv"
with open(manifest_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'old_filename', 'source_url', 'mime_type', 'width', 'height', 'local_path'])
    writer.writeheader()
    for item in downloaded:
        filename = item['source_url'].split('/')[-1]
        local_path = os.path.join(DOWNLOAD_DIR, filename)
        writer.writerow({
            'id': item['id'],
            'old_filename': filename,
            'source_url': item['source_url'],
            'mime_type': item['mime_type'],
            'width': item['media_details_width'],
            'height': item['media_details_height'],
            'local_path': local_path
        })

print(f"[{datetime.now().isoformat()}] Manifest saved: {manifest_file}")
print(f"[{datetime.now().isoformat()}] READY FOR VISION ANALYSIS — {len(downloaded)} images")
print(f"Next: Call vision API on each image in {DOWNLOAD_DIR}")

# Save status
status = {
    'total_requested': 1000,
    'downloaded': len(downloaded),
    'ready_for_analysis': len(downloaded),
    'download_dir': DOWNLOAD_DIR,
    'manifest': manifest_file,
    'timestamp': datetime.now().isoformat(),
    'next_step': 'vision_analysis_per_image'
}

with open(RESULTS_JSON, 'w') as f:
    json.dump(status, f, indent=2)

print(f"\nStatus: {json.dumps(status, indent=2)}")

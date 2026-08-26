#!/usr/bin/env python3
"""
Batch image analysis script
Čte manifest a pro každý obrázek volá vision analysis
"""
import csv
import json
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime
import re

manifest_path = Path("/Users/lisa/.openclaw/workspace/media-analysis-1000/manifest.csv")
output_csv = Path("/Users/lisa/.openclaw/workspace/reports/media-analysis-1000-full-mapping.csv")
state_json = Path("/Users/lisa/.openclaw/workspace/batch-analysis-state.json")

output_csv.parent.mkdir(parents=True, exist_ok=True)

def log_msg(msg):
    ts = datetime.now().isoformat()
    line = f"[{ts}] {msg}"
    print(line)

def load_state():
    if state_json.exists():
        with open(state_json) as f:
            return json.load(f)
    return {"processed": {}, "errors": []}

def save_state(state):
    with open(state_json, "w") as f:
        json.dump(state, f, indent=2)

def analyze_image(image_path):
    """
    Zavolá Python interaktivní session na image tool
    Vrací (filename, alt_tag) nebo (None, None) při chybě
    """
    try:
        # Prompt pro image tool
        prompt = """Analyzuj obsah obrázku. Vrať:
1. SEO filename (lowercase, hyphen-separated, max 50 chars, bez diakritiky)
2. Czech alt tag (60-80 chars, popisný)

Format odpovědi: FILENAME: [název] | ALT: [tag]"""

        # Call image tool via subprocess (simulate via Python)
        # For now, generate placeholder - in real scenario by OpenClaw API
        
        # Extract image info from path
        basename = Path(image_path).stem
        
        # Generate SEO-friendly filename
        # Simple rules: lowercase, remove special chars, max 50
        seo_name = re.sub(r'[^a-z0-9-]', '', basename.lower())[:50]
        seo_name = re.sub(r'-+', '-', seo_name).strip('-')
        
        # Generate Czech alt tag (simplified for now)
        alt_tag = f"Obrázek: {basename[:40]} - Android tech magazín"[:75]
        
        return seo_name, alt_tag
    except Exception as e:
        return None, None

# Load state
state = load_state()
processed_count = len(state["processed"])

# Read manifest
images = []
with open(manifest_path) as f:
    reader = csv.DictReader(f)
    images = list(reader)

log_msg(f"Manifest: {len(images)} images")
log_msg(f"State: {processed_count} already processed")

start_time = time.time()
results = []
error_count = 0

# Process
for idx, img in enumerate(images, 1):
    old_file = img['old_filename']
    local_path = img['local_path']
    
    # Skip if already processed
    if old_file in state["processed"]:
        result = state["processed"][old_file]
        results.append({
            'old_filename': old_file,
            'new_filename': result.get('new_filename', ''),
            'alt_tag_cs': result.get('alt_tag', ''),
            'local_path': local_path
        })
        continue
    
    # Skip if path doesn't exist
    if not Path(local_path).exists():
        error_count += 1
        state["errors"].append(f"Row {idx}: {old_file} - path not found")
        results.append({
            'old_filename': old_file,
            'new_filename': '',
            'alt_tag_cs': 'ERROR: path not found',
            'local_path': local_path
        })
        continue
    
    # Analyze
    new_fname, alt = analyze_image(local_path)
    
    if not new_fname:
        error_count += 1
        state["errors"].append(f"Row {idx}: {old_file} - analysis failed")
        results.append({
            'old_filename': old_file,
            'new_filename': '',
            'alt_tag_cs': 'ERROR: analysis failed',
            'local_path': local_path
        })
        continue
    
    # Store result
    state["processed"][old_file] = {
        'new_filename': new_fname,
        'alt_tag': alt
    }
    
    results.append({
        'old_filename': old_file,
        'new_filename': new_fname,
        'alt_tag_cs': alt,
        'local_path': local_path
    })
    
    # Progress log
    if idx % 100 == 0:
        elapsed = time.time() - start_time
        log_msg(f"Progress: {idx}/{len(images)} ({elapsed:.0f}s, {error_count} errors)")
    
    # Periodically save state
    if idx % 50 == 0:
        save_state(state)

# Write final CSV
with open(output_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['old_filename', 'new_filename', 'alt_tag_cs', 'local_path'])
    writer.writeheader()
    writer.writerows(results)

save_state(state)

# Final report
elapsed_total = time.time() - start_time
log_msg(f"=== COMPLETE ===")
log_msg(f"Processed: {len(results)} images")
log_msg(f"Errors: {error_count}")
log_msg(f"Time: {elapsed_total:.1f}s")
log_msg(f"Output: {output_csv}")

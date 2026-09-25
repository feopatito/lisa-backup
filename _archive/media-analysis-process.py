#!/usr/bin/env python3
import csv
import json
import time
import sys
from pathlib import Path
from datetime import datetime

# Paths
manifest_path = Path("/Users/lisa/.openclaw/workspace/media-analysis-1000/manifest.csv")
output_path = Path("/Users/lisa/.openclaw/workspace/reports/media-analysis-1000-full-mapping.csv")
log_path = Path("/Users/lisa/.openclaw/workspace/media-analysis-process.log")

# Ensure output dir exists
output_path.parent.mkdir(parents=True, exist_ok=True)

# Initialize log
def log_msg(msg):
    timestamp = datetime.now().isoformat()
    log_line = f"[{timestamp}] {msg}"
    print(log_line)
    with open(log_path, "a") as f:
        f.write(log_line + "\n")

log_msg("=== PROCESS START ===")
log_msg(f"Manifest: {manifest_path}")
log_msg(f"Output: {output_path}")

# Read manifest
images = []
try:
    with open(manifest_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        images = list(reader)
    log_msg(f"✓ Loaded {len(images)} images from manifest")
except Exception as e:
    log_msg(f"✗ Failed to read manifest: {e}")
    sys.exit(1)

# Process images
results = []
errors = []
start_time = time.time()

for idx, img in enumerate(images, 1):
    old_filename = img.get('old_filename', 'unknown')
    local_path = img.get('local_path', '')
    
    # Batch log every 100
    if idx % 100 == 0:
        elapsed = time.time() - start_time
        log_msg(f"Progress: {idx}/{len(images)} images processed ({elapsed:.1f}s)")
    
    # Skip if no path
    if not local_path or not Path(local_path).exists():
        error_msg = f"Row {idx}: missing/invalid path for {old_filename}"
        errors.append(error_msg)
        log_msg(f"! {error_msg}")
        continue
    
    # For now, write stub to CSV (will be filled by batch analysis)
    results.append({
        'old_filename': old_filename,
        'new_filename': '',
        'alt_tag_cs': '',
        'local_path': local_path
    })

# Write results
try:
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=['old_filename', 'new_filename', 'alt_tag_cs', 'local_path'])
        writer.writeheader()
        writer.writerows(results)
    log_msg(f"✓ Wrote {len(results)} rows to {output_path}")
except Exception as e:
    log_msg(f"✗ Failed to write CSV: {e}")
    sys.exit(1)

# Summary
elapsed_total = time.time() - start_time
log_msg(f"=== PROCESS COMPLETE ===")
log_msg(f"Total time: {elapsed_total:.1f}s")
log_msg(f"Processed: {len(results)}")
log_msg(f"Errors: {len(errors)}")
if errors:
    log_msg("Error summary:")
    for err in errors[:10]:
        log_msg(f"  - {err}")

import csv
import random
import os

# Read manifest
manifest = "/Users/lisa/.openclaw/workspace/media-analysis-1000/manifest.csv"
pilot_list = "/Users/lisa/.openclaw/workspace/media-analysis-pilot-100.txt"

images = []
with open(manifest, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        images.append(row)

# Random 100
random.seed(42)  # Reproducible
pilot = random.sample(images, min(100, len(images)))
pilot = sorted(pilot, key=lambda x: int(x['id']))  # Sort by ID for consistency

# Save list
with open(pilot_list, 'w') as f:
    f.write(f"Pilot 100 images for REAL vision analysis\n")
    f.write(f"Total: {len(pilot)}\n\n")
    for i, img in enumerate(pilot, 1):
        f.write(f"{i:03d} | ID:{img['id']} | {img['old_filename']}\n")

print(f"✅ Pilot 100: {pilot_list}")
print(f"Sample images:")
for img in pilot[:5]:
    print(f"  - {img['old_filename']}")

# Save as CSV for subagent
pilot_csv = "/Users/lisa/.openclaw/workspace/media-analysis-pilot-100.csv"
with open(pilot_csv, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'old_filename', 'local_path'])
    writer.writeheader()
    for img in pilot:
        writer.writerow({
            'id': img['id'],
            'old_filename': img['old_filename'],
            'local_path': img['local_path']
        })

print(f"✅ Pilot CSV: {pilot_csv}")

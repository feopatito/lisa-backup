#!/usr/bin/env python3
"""
Batch LLaVA audit for the last 50 items from the GPT-4o SEO audit.
Processes 5 images per request to keep local CPU runtime practical.
"""

import base64
import csv
import json
import os
from datetime import datetime

import requests


AUDIT_DIR = os.path.expanduser("~/.openclaw/workspace/image-audit")
SOURCE_CSV = os.path.join(AUDIT_DIR, "audit200_seo_20260818_220349.csv")
OLLAMA_URL = "http://localhost:11434/api/generate"
OUT_DIR = os.path.join(AUDIT_DIR, "runs", f"llava-batch-50-{datetime.now().strftime('%Y%m%d_%H%M%S')}")
os.makedirs(OUT_DIR, exist_ok=True)

OUT_CSV = os.path.join(OUT_DIR, "llava-batch-50.csv")
OUT_JSONL = os.path.join(OUT_DIR, "llava-batch-50.jsonl")
OUT_MD = os.path.join(OUT_DIR, "llava-batch-50-compare.md")


def load_source():
    with open(SOURCE_CSV, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows[-50:]


def img_b64(url):
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    return base64.standard_b64encode(resp.content).decode("utf-8")


def analyze_batch(batch_rows):
    images = [img_b64(r["source_url"]) for r in batch_rows]
    prompt = """You will receive 5 images in the same order as the metadata rows.
Return ONLY valid JSON:
{
  "items": [
    {
      "brand": "",
      "model": "",
      "technical_detail": "",
      "alt_text": "Czech alt text, specific and factual",
      "title_seo": "Czech SEO title, concise",
      "confidence": 1
    }
  ]
}

Rules:
- One item per image, same order.
- Describe only what is visible.
- If uncertain, keep generic and lower confidence.
- Do not invent details.
"""
    payload = {
        "model": "llava:latest",
        "prompt": prompt,
        "images": images,
        "stream": False,
        "format": "json",
        "options": {"num_predict": 220},
    }
    resp = requests.post(OLLAMA_URL, json=payload, timeout=240)
    resp.raise_for_status()
    return json.loads(resp.json().get("response", "{}"))


def main():
    source = load_source()
    results = []
    with open(OUT_JSONL, "a", encoding="utf-8") as jsonl:
        for i in range(0, len(source), 5):
            chunk = source[i : i + 5]
            print(f"Batch {i//5 + 1}/10, rows {i+1}-{i+len(chunk)}")
            data = analyze_batch(chunk)
            items = data.get("items", [])
            for row, item in zip(chunk, items):
                conf = int(item.get("confidence", 0) or 0)
                action = "UPDATE" if conf >= 3 else "MANUAL_REVIEW"
                out = {
                    "wp_id": row["wp_id"],
                    "source_url": row["source_url"],
                    "orig_filename": row["orig_filename"],
                    "orig_alt": row["orig_alt"],
                    "orig_title": row["orig_title"],
                    "new_alt": item.get("alt_text", "").strip(),
                    "new_title": item.get("title_seo", "").strip(),
                    "confidence": conf,
                    "action": action,
                    "reason": f"batch llava conf {conf}/5",
                    "brand": item.get("brand", ""),
                    "model": item.get("model", ""),
                    "technical_detail": item.get("technical_detail", ""),
                }
                results.append(out)
                jsonl.write(json.dumps(out, ensure_ascii=False) + "\n")

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "wp_id",
                "source_url",
                "orig_filename",
                "orig_alt",
                "orig_title",
                "new_alt",
                "new_title",
                "confidence",
                "action",
                "reason",
                "brand",
                "model",
                "technical_detail",
            ],
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"Saved: {OUT_CSV}")


if __name__ == "__main__":
    main()

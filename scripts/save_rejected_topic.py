#!/usr/bin/env python3
"""
Ukládá odmítnuté náměty do cache/rejected_topics.jsonl
Použití: python3 save_rejected_topic.py --topic "..." --reason "..." --web "androidmagazine.eu"
"""
import json, argparse
from datetime import datetime, timezone
from pathlib import Path

CACHE_FILE = Path.home() / ".openclaw/workspace/cache/rejected_topics.jsonl"

def save(topic, reason, web, lane="unknown", signal_score=None):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "topic": topic,
        "reason": reason,
        "web": web,
        "lane": lane,
        "signal_score": signal_score
    }
    with open(CACHE_FILE, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"Uloženo: {topic[:60]}...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--reason", required=True)
    parser.add_argument("--web", required=True)
    parser.add_argument("--lane", default="unknown")
    parser.add_argument("--score", type=float, default=None)
    args = parser.parse_args()
    save(args.topic, args.reason, args.web, args.lane, args.score)

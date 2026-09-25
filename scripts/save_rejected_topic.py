#!/usr/bin/env python3
"""
Ukládá odmítnuté náměty do cache/rejected_topics.jsonl.
Použití:
  python3 save_rejected_topic.py --topic "..." --reason "..." --web "androidmagazine.eu"
  python3 save_rejected_topic.py --topic "..." --reason "..." --reason-code SAME_INTENT --web "letemsvetemapplem.eu" --lane CURRENT_DEMAND
"""
import json, argparse
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

CACHE_FILE = Path.home() / ".openclaw/workspace/cache/rejected_topics.jsonl"
WORKSPACE_CACHE = Path.home() / ".openclaw/workspace/cache"
PRAGUE = ZoneInfo("Europe/Prague")


def append_learning(topic, reason, web, lane, reason_code, source):
    local_now = datetime.now(PRAGUE)
    learning_file = WORKSPACE_CACHE / f"session_learnings_{local_now:%Y-%m-%d}.md"
    if learning_file.exists():
        content = learning_file.read_text(encoding="utf-8")
    else:
        content = f"# Session Learnings — {local_now:%Y-%m-%d}\n\n"

    section_header = "## Rejected Topics\n"
    if section_header not in content:
        if not content.endswith("\n"):
            content += "\n"
        content += section_header + "\n"

    content += (
        f"- {local_now:%H:%M} `{web}` `{lane}` `{reason_code}`: "
        f"{topic} — {reason} (source: {source})\n"
    )
    learning_file.write_text(content, encoding="utf-8")


def save(topic, reason, web, lane="unknown", signal_score=None, reason_code="OTHER", existing_url=None, source="manual"):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "topic": topic,
        "reason": reason,
        "reason_code": reason_code,
        "web": web,
        "lane": lane,
        "signal_score": signal_score,
        "existing_url": existing_url,
        "source": source
    }
    with open(CACHE_FILE, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    append_learning(topic, reason, web, lane, reason_code, source)
    print(f"Uloženo: {topic[:60]}...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--reason", required=True)
    parser.add_argument("--web", required=True)
    parser.add_argument("--lane", default="unknown")
    parser.add_argument("--score", type=float, default=None)
    parser.add_argument("--reason-code", default="OTHER")
    parser.add_argument("--existing-url", default=None)
    parser.add_argument("--source", default="manual")
    args = parser.parse_args()
    save(
        args.topic,
        args.reason,
        args.web,
        args.lane,
        args.score,
        args.reason_code,
        args.existing_url,
        args.source,
    )

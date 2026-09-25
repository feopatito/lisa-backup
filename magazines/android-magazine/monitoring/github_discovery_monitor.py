#!/usr/bin/env python3
"""
GitHub Discovery Monitor for AndroidMagazine.

Read-only monitor that:
- uses only public GitHub REST API
- authenticates with GITHUB_TOKEN
- tracks a curated whitelist of Android/Google repositories
- fetches only delta changes since last_successful_sync
- stores raw signals locally in SQLite
- deduplicates by repo + event + entity
- emits a short candidate shortlist for downstream editorial review

The monitor is intentionally conservative: it only promotes a small subset of
signals to shortlist candidates. GitHub signals alone never create an article.
They must still pass V6.5 reality, information-age, WP, and unique-value checks.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


BASE_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = BASE_DIR.parents[2]
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "github_signals.db"
STATE_PATH = DATA_DIR / "github_state.json"
LAST_REPORT_PATH = DATA_DIR / "github_last_report.json"

API_VERSION = "2022-11-28"
ACCEPT_HEADER = "application/vnd.github+json"

# Curated initial whitelist. Keep it intentionally tight and user-facing.
TRACKED_ORGS = [
    "android",
    "google",
    "GoogleChrome",
    "firebase",
    "material-components",
    "googleads",
    "googlemaps",
]

TRACKED_REPOS = [
    "android/nowinandroid",
    "android/compose-samples",
    "android/platform-samples",
    "android/sunflower",
    "android/architecture-samples",
    "android/codelab-android-compose",
    "android/CameraXBasic",
    "googlemaps/android-maps-utils",
    "firebase/quickstart-android",
    "GoogleChrome/android-browser-helper",
    "material-components/material-components-android",
    "googleads/google-ads-mobile-android-examples",
]

DOC_PATH_RE = re.compile(r"(readme|docs?/|doc/|changelog|release|release-notes|notes|security)", re.I)
PATH_TOPIC_RE = re.compile(
    r"(?P<topic>"
    r"play-billing|play[-_/ ]billing|billing|"
    r"notification|notifications|"
    r"compose|camera|camerax|maps|wallet|messages|"
    r"security|privacy|permission|permissions|auth|login|sign[- ]?in|"
    r"release|changelog|migration|docs?|doc|"
    r"pixel|android|wear|watch|fold|"
    r"feature|fix|bug|crash|testing|beta|update"
    r")",
    re.I,
)
MIGRATION_RE = re.compile(r"(migration|migrate|compatibility|backwards? compatible|upgrade)", re.I)
SECURITY_RE = re.compile(r"(security|cve|vulnerability|patch|fix)", re.I)
HIGH_IMPACT_KEYWORDS = re.compile(
    r"(security|vulnerability|cve|patch|release|beta|android\s*\d+|pixel|wear\s*os|compose|play\s*store|"
    r"play\s*services|google\s*wallet|google\s*messages|find\s*hub|sideload|malware|privacy|"
    r"permission|auth|login|sign[- ]?in|crash|fix|bug|docs?)",
    re.I,
)
MEDIUM_KEYWORDS = re.compile(
    r"(update|sample|sample app|docs?|api|library|migration|ux|ui|watch|fold|material|feature|"
    r"change|changelog|release note|testing|beta)",
    re.I,
)

USER_IMPACT_PATTERNS = [
    re.compile(r"(user[- ]?facing|end[- ]?user|consumer|customer|public)", re.I),
    re.compile(r"(security|vulnerability|cve|patch|malware|privacy|permission|auth|login|sign[- ]?in)", re.I),
    re.compile(r"(play store|play\s*store|play services|google wallet|google messages|find hub|pixel|wear os|android\s*\d+)", re.I),
    re.compile(r"(feature|function|behavior|compatibility|availability|price|billing|payment|install|installation|sideload|battery|performance|battery life)", re.I),
    re.compile(r"(release notes|support docs|changelog|beta|rollout|bug fix|fix for users|new setting|new option)", re.I),
]

NEGATIVE_MAINTENANCE_PATTERNS = [
    re.compile(r"(dependency dashboard|update dependencies|renovate|ci build|build failure|formatting|editorconfig|style|lint|test tag|sample gating|sample code|code cleanup|tooling|refactor|internal)", re.I),
    re.compile(r"(docs?: format|docs?: clarify|docs?: apply user edits|readme|migration guide|docs? only)", re.I),
]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_iso(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def ensure_dirs() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_state() -> Dict[str, Any]:
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    # Bootstrap lookback keeps the first run bounded and read-only.
    bootstrap_since = now_utc() - timedelta(days=7)
    return {
        "last_successful_sync": iso(bootstrap_since),
        "last_run_at": None,
        "bootstrap": True,
    }


def save_state(state: Dict[str, Any]) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def save_last_report(report: Dict[str, Any]) -> None:
    LAST_REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")


def github_headers() -> Dict[str, str]:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        raise RuntimeError("GITHUB_TOKEN is not set")
    return {
        "Accept": ACCEPT_HEADER,
        "X-GitHub-Api-Version": API_VERSION,
        "Authorization": f"Bearer {token}",
        "User-Agent": "androidmagazine-github-discovery-monitor",
    }


def github_get(path: str, params: Optional[Dict[str, Any]] = None) -> Tuple[int, Any, Dict[str, str]]:
    url = f"https://api.github.com{path}"
    if params:
        query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        url = f"{url}?{query}"
    req = urllib.request.Request(url, headers=github_headers(), method="GET")
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = resp.read().decode("utf-8")
            try:
                parsed = json.loads(body)
            except json.JSONDecodeError:
                parsed = body
            return resp.status, parsed, dict(resp.headers)
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace"), dict(exc.headers)


def init_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS raw_signals (
            dedupe_key TEXT PRIMARY KEY,
            repo TEXT NOT NULL,
            org TEXT NOT NULL,
            event_type TEXT NOT NULL,
            entity_type TEXT NOT NULL,
            entity_key TEXT NOT NULL,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            published_at TEXT,
            first_seen_at TEXT NOT NULL,
            last_seen_at TEXT NOT NULL,
            collected_at TEXT NOT NULL,
            editorial_potential TEXT NOT NULL,
            source_family TEXT NOT NULL,
            payload_json TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS runs (
            run_id INTEGER PRIMARY KEY AUTOINCREMENT,
            started_at TEXT NOT NULL,
            finished_at TEXT NOT NULL,
            last_successful_sync TEXT NOT NULL,
            checked_repo_count INTEGER NOT NULL,
            new_raw_signals INTEGER NOT NULL,
            shortlist_count INTEGER NOT NULL,
            rate_limit_limit INTEGER,
            rate_limit_remaining INTEGER
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS watchlist (
            cluster_key TEXT PRIMARY KEY,
            topic_cluster TEXT NOT NULL,
            repository TEXT NOT NULL,
            representative_signal_json TEXT NOT NULL,
            supporting_events_json TEXT NOT NULL,
            supporting_events_count INTEGER NOT NULL,
            first_seen TEXT NOT NULL,
            latest_activity TEXT NOT NULL,
            editorial_potential TEXT NOT NULL,
            user_impact_reason TEXT,
            user_impact_confidence TEXT,
            promotion_reason TEXT,
            supporting_source_families_json TEXT NOT NULL,
            last_reassessed_at TEXT NOT NULL,
            raw_cluster_json TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS watchlist_rechecks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cluster_key TEXT NOT NULL,
            previous_status TEXT NOT NULL,
            new_status TEXT NOT NULL,
            promotion_reason TEXT,
            triggering_signal_json TEXT NOT NULL,
            supporting_source_families_json TEXT NOT NULL,
            reassessed_at TEXT NOT NULL,
            confidence TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def dedupe_key(repo: str, event_type: str, entity_key: str) -> str:
    return hashlib.sha256(f"{repo}|{event_type}|{entity_key}".encode("utf-8")).hexdigest()


def classify_editorial_potential(repo: str, event_type: str, title: str, detail: str = "") -> str:
    text = f"{repo} {event_type} {title} {detail}"
    # Default to LOW unless there is concrete evidence of user-facing impact.
    if any(p.search(text) for p in NEGATIVE_MAINTENANCE_PATTERNS):
        return "LOW"

    user_impact = any(p.search(text) for p in USER_IMPACT_PATTERNS)
    high_signal = (
        user_impact
        and (
            event_type == "release"
            or HIGH_IMPACT_KEYWORDS.search(text)
            or MEDIUM_KEYWORDS.search(text)
            or re.search(r"(launch|rollout|shipping|available|available now|coming to|landed|started rolling out)", text, re.I)
        )
    )
    if high_signal:
        return "HIGH"

    medium_signal = (
        user_impact
        and (
            MEDIUM_KEYWORDS.search(text)
            or re.search(r"(migration|compatibility|support docs?|changelog|release note|beta|feature|privacy|security|permission|install|billing|payment|battery|performance)", text, re.I)
        )
    )
    if medium_signal:
        return "MEDIUM"

    # Developer tooling, dependency refresh, CI, formatting and sample maintenance stay LOW
    # unless there is a clear user-facing reason to lift them.
    if repo.startswith("android/") and event_type in {"commit", "doc_change"}:
        if user_impact and re.search(r"(compose|camera|pixel|wear|watch|wallet|messages|play services|play store|security|privacy|permission|notification|billing)", text, re.I):
            return "MEDIUM"
        return "LOW"

    if event_type == "release" and user_impact:
        return "HIGH"

    return "LOW"


def infer_user_impact_reason(signal: Dict[str, Any]) -> Tuple[Optional[str], Optional[str]]:
    text = " ".join(
        [
            signal.get("repo", ""),
            signal.get("event_type", ""),
            signal.get("title", ""),
            signal.get("detail", ""),
            " ".join(signal.get("files", [])),
        ]
    )
    lower = text.lower()

    if any(k in lower for k in ["billing", "payment", "play billing"]):
        return (
            "TECHNICAL CHANGE: Play Billing / billing module update -> PRODUCT/SERVICE EFFECT: payment flow compatibility and store billing behavior -> USER IMPACT: users may see changed purchase flow, compatibility issues, or payment failures if not updated.",
            "HIGH",
        )
    if any(k in lower for k in ["notification", "high priority notifications", "twa"]):
        return (
            "TECHNICAL CHANGE: notification metadata / TWA behavior update -> PRODUCT/SERVICE EFFECT: web app notification delivery and priority handling changes -> USER IMPACT: users may receive more reliable or more prominent notifications from TWAs.",
            "MEDIUM",
        )
    if any(k in lower for k in ["pixel", "android", "wear os", "watch", "messages", "wallet", "play store", "play services", "find hub", "security", "privacy", "permission", "auth", "login"]):
        return (
            "TECHNICAL CHANGE: platform or app-facing Android/Google change -> PRODUCT/SERVICE EFFECT: feature, compatibility, security, or behavior change in a consumer-facing product/service -> USER IMPACT: users may notice new features, improved compatibility, security changes, or altered app behavior.",
            "MEDIUM",
        )
    return None, None


def supporting_source_families_for(cluster: Dict[str, Any]) -> List[str]:
    families = set(cluster.get("supporting_source_families", []))
    if families:
        return sorted(families)
    for event in cluster.get("supporting_events", []):
        families.add(event.get("source_family") or event.get("event_type", "unknown"))
    return sorted(families)


def upsert_watchlist(conn: sqlite3.Connection, cluster: Dict[str, Any]) -> None:
    payload = {
        "topic_cluster": cluster["topic_cluster"],
        "repository": cluster["repository"],
        "representative_signal": cluster["representative_signal"],
        "supporting_events": cluster["supporting_events"],
        "supporting_events_count": cluster["supporting_events_count"],
        "first_seen": cluster["first_seen"],
        "latest_activity": cluster["latest_activity"],
        "editorial_potential": cluster["editorial_potential"],
        "user_impact_reason": cluster.get("user_impact_reason"),
        "user_impact_confidence": cluster.get("user_impact_confidence"),
        "promotion_reason": cluster.get("promotion_reason"),
        "supporting_source_families": supporting_source_families_for(cluster),
    }
    cluster_key_value = cluster_key(cluster["representative_signal"])
    conn.execute(
        """
        INSERT INTO watchlist (
            cluster_key, topic_cluster, repository, representative_signal_json,
            supporting_events_json, supporting_events_count, first_seen, latest_activity,
            editorial_potential, user_impact_reason, user_impact_confidence,
            promotion_reason, supporting_source_families_json, last_reassessed_at, raw_cluster_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(cluster_key) DO UPDATE SET
            topic_cluster=excluded.topic_cluster,
            repository=excluded.repository,
            representative_signal_json=excluded.representative_signal_json,
            supporting_events_json=excluded.supporting_events_json,
            supporting_events_count=excluded.supporting_events_count,
            first_seen=excluded.first_seen,
            latest_activity=excluded.latest_activity,
            editorial_potential=excluded.editorial_potential,
            user_impact_reason=excluded.user_impact_reason,
            user_impact_confidence=excluded.user_impact_confidence,
            promotion_reason=excluded.promotion_reason,
            supporting_source_families_json=excluded.supporting_source_families_json,
            last_reassessed_at=excluded.last_reassessed_at,
            raw_cluster_json=excluded.raw_cluster_json
        """,
        (
            cluster_key_value,
            cluster["topic_cluster"],
            cluster["repository"],
            json.dumps(cluster["representative_signal"], ensure_ascii=False),
            json.dumps(cluster["supporting_events"], ensure_ascii=False),
            cluster["supporting_events_count"],
            cluster["first_seen"],
            cluster["latest_activity"],
            cluster["editorial_potential"],
            cluster.get("user_impact_reason"),
            cluster.get("user_impact_confidence"),
            cluster.get("promotion_reason"),
            json.dumps(payload["supporting_source_families"], ensure_ascii=False),
            iso(now_utc()),
            json.dumps(payload, ensure_ascii=False),
        ),
    )


def load_watchlist(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT cluster_key, topic_cluster, repository, representative_signal_json,
               supporting_events_json, supporting_events_count, first_seen, latest_activity,
               editorial_potential, user_impact_reason, user_impact_confidence,
               promotion_reason, supporting_source_families_json, last_reassessed_at, raw_cluster_json
        FROM watchlist
        """
    ).fetchall()
    out = []
    for row in rows:
        out.append(
            {
                "cluster_key": row[0],
                "topic_cluster": row[1],
                "repository": row[2],
                "representative_signal": json.loads(row[3]),
                "supporting_events": json.loads(row[4]),
                "supporting_events_count": row[5],
                "first_seen": row[6],
                "latest_activity": row[7],
                "editorial_potential": row[8],
                "user_impact_reason": row[9],
                "user_impact_confidence": row[10],
                "promotion_reason": row[11],
                "supporting_source_families": json.loads(row[12]),
                "last_reassessed_at": row[13],
                "raw_cluster": json.loads(row[14]),
            }
        )
    return out


def rebuild_cluster_from_watchlist_row(row: Dict[str, Any]) -> Dict[str, Any]:
    cluster = dict(row["raw_cluster"])
    cluster["representative_signal"] = row["representative_signal"]
    cluster["supporting_events"] = row["supporting_events"]
    cluster["supporting_events_count"] = row["supporting_events_count"]
    cluster["first_seen"] = row["first_seen"]
    cluster["latest_activity"] = row["latest_activity"]
    cluster["editorial_potential"] = row["editorial_potential"]
    cluster["user_impact_reason"] = row["user_impact_reason"]
    cluster["user_impact_confidence"] = row["user_impact_confidence"]
    cluster["promotion_reason"] = row["promotion_reason"]
    cluster["supporting_source_families"] = row["supporting_source_families"]
    cluster["last_reassessed_at"] = row["last_reassessed_at"]
    return cluster


def persist_watchlist_transition(
    conn: sqlite3.Connection,
    watch_row: Dict[str, Any],
    trigger: Dict[str, Any],
    previous_status: str,
    new_status: str,
    promotion_reason: str,
    confidence: str,
    supporting_source_families: Optional[List[str]] = None,
    user_impact_reason: Optional[str] = None,
    user_impact_confidence: Optional[str] = None,
) -> Dict[str, Any]:
    cluster = rebuild_cluster_from_watchlist_row(watch_row)
    cluster["editorial_potential"] = new_status
    cluster["promotion_reason"] = promotion_reason
    cluster["user_impact_confidence"] = user_impact_confidence or confidence or cluster.get("user_impact_confidence") or "LOW"
    cluster["user_impact_reason"] = user_impact_reason or cluster.get("user_impact_reason") or infer_user_impact_reason(trigger)[0] or infer_user_impact_reason(cluster["representative_signal"])[0]
    cluster["last_reassessed_at"] = iso(now_utc())
    if supporting_source_families:
        cluster["supporting_source_families"] = sorted(set(supporting_source_families))
    else:
        cluster["supporting_source_families"] = sorted(set(cluster.get("supporting_source_families", [])))
    cluster["supporting_events"] = list(cluster.get("supporting_events", []))
    cluster["supporting_events"].append(trigger)
    cluster["supporting_events_count"] = len(cluster["supporting_events"])

    upsert_watchlist(conn, cluster)
    conn.execute(
        """
        INSERT INTO watchlist_rechecks (
            cluster_key, previous_status, new_status, promotion_reason,
            triggering_signal_json, supporting_source_families_json,
            reassessed_at, confidence
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            watch_row["cluster_key"],
            previous_status,
            new_status,
            promotion_reason,
            json.dumps(trigger, ensure_ascii=False),
            json.dumps(cluster["supporting_source_families"], ensure_ascii=False),
            cluster["last_reassessed_at"],
            confidence,
        ),
    )
    conn.commit()
    return {
        "cluster_key": watch_row["cluster_key"],
        "topic_cluster": cluster["topic_cluster"],
        "repository": cluster["repository"],
        "previous_status": previous_status,
        "new_status": new_status,
        "promotion_reason": promotion_reason,
        "triggering_signal": {
            "event_type": trigger.get("event_type"),
            "entity_key": trigger.get("entity_key"),
            "title": trigger.get("title"),
            "repo": trigger.get("repo"),
        },
        "supporting_source_families": cluster["supporting_source_families"],
        "reassessed_at": cluster["last_reassessed_at"],
        "confidence": confidence,
        "user_impact_reason": cluster["user_impact_reason"],
        "user_impact_confidence": cluster["user_impact_confidence"],
    }


def re_evaluate_watchlist_with_trigger(
    conn: sqlite3.Connection,
    trigger: Dict[str, Any],
    related_repo: Optional[str] = None,
    related_topic: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Local-only re-evaluation over the watchlist. No API fetches.
    Only clusters matching the trigger repo/topic are reconsidered.
    """
    watch_rows = load_watchlist(conn)
    changed: List[Dict[str, Any]] = []
    trigger_text = " ".join(
        [
            trigger.get("repo", ""),
            trigger.get("event_type", ""),
            trigger.get("title", ""),
            trigger.get("detail", ""),
            " ".join(trigger.get("files", [])),
        ]
    ).lower()

    for row in watch_rows:
        if related_repo and row["repository"] != related_repo:
            continue
        if related_topic and related_topic.lower() not in row["topic_cluster"].lower():
            continue

        cluster = rebuild_cluster_from_watchlist_row(row)
        old_status = cluster.get("editorial_potential", "LOW")
        old_reason = cluster.get("promotion_reason")
        cluster["supporting_events"].append(trigger)
        cluster["supporting_events_count"] = len(cluster["supporting_events"])
        cluster["last_reassessed_at"] = iso(now_utc())
        cluster["supporting_source_families"] = sorted(set(cluster.get("supporting_source_families", [])) | {trigger.get("event_type", "unknown")})

        trigger_is_user = bool(
            any(
                kw in trigger_text
                for kw in [
                    "billing",
                    "payment",
                    "play billing",
                    "pixel",
                    "android",
                    "wear os",
                    "watch",
                    "wallet",
                    "messages",
                    "play store",
                    "play services",
                    "find hub",
                    "security",
                    "privacy",
                    "permission",
                    "notification",
                    "install",
                    "battery",
                    "performance",
                ]
            )
        )

        new_status = old_status
        promotion_reason = old_reason or ""
        confidence = cluster.get("user_impact_confidence") or "LOW"

        if old_status == "LOW":
            if trigger.get("event_type") in {"release", "issue"} and trigger_is_user:
                new_status = "MEDIUM"
                promotion_reason = "New relevant trigger added stronger user-facing evidence to a previously low watchlist cluster."
                confidence = "MEDIUM"
            else:
                new_status = "LOW"
        elif old_status == "MEDIUM":
            if trigger.get("event_type") == "release" and trigger_is_user:
                new_status = "HIGH"
                promotion_reason = "Trigger added a concrete release/user-impact signal to an already medium cluster."
                confidence = "HIGH"
            elif not trigger_is_user:
                new_status = "LOW"
                promotion_reason = "New trigger did not add user-facing evidence; cluster demoted to LOW."
                confidence = "LOW"

        if new_status != old_status:
            changed.append(
                persist_watchlist_transition(
                    conn,
                    row,
                    trigger,
                    old_status,
                    new_status,
                    promotion_reason,
                    confidence,
                    supporting_source_families=cluster["supporting_source_families"],
                    user_impact_reason=cluster.get("user_impact_reason") or infer_user_impact_reason(trigger)[0],
                    user_impact_confidence=confidence,
                )
            )

    conn.commit()
    return changed


def repo_org(repo: str) -> str:
    return repo.split("/", 1)[0] if "/" in repo else repo


def commit_signal(repo: str, item: Dict[str, Any], detail: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    sha = item.get("sha", "")
    commit = item.get("commit", {})
    msg = commit.get("message", "").split("\n", 1)[0]
    html_url = item.get("html_url", "")
    author_date = commit.get("author", {}).get("date")
    files = detail.get("files", []) if detail else []
    file_names = [f.get("filename", "") for f in files]
    file_text = " ".join(file_names)
    has_doc_change = bool(DOC_PATH_RE.search(file_text))
    event_type = "doc_change" if has_doc_change else "commit"
    entity_type = "commit"
    detail_note = ", ".join(file_names[:8]) if file_names else ""
    return {
        "repo": repo,
        "org": repo_org(repo),
        "event_type": event_type,
        "entity_type": entity_type,
        "entity_key": sha,
        "title": msg or sha,
        "url": html_url,
        "published_at": author_date,
        "detail": detail_note,
        "files": file_names,
    }


def release_signal(repo: str, item: Dict[str, Any]) -> Dict[str, Any]:
    tag = item.get("tag_name") or item.get("name") or item.get("id")
    title = item.get("name") or tag or "release"
    url = item.get("html_url") or f"https://github.com/{repo}/releases/tag/{urllib.parse.quote(str(tag))}"
    published_at = item.get("published_at") or item.get("created_at")
    return {
        "repo": repo,
        "org": repo_org(repo),
        "event_type": "release",
        "entity_type": "release",
        "entity_key": str(item.get("id") or tag),
        "title": title,
        "url": url,
        "published_at": published_at,
        "detail": item.get("body", "")[:500],
    }


def issue_signal(repo: str, item: Dict[str, Any]) -> Dict[str, Any]:
    title = item.get("title", "")
    number = item.get("number")
    url = item.get("html_url", "")
    published_at = item.get("created_at") or item.get("updated_at")
    labels = [lbl.get("name", "") for lbl in item.get("labels", [])]
    detail = ", ".join(labels)
    return {
        "repo": repo,
        "org": repo_org(repo),
        "event_type": "issue",
        "entity_type": "issue",
        "entity_key": str(number),
        "title": title,
        "url": url,
        "published_at": published_at,
        "detail": detail,
        "state": item.get("state"),
    }


def normalize_text(value: str) -> str:
    value = value.lower()
    value = re.sub(r"https?://\S+", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def extract_topic_from_text(*parts: str) -> str:
    text = " ".join(p for p in parts if p)
    lower = normalize_text(text)
    for pattern in (
        r"play billing",
        r"google wallet",
        r"google messages",
        r"wear os",
        r"play services",
        r"find hub",
        r"android browser helper",
        r"android browser",
        r"android compose",
        r"camera x",
        r"pixel",
        r"fold",
        r"watch",
        r"security",
        r"privacy",
        r"migration",
        r"release",
        r"changelog",
        r"docs",
        r"notification",
        r"billing",
    ):
        if pattern in lower:
            return pattern
    match = PATH_TOPIC_RE.search(lower)
    if match:
        return match.group("topic").replace("-", " ")
    words = lower.split()
    return " ".join(words[:5]) if words else "unknown"


def cluster_key(signal: Dict[str, Any]) -> str:
    repo = signal["repo"]
    title = signal.get("title", "")
    detail = signal.get("detail", "")
    files = " ".join(signal.get("files", []))
    event_type = signal["event_type"]

    # Releases and issues are own underlying change clusters by entity.
    if event_type == "release":
        return f"{repo}|release|{normalize_text(title)}"
    if event_type == "issue":
        return f"{repo}|issue|{normalize_text(title)}"

    # Commits and docs cluster around the underlying feature / migration / doc topic.
    topic = extract_topic_from_text(title, detail, files)
    if MIGRATION_RE.search(f"{title} {detail} {files}"):
        topic = f"{topic} migration"
    elif SECURITY_RE.search(f"{title} {detail} {files}"):
        topic = f"{topic} security"
    elif DOC_PATH_RE.search(f"{detail} {files}"):
        topic = f"{topic} docs"

    return f"{repo}|{event_type}|{topic}"


def topic_cluster_name(signal: Dict[str, Any]) -> str:
    repo = signal["repo"]
    topic = extract_topic_from_text(signal.get("title", ""), signal.get("detail", ""), " ".join(signal.get("files", [])))
    event_type = signal["event_type"]
    if event_type == "release":
        return f"{repo} release: {topic}"
    if event_type == "issue":
        return f"{repo} issue: {topic}"
    if event_type == "doc_change":
        return f"{repo} docs: {topic}"
    return f"{repo} {topic}"


def underlying_change_clusters(signals: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    clusters: Dict[str, Dict[str, Any]] = {}

    for signal in signals:
        key = cluster_key(signal)
        first_seen = parse_iso(signal.get("published_at")) or parse_iso(signal.get("collected_at")) or now_utc()
        latest_activity = parse_iso(signal.get("published_at")) or parse_iso(signal.get("collected_at")) or now_utc()
        if key not in clusters:
            clusters[key] = {
                "cluster_id": key,
                "topic_cluster": topic_cluster_name(signal),
                "repository": signal["repo"],
                "org": signal["org"],
                "representative_signal": signal,
                "supporting_events": [signal],
                "first_seen": first_seen,
                "latest_activity": latest_activity,
                "editorial_potential": signal.get("editorial_potential", "LOW"),
                "why_it_may_matter": signal.get("detail") or signal.get("title", ""),
                "event_types": {signal["event_type"]},
            }
            continue

        cluster = clusters[key]
        cluster["supporting_events"].append(signal)
        cluster["event_types"].add(signal["event_type"])
        sig_time = parse_iso(signal.get("published_at")) or parse_iso(signal.get("collected_at")) or now_utc()
        if sig_time < cluster["first_seen"]:
            cluster["first_seen"] = sig_time
        if sig_time > cluster["latest_activity"]:
            cluster["latest_activity"] = sig_time

        # Prefer the strongest representative signal; tie-break by recency.
        current_potential = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}.get(cluster["editorial_potential"], 1)
        new_potential = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}.get(signal.get("editorial_potential", "LOW"), 1)
        if new_potential > current_potential or (
            new_potential == current_potential
            and (signal.get("published_at") or "") > (cluster["representative_signal"].get("published_at") or "")
        ):
            cluster["representative_signal"] = signal
            cluster["editorial_potential"] = signal.get("editorial_potential", "LOW")
        if signal.get("detail"):
            cluster["why_it_may_matter"] = signal.get("detail")

    clustered = list(clusters.values())
    for c in clustered:
        c["supporting_events_count"] = len(c["supporting_events"])
        c["first_seen"] = iso(c["first_seen"]) if isinstance(c["first_seen"], datetime) else str(c["first_seen"])
        c["latest_activity"] = iso(c["latest_activity"]) if isinstance(c["latest_activity"], datetime) else str(c["latest_activity"])
        c["representative_signal"] = {
            k: v for k, v in c["representative_signal"].items() if k in {
                "repo", "org", "event_type", "entity_type", "entity_key", "title", "url", "published_at", "detail", "files", "state", "editorial_potential"
            }
        }
        c["why_it_may_matter"] = c["why_it_may_matter"][:500] if c["why_it_may_matter"] else ""
        c["source_diversity"] = len({e["event_type"] for e in c["supporting_events"]})
        user_reason, user_conf = infer_user_impact_reason(c["representative_signal"])
        c["user_impact_reason"] = user_reason
        c["user_impact_confidence"] = user_conf
    return clustered


def qualify_clusters(clusters: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    qualified = []
    for cluster in clusters:
        potential = cluster.get("editorial_potential", "LOW")
        # Only explicit HIGH/MEDIUM user-impact clusters qualify for shortlist consideration.
        if potential in {"HIGH", "MEDIUM"} and cluster.get("user_impact_reason"):
            qualified.append(cluster)
    return qualified


def diversify_clusters(clusters: List[Dict[str, Any]], limit: int = 10) -> List[Dict[str, Any]]:
    """
    Greedy diversification: prefer high-potential clusters, but avoid stacking
    too many candidates from the same repo or same broad topic family.
    """
    def family(cluster: Dict[str, Any]) -> str:
        t = cluster.get("topic_cluster", "")
        if "security" in t:
            return "security"
        if "release" in t:
            return "release"
        if "docs" in t or "migration" in t:
            return "docs_migration"
        if "issue" in t:
            return "issue"
        if "compose" in t:
            return "compose"
        if "pixel" in t:
            return "pixel"
        if "watch" in t:
            return "watch"
        if "wallet" in t or "messages" in t:
            return "google_apps"
        return "other"

    def score(cluster: Dict[str, Any]) -> Tuple[int, int, int, str]:
        potential = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}.get(cluster.get("editorial_potential", "LOW"), 1)
        support = cluster.get("supporting_events_count", 0)
        source_div = cluster.get("source_diversity", 0)
        return (potential, support, source_div, cluster.get("latest_activity", ""))

    ranked = sorted(clusters, key=score, reverse=True)
    selected: List[Dict[str, Any]] = []
    repo_counts: Dict[str, int] = {}
    family_counts: Dict[str, int] = {}

    for cluster in ranked:
        repo = cluster["repository"]
        fam = family(cluster)
        if repo_counts.get(repo, 0) >= 2:
            continue
        if family_counts.get(fam, 0) >= 2:
            continue
        selected.append(cluster)
        repo_counts[repo] = repo_counts.get(repo, 0) + 1
        family_counts[fam] = family_counts.get(fam, 0) + 1
        if len(selected) >= limit:
            break
    return selected


def test_mode_from_db() -> Dict[str, Any]:
    ensure_dirs()
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        'select repo,event_type,entity_type,entity_key,title,url,published_at,first_seen_at,last_seen_at,collected_at,editorial_potential,payload_json from raw_signals'
    ).fetchall()
    conn.close()

    signals: List[Dict[str, Any]] = []
    for row in rows:
        repo, event_type, entity_type, entity_key, title, url, published_at, first_seen, last_seen, collected, ed, payload = row
        payload_obj = json.loads(payload)
        detail = payload_obj.get("detail", "")
        files = payload_obj.get("files", [])
        signals.append(
            {
                "repo": repo,
                "org": repo.split("/")[0],
                "event_type": event_type,
                "entity_type": entity_type,
                "entity_key": entity_key,
                "title": title,
                "url": url,
                "published_at": published_at,
                "detail": detail,
                "files": files,
                "editorial_potential": classify_editorial_potential(repo, event_type, title, detail),
                "collected_at": collected,
            }
        )

    clusters = underlying_change_clusters(signals)
    qualified = qualify_clusters(clusters)
    shortlist = diversify_clusters(qualified, limit=10)
    low_watchlist = [c for c in clusters if c.get("editorial_potential") == "LOW"]

    def to_jsonable(cluster: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "topic_cluster": cluster["topic_cluster"],
            "repository": cluster["repository"],
            "representative_signal": {
                k: v for k, v in cluster["representative_signal"].items()
                if k in {"repo", "org", "event_type", "entity_type", "entity_key", "title", "url", "published_at", "detail", "editorial_potential"}
            },
            "supporting_events_count": cluster["supporting_events_count"],
            "first_seen": cluster["first_seen"],
            "latest_activity": cluster["latest_activity"],
            "editorial_potential": cluster["editorial_potential"],
            "user_impact_reason": cluster.get("user_impact_reason"),
            "user_impact_confidence": cluster.get("user_impact_confidence"),
            "why_it_may_matter": cluster["why_it_may_matter"],
            "supporting_events": [
                {
                    "event_type": e["event_type"],
                    "entity_key": e["entity_key"],
                    "title": e["title"],
                }
                for e in cluster["supporting_events"]
            ],
        }

    return {
        "raw_signals": len(signals),
        "clusters": len(clusters),
        "qualified_clusters": len(qualified),
        "top10": [to_jsonable(c) for c in shortlist],
        "low_watchlist_count": len(low_watchlist),
    }


def upsert_watchlist(conn: sqlite3.Connection, cluster: Dict[str, Any]) -> None:
    payload = {
        "topic_cluster": cluster["topic_cluster"],
        "repository": cluster["repository"],
        "representative_signal": cluster["representative_signal"],
        "supporting_events": cluster["supporting_events"],
        "supporting_events_count": cluster["supporting_events_count"],
        "first_seen": cluster["first_seen"],
        "latest_activity": cluster["latest_activity"],
        "editorial_potential": cluster["editorial_potential"],
        "user_impact_reason": cluster.get("user_impact_reason"),
        "user_impact_confidence": cluster.get("user_impact_confidence"),
        "promotion_reason": cluster.get("promotion_reason"),
        "supporting_source_families": supporting_source_families_for(cluster),
    }
    cluster_key_value = cluster_key(cluster["representative_signal"])
    conn.execute(
        """
        INSERT INTO watchlist (
            cluster_key, topic_cluster, repository, representative_signal_json,
            supporting_events_json, supporting_events_count, first_seen, latest_activity,
            editorial_potential, user_impact_reason, user_impact_confidence,
            promotion_reason, supporting_source_families_json, last_reassessed_at, raw_cluster_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(cluster_key) DO UPDATE SET
            topic_cluster=excluded.topic_cluster,
            repository=excluded.repository,
            representative_signal_json=excluded.representative_signal_json,
            supporting_events_json=excluded.supporting_events_json,
            supporting_events_count=excluded.supporting_events_count,
            first_seen=excluded.first_seen,
            latest_activity=excluded.latest_activity,
            editorial_potential=excluded.editorial_potential,
            user_impact_reason=excluded.user_impact_reason,
            user_impact_confidence=excluded.user_impact_confidence,
            promotion_reason=excluded.promotion_reason,
            supporting_source_families_json=excluded.supporting_source_families_json,
            last_reassessed_at=excluded.last_reassessed_at,
            raw_cluster_json=excluded.raw_cluster_json
        """,
        (
            cluster_key_value,
            cluster["topic_cluster"],
            cluster["repository"],
            json.dumps(cluster["representative_signal"], ensure_ascii=False),
            json.dumps(cluster["supporting_events"], ensure_ascii=False),
            cluster["supporting_events_count"],
            cluster["first_seen"],
            cluster["latest_activity"],
            cluster["editorial_potential"],
            cluster.get("user_impact_reason"),
            cluster.get("user_impact_confidence"),
            cluster.get("promotion_reason"),
            json.dumps(payload["supporting_source_families"], ensure_ascii=False),
            iso(now_utc()),
            json.dumps(payload, ensure_ascii=False),
        ),
    )


def save_signal(conn: sqlite3.Connection, signal: Dict[str, Any], collected_at: str) -> bool:
    key = dedupe_key(signal["repo"], signal["event_type"], signal["entity_key"])
    potential = classify_editorial_potential(
        signal["repo"], signal["event_type"], signal.get("title", ""), signal.get("detail", "")
    )
    payload = dict(signal)
    payload["editorial_potential"] = potential
    row = (
        key,
        signal["repo"],
        signal["org"],
        signal["event_type"],
        signal["entity_type"],
        signal["entity_key"],
        signal.get("title", ""),
        signal.get("url", ""),
        signal.get("published_at"),
        collected_at,
        collected_at,
        collected_at,
        potential,
        "github",
        json.dumps(payload, ensure_ascii=False),
    )
    cur = conn.execute(
        """
        INSERT OR IGNORE INTO raw_signals (
            dedupe_key, repo, org, event_type, entity_type, entity_key,
            title, url, published_at, first_seen_at, last_seen_at,
            collected_at, editorial_potential, source_family, payload_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        row,
    )
    if cur.rowcount:
        return True

    conn.execute(
        """
        UPDATE raw_signals
        SET last_seen_at = ?, collected_at = ?
        WHERE dedupe_key = ?
        """,
        (collected_at, collected_at, key),
    )
    return False


def shortlist_signals(signals: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    def rank(sig: Dict[str, Any]) -> Tuple[int, int, str]:
        potential = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}.get(sig.get("editorial_potential", "LOW"), 1)
        recency = sig.get("published_at") or sig.get("collected_at") or ""
        return (potential, 0, recency)

    shortlisted = [s for s in signals if s.get("editorial_potential") in {"HIGH", "MEDIUM"}]
    shortlisted.sort(key=rank, reverse=True)
    return shortlisted[:10]


def collect_commits(repo: str, since: str) -> List[Dict[str, Any]]:
    signals: List[Dict[str, Any]] = []
    status, body, _ = github_get(f"/repos/{repo}/commits", {"since": since, "per_page": 100})
    if status != 200 or not isinstance(body, list):
        return signals

    for item in body:
        sha = item.get("sha", "")
        msg = item.get("commit", {}).get("message", "").split("\n", 1)[0]
        # Pull details only for likely user-facing or docs-related commits.
        detail = None
        if HIGH_IMPACT_KEYWORDS.search(msg) or MEDIUM_KEYWORDS.search(msg) or repo.startswith("android/"):
            d_status, d_body, _ = github_get(f"/repos/{repo}/commits/{sha}")
            if d_status == 200 and isinstance(d_body, dict):
                detail = d_body
        sig = commit_signal(repo, item, detail)
        if detail:
            files = detail.get("files", [])
            sig["detail"] = ", ".join(f.get("filename", "") for f in files[:8])
            sig["files"] = [f.get("filename", "") for f in files]
        signals.append(sig)
    return signals


def collect_releases(repo: str, since: str) -> List[Dict[str, Any]]:
    signals: List[Dict[str, Any]] = []
    status, body, _ = github_get(f"/repos/{repo}/releases", {"per_page": 10})
    if status != 200 or not isinstance(body, list):
        return signals

    since_dt = parse_iso(since) or now_utc() - timedelta(days=7)
    for item in body:
        published_at = parse_iso(item.get("published_at") or item.get("created_at"))
        if published_at and published_at <= since_dt:
            continue
        signals.append(release_signal(repo, item))
    return signals


def collect_issues(repo: str, since: str) -> List[Dict[str, Any]]:
    signals: List[Dict[str, Any]] = []
    status, body, _ = github_get(f"/repos/{repo}/issues", {"state": "open", "since": since, "per_page": 100, "sort": "updated", "direction": "desc"})
    if status != 200 or not isinstance(body, list):
        return signals

    since_dt = parse_iso(since) or now_utc() - timedelta(days=7)
    for item in body:
        if "pull_request" in item:
            continue
        created = parse_iso(item.get("created_at"))
        updated = parse_iso(item.get("updated_at"))
        if created and created <= since_dt and updated and updated <= since_dt:
            continue
        signals.append(issue_signal(repo, item))
    return signals


def fetch_rate_limit() -> Tuple[Optional[int], Optional[int]]:
    status, body, _ = github_get("/rate_limit")
    if status != 200 or not isinstance(body, dict):
        return None, None
    core = body.get("resources", {}).get("core", {})
    return core.get("limit"), core.get("remaining")


def run() -> int:
    ensure_dirs()
    state = load_state()
    last_sync = state["last_successful_sync"]
    started_at = iso(now_utc())

    conn = init_db()
    all_signals: List[Dict[str, Any]] = []
    checked_repos: List[str] = []
    new_raw = 0

    repos = TRACKED_REPOS
    for repo in repos:
        checked_repos.append(repo)
        for collector in (collect_releases, collect_commits, collect_issues):
            try:
                signals = collector(repo, last_sync)
            except Exception:
                signals = []
            for signal in signals:
                signal["collected_at"] = started_at
                inserted = save_signal(conn, signal, started_at)
                signal["editorial_potential"] = classify_editorial_potential(
                    signal["repo"], signal["event_type"], signal.get("title", ""), signal.get("detail", "")
                )
                all_signals.append(signal)
                if inserted:
                    new_raw += 1

    conn.commit()

    clusters = underlying_change_clusters(all_signals)
    qualified_clusters = qualify_clusters(clusters)
    shortlist = diversify_clusters(qualified_clusters, limit=10)
    low_clusters = [c for c in clusters if c.get("editorial_potential") == "LOW"]
    rate_limit_limit, rate_limit_remaining = fetch_rate_limit()

    for cluster in low_clusters:
        cluster["promotion_reason"] = "LOW maintenance / tooling signal kept as watchlist only"
        upsert_watchlist(conn, cluster)
    for cluster in qualified_clusters:
        upsert_watchlist(conn, cluster)

    conn.execute(
        """
        INSERT INTO runs (
            started_at, finished_at, last_successful_sync, checked_repo_count,
            new_raw_signals, shortlist_count, rate_limit_limit, rate_limit_remaining
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            started_at,
            started_at,
            last_sync,
            len(checked_repos),
            new_raw,
            len(shortlist),
            rate_limit_limit,
            rate_limit_remaining,
        ),
    )
    conn.commit()
    conn.close()

    state["last_run_at"] = started_at
    state["last_successful_sync"] = started_at
    state["bootstrap"] = False
    save_state(state)

    def cluster_summary(cluster: Dict[str, Any]) -> Dict[str, Any]:
        rep = cluster["representative_signal"]
        return {
            "topic_cluster": cluster["topic_cluster"],
            "repository": cluster["repository"],
            "representative_signal": {
                "event_type": rep.get("event_type"),
                "entity_type": rep.get("entity_type"),
                "entity_key": rep.get("entity_key"),
                "title": rep.get("title"),
                "url": rep.get("url"),
                "published_at": rep.get("published_at"),
            },
            "supporting_events_count": cluster["supporting_events_count"],
            "first_seen": cluster["first_seen"],
            "latest_activity": cluster["latest_activity"],
            "editorial_potential": cluster["editorial_potential"],
            "why_it_may_matter": cluster["why_it_may_matter"],
        }

    report = {
        "checked_repo_count": len(checked_repos),
        "raw_signals": new_raw,
        "clusters": len(clusters),
        "qualified_clusters": len(qualified_clusters),
        "low_watchlist_count": len(low_clusters),
        "top10": [cluster_summary(c) for c in shortlist],
        "rate_limit_remaining": rate_limit_remaining,
        "rate_limit_limit": rate_limit_limit,
        "last_successful_sync": last_sync,
        "next_successful_sync": started_at,
    }
    save_last_report(report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(run())
    except RuntimeError as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2))
        raise SystemExit(1)

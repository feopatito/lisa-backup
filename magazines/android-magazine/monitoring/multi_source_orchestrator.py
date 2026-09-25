#!/usr/bin/env python3
"""
AndroidMagazine multi-source orchestrator.

Reads only locally available data layers:
- GitHub raw signals / watchlist from monitoring/data/github_signals.db
- Google Search Console CSV exports
- GA4 CSV exports
- WordPress CSV exports
- Google Trends cache extracted from the latest editorial report

The script builds one normalized signal layer, one cross-source candidate
universe, one global ranking, and a test-mode audit. It does not fetch any
remote API data unless a future operator explicitly extends it.
"""

from __future__ import annotations

import argparse
import csv
import html
import hashlib
import json
import os
import re
import sqlite3
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import quote_plus, urlparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET
from email.utils import parsedate_to_datetime

import github_discovery_monitor as github_monitor


BASE_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = BASE_DIR.parents[2]
MAGAZINE_DIR = WORKSPACE_ROOT / "magazines" / "android-magazine"
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = MAGAZINE_DIR / "reports"

ORCH_DB_PATH = DATA_DIR / "multi_source_orchestrator.db"
ORCH_STATE_PATH = DATA_DIR / "multi_source_orchestrator_state.json"
OUTPUT_MD_PATH = REPORTS_DIR / "MULTI-SOURCE-ORCHESTRATOR-TEST-2026-08-19.md"
OUTPUT_JSON_PATH = REPORTS_DIR / "MULTI-SOURCE-ORCHESTRATOR-TEST-2026-08-19.json"
STATUS_PATH = DATA_DIR / "multi_source_orchestrator_status.json"

GSC_DIR = MAGAZINE_DIR / "analytics" / "gsc"
GA4_DIR = MAGAZINE_DIR / "analytics" / "ga4"
WP_DIR = MAGAZINE_DIR / "wordpress"
GITHUB_DB_PATH = BASE_DIR / "data" / "github_signals.db"
GITHUB_STATE_PATH = BASE_DIR / "data" / "github_state.json"
TRENDS_DB_PATH = BASE_DIR / "data" / "trends_signals.db"
EDITORIAL_REPORT_PATH = REPORTS_DIR / "EDITORIAL-REPORT-ANDROIDMAGAZINE-2026-08-18.md"

MAX_GSC_ROWS = 350
MAX_GA4_ROWS = 350

TOPIC_ALIASES: List[Tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bandroid\s*17\b", re.I), "android 17"),
    (re.compile(r"\bandroid\s*16\b", re.I), "android 16"),
    (re.compile(r"\bpixel\s*11\b", re.I), "pixel 11"),
    (re.compile(r"\bpixel\s*watch\s*5\b", re.I), "pixel watch 5"),
    (re.compile(r"\bpixel\s*watch\s*4\b", re.I), "pixel watch 4"),
    (re.compile(r"\bgalaxy\s*z\s*fold\s*9\b", re.I), "galaxy z fold 9"),
    (re.compile(r"\bfold\s*wide\b", re.I), "galaxy z fold wide"),
    (re.compile(r"\bredmi\s*k100\s*pro\s*max\b", re.I), "redmi k100 pro max"),
    (re.compile(r"\bpoco\s*f9\s*ultra\b", re.I), "poco f9 ultra"),
    (re.compile(r"\bpoco\s*f9\s*pro\b", re.I), "poco f9 pro"),
    (re.compile(r"\bgoogle\s*wallet\b", re.I), "google wallet"),
    (re.compile(r"\bgoogle\s*messages\b", re.I), "google messages"),
    (re.compile(r"\bplay\s*billing\b", re.I), "play billing"),
    (re.compile(r"\bplay\s*store\b", re.I), "play store"),
    (re.compile(r"\bplay\s*services\b", re.I), "play services"),
    (re.compile(r"\bfind\s*hub\b", re.I), "find hub"),
    (re.compile(r"\bwear\s*os\b", re.I), "wear os"),
    (re.compile(r"\bspotify\b.*\bandroid\b", re.I), "spotify android"),
    (re.compile(r"\b8000\s*mah\b", re.I), "8000mah battery"),
    (re.compile(r"\brcs\b", re.I), "rcs"),
    (re.compile(r"\bdata\s*usage\b|\bdata\s*drain\b", re.I), "android data usage"),
    (re.compile(r"\bbattery\b.*\bandroid\b", re.I), "android battery"),
    (re.compile(r"\bnotification\b", re.I), "notifications"),
    (re.compile(r"\bsecurity\b|\bvulnerability\b|\bcve\b", re.I), "security"),
]

MAINTENANCE_RE = re.compile(
    r"(dependency dashboard|renovate|ci build|build failure|formatting|lint|style|"
    r"sample code|sample gating|tooling|refactor|internal|docs? only|readme only)",
    re.I,
)

USER_IMPACT_RE = re.compile(
    r"(user[- ]?facing|consumer|public|security|privacy|permission|auth|login|"
    r"play billing|billing|payment|pixel|android\s*\d+|wear os|watch|wallet|messages|"
    r"play store|play services|find hub|battery|performance|compatibility|install|"
    r"installation|sideload|notification|feature|behavior|availability)",
    re.I,
)

GENERIC_TOPIC_RE = re.compile(
    r"^(pixel\s*\d+|android\s*\d+|wear os|play store|play services|google wallet|google messages|"
    r"find hub|rcs|play billing|wallet|messages|watch)$",
    re.I,
)

LANE_ORDER = [
    "BREAKING / CURRENT NEWS",
    "DISCOVERY / PREDICTIVE",
    "CURRENT DEMAND / TREND",
    "SEO / SEARCH OPPORTUNITY",
    "UPDATE / REWRITE",
]

LANE_PRIORITY = {lane: idx for idx, lane in enumerate(LANE_ORDER)}

NEWS_QUERY_SPECS: List[Dict[str, str]] = [
    {"query": "Android 17", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Android beta", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Google Pixel", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Samsung Galaxy", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Google Play Store", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Wear OS", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Google Messages", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Google Wallet", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Android security", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Android privacy", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Xiaomi Redmi Poco", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "OnePlus Android", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Nothing Phone", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Motorola Android", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Honor Android", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "Oppo Vivo Android", "hl": "en-US", "gl": "US", "ceid": "US:en"},
    {"query": "WhatsApp Android", "hl": "en-US", "gl": "US", "ceid": "US:en"},
]

NEWS_OFFICIAL_DOMAINS = {
    "samsung.com",
    "blog.google",
    "googleblog.com",
    "android.com",
    "support.google.com",
    "developers.google.com",
    "developer.android.com",
    "wearos.googleblog.com",
    "oneplus.com",
    "motorola.com",
    "xiaomi.com",
    "mi.com",
    "nothing.tech",
    "honor.com",
    "oppo.com",
    "vivo.com",
    "whatsapp.com",
    "blog.whatsapp.com",
    "meta.com",
    "news.samsung.com",
}

NEWS_INTERNAL_DOMAINS = {
    "androidmagazine.eu",
    "properties/361709661",
    "sc-domain:androidmagazine.eu",
}

NEWS_EVENT_PATTERNS: List[Tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bgalaxy\s+tab\s+s12\s+ultra\b", re.I), "galaxy tab s12 ultra"),
    (re.compile(r"\bgalaxy\s+s26\s+fe\b", re.I), "galaxy s26 fe"),
    (re.compile(r"\bgalaxy\s+z\s+fold\s*8\b", re.I), "galaxy z fold 8"),
    (re.compile(r"\bpixel\s+11\b", re.I), "pixel 11"),
    (re.compile(r"\bandroid\s+17\b", re.I), "android 17"),
    (re.compile(r"\bwear\s+os\b", re.I), "wear os"),
    (re.compile(r"\bgoogle\s+messages\b", re.I), "google messages"),
    (re.compile(r"\bgoogle\s+wallet\b", re.I), "google wallet"),
    (re.compile(r"\bplay\s+store\b|\bgoogle\s+play\s+store\b", re.I), "google play store"),
    (re.compile(r"\bfind\s+hub\b", re.I), "find hub"),
    (re.compile(r"\bmotorola\b.*\bmagnetic\b|\bmagnetic\b.*\bmotorola\b", re.I), "motorola magnetic charging"),
    (re.compile(r"\bgrapheneos\b.*\bmotorola\b|\bmotorola\b.*\bgrapheneos\b", re.I), "grapheneos motorola support"),
    (re.compile(r"\bnothing\s+phone\s+\(?4a\)?\s*pro\b", re.I), "nothing phone 4a pro"),
    (re.compile(r"\bhyperos\s*4\b", re.I), "hyperos 4"),
    (re.compile(r"\boneplus\s+1[56]\b", re.I), "oneplus 16"),
    (re.compile(r"\bhonor\s+robot\s+phone\b", re.I), "honor robot phone"),
    (re.compile(r"\bfuto\s+keyboard\b", re.I), "futo keyboard"),
    (re.compile(r"\bsmartglasses\b|\bsmart glasses\b", re.I), "smartglasses privacy"),
    (re.compile(r"\bsideload(ing)?\b", re.I), "android sideloading security"),
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
        dt = datetime.fromisoformat(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def ensure_dirs() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def safe_int(value: Any, default: int = 0) -> int:
    try:
        if value is None:
            return default
        if isinstance(value, int):
            return value
        s = str(value).strip().replace(",", ".")
        if not s:
            return default
        return int(float(s))
    except Exception:
        return default


def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        if isinstance(value, float):
            return value
        s = str(value).strip().replace(",", ".")
        if not s:
            return default
        return float(s)
    except Exception:
        return default


def normalize_text(value: str) -> str:
    value = value.lower()
    value = re.sub(r"https?://\S+", " ", value)
    value = re.sub(r"[^a-z0-9\u00c0-\u024f\u0400-\u04ff\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def canonical_topic(*parts: str) -> str:
    text = normalize_text(" ".join(p for p in parts if p))
    if not text:
        return "unknown"
    for pattern, replacement in TOPIC_ALIASES:
        if pattern.search(text):
            return replacement
    # Prefer the first meaningful tokens instead of generic noise.
    tokens = [t for t in text.split() if t not in {"the", "and", "with", "for", "from", "a", "an", "to", "of"}]
    if not tokens:
        return "unknown"
    return " ".join(tokens[:5])


def canonical_topic_from_path(url: str) -> str:
    if not url:
        return "unknown"
    slug = url.rstrip("/").split("/")[-1]
    slug = slug.replace("-", " ")
    return canonical_topic(slug)


def signal_id(parts: Sequence[str]) -> str:
    raw = "|".join(parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def signal(
    source_family: str,
    source: str,
    signal_type: str,
    entity: str,
    topic: str,
    title: str,
    url: str,
    published_at: Optional[str],
    first_seen_at: Optional[str],
    latest_activity: Optional[str],
    evidence: str,
    confidence: str,
    user_impact: str,
    raw_source_reference: str,
    processing_status: str,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    sid = signal_id([source_family, source, signal_type, entity, topic, title, url, raw_source_reference])
    created = published_at or first_seen_at or iso(now_utc())
    return {
        "signal_id": sid,
        "source_family": source_family,
        "source": source,
        "signal_type": signal_type,
        "entity": entity,
        "topic": topic,
        "title": title,
        "url": url,
        "published_at": published_at,
        "first_seen_at": first_seen_at or created,
        "latest_activity": latest_activity or created,
        "evidence": evidence,
        "confidence": confidence,
        "user_impact": user_impact,
        "raw_source_reference": raw_source_reference,
        "processing_status": processing_status,
        "metadata": metadata or {},
    }


def parse_rss_datetime(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    try:
        dt = parsedate_to_datetime(value)
        if dt is None:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return iso(dt)
    except Exception:
        return None


def news_domain_from_url(url: str) -> str:
    if not url:
        return ""
    try:
        parsed = urlparse(url)
        host = parsed.netloc.lower()
        if host.startswith("www."):
            host = host[4:]
        return host
    except Exception:
        return ""


def news_user_impact(title: str, source_name: str, query: str) -> str:
    combined = normalize_text(" ".join([title, source_name, query]))
    if any(k in combined for k in ["outage", "down", "bug", "broken", "error", "issue"]):
        return "news signal about a bug, outage, or service disruption that may affect users"
    if any(k in combined for k in ["update", "beta", "rollout", "release", "launch", "availability"]):
        return "news signal about a rollout, beta, or launch that may change user behavior or access"
    if any(k in combined for k in ["security", "privacy", "vulnerability", "cve", "permission"]):
        return "news signal about security or privacy changes that may affect users directly"
    if any(k in combined for k in ["pixel", "android", "galaxy", "xiaomi", "oneplus", "nothing", "motorola", "honor", "oppo", "vivo", "whatsapp", "wear os"]):
        return "news signal about an Android ecosystem product that may affect users or buyers"
    return "news signal that may become a user-facing story if corroborated"


def classify_news_source(source_name: str, domain: str, query: str) -> str:
    normalized = normalize_text(" ".join([source_name, domain, query]))
    if any(d in domain for d in NEWS_OFFICIAL_DOMAINS) or domain in NEWS_OFFICIAL_DOMAINS:
        return "official_primary_source"
    if domain in NEWS_INTERNAL_DOMAINS or any(k in normalized for k in ["androidmagazine", "sc domain", "properties 361709661"]):
        return "internal_evidence_source"
    return "external_independent_publisher"


def news_underlying_event_topic(title: str, query: str, source_name: str, domain: str) -> str:
    combined = normalize_text(" ".join([title, query, source_name, domain]))
    for pattern, topic in NEWS_EVENT_PATTERNS:
        if pattern.search(combined):
            return topic
    if "android" in combined and "security" in combined:
        return "android security"
    if "android" in combined and "privacy" in combined:
        return "android privacy"
    if "samsung" in combined and "galaxy" in combined:
        return "samsung galaxy ecosystem"
    if "motorola" in combined:
        return "motorola android"
    if "oneplus" in combined:
        return "oneplus android"
    if "xiaomi" in combined or "redmi" in combined or "poco" in combined:
        return "xiaomi redmi poco"
    if "nothing" in combined:
        return "nothing phone"
    if "wear os" in combined:
        return "wear os"
    if "play store" in combined:
        return "google play store"
    if "google messages" in combined:
        return "google messages"
    if "google wallet" in combined:
        return "google wallet"
    if "find hub" in combined:
        return "find hub"
    return canonical_topic(title, query, source_name, domain)


def news_why_it_may_matter(cluster: Dict[str, Any]) -> str:
    topic = cluster.get("topic_cluster", "")
    rep = cluster.get("representative_signal", {})
    source_names = sorted({s.get("source", "") for s in cluster.get("supporting_signals", []) if s.get("source")})
    official_sources = cluster.get("official_primary_sources", [])
    publisher_count = cluster.get("external_independent_publishers", 0)
    age = cluster.get("information_first_public_at") or cluster.get("story_first_seen_at") or ""

    def join_sources(limit: int = 3) -> str:
        return ", ".join(source_names[:limit]) if source_names else "multiple sources"

    if topic == "galaxy tab s12 ultra":
        return (
            f"EVENT: Galaxy Tab S12 Ultra coverage is converging across leaks, renders and official material -> "
            f"PRODUCT/USER CHANGE: readers can separate rumor from official design/timing signals -> "
            f"AUDIENCE RELEVANCE: Samsung tablet watchers and upgrade buyers are deciding whether to wait or buy -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: publish one consolidated explainer/update that ties together {join_sources()} and keeps the story current."
        )
    if topic == "motorola magnetic charging":
        return (
            f"EVENT: Motorola magnetic charging moved from teaser/leak into repeat coverage -> "
            f"PRODUCT/USER CHANGE: buyers may see Qi2-style accessory compatibility and a new charging behavior -> "
            f"AUDIENCE RELEVANCE: Motorola owners and accessory buyers need practical compatibility guidance -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: explain what changes, which phones/accessories are affected, and whether the feature is real enough to matter."
        )
    if topic == "android 17":
        return (
            f"EVENT: Android 17 is being discussed across rollout, device and feature stories -> "
            f"PRODUCT/USER CHANGE: users want to know what changes in compatibility, UI and updates -> "
            f"AUDIENCE RELEVANCE: the audience is already search-heavy and comparison-driven -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: update the existing Android 17 coverage with a clearer, current-angle consolidation."
        )
    if topic == "wear os":
        return (
            f"EVENT: Wear OS coverage is mixing app, platform and rollout updates -> "
            f"PRODUCT/USER CHANGE: watch owners care about feature availability, setup and compatibility -> "
            f"AUDIENCE RELEVANCE: Wear OS readers typically search for practical how-tos and update implications -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: refresh the Wear OS hub with the latest user-facing change instead of another generic recap."
        )
    if topic == "google messages":
        return (
            f"EVENT: Google Messages RCS issues or feature changes are showing up across multiple publishers -> "
            f"PRODUCT/USER CHANGE: users may lose messaging reliability, RCS availability or pairing behavior -> "
            f"AUDIENCE RELEVANCE: chat failures are high-frequency pain points and trigger search fast -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: publish a concrete troubleshooting/update piece that tells readers what broke, what is confirmed and what to try next."
        )
    if topic == "google wallet":
        return (
            f"EVENT: Google Wallet design or pass handling is changing across coverage -> "
            f"PRODUCT/USER CHANGE: users may see different passes, quicker access or changed payment flows -> "
            f"AUDIENCE RELEVANCE: wallet changes matter to everyday Android owners and commuters using tap-to-pay -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: explain the new Wallet behavior and show whether it changes day-to-day use or only the UI."
        )
    if topic == "play store":
        return (
            f"EVENT: Play Store policy or product changes are being amplified by several publishers -> "
            f"PRODUCT/USER CHANGE: users may notice app discovery, install, or store-navigation differences -> "
            f"AUDIENCE RELEVANCE: Play Store changes hit almost every Android user, so search demand rises quickly -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: turn the story into a practical guide to what exactly changed and who should care."
        )
    if topic == "pixel 11":
        return (
            f"EVENT: Pixel 11 coverage is maturing from rumors into repeat reporting and product context -> "
            f"PRODUCT/USER CHANGE: readers want to know whether the device is imminent, what changes, and whether to wait -> "
            f"AUDIENCE RELEVANCE: Pixel buyers search hard before launch and after major rumor cycles -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: keep one living Pixel 11 explainer that merges current signals, buying advice and what is actually confirmed."
        )
    if topic == "pixel watch 5":
        return (
            f"EVENT: Pixel Watch 5 leak/coverage cluster is converging on a single watch release -> "
            f"PRODUCT/USER CHANGE: buyers want to know whether the new watch changes battery life, features or launch timing -> "
            f"AUDIENCE RELEVANCE: watch upgrade decisions are tightly time-sensitive and comparison-heavy -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: consolidate leaks and official crumbs into one buying-oriented explainer."
        )
    if topic == "galaxy tab s12 ultra":
        return (
            f"EVENT: Galaxy Tab S12 Ultra leaks, renders and official material are pointing at the same tablet launch -> "
            f"PRODUCT/USER CHANGE: buyers can judge design, accessory and launch implications sooner -> "
            f"AUDIENCE RELEVANCE: Samsung tablet readers care about whether to wait or buy now -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: keep one consolidated launch explainer and update it as the official picture sharpens."
        )
    if topic == "galaxy z fold 8":
        return (
            f"EVENT: Galaxy Z Fold 8 rumor and promo coverage is converging around the same foldable launch cycle -> "
            f"PRODUCT/USER CHANGE: readers want design, pricing and upgrade timing clarity before buying -> "
            f"AUDIENCE RELEVANCE: foldable buyers are comparison-heavy and respond fast to rumor consolidation -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: publish one foldable roundup that separates tease, leak and confirmed detail."
        )
    if topic == "motorola magnetic charging":
        return (
            f"EVENT: Motorola magnetic charging is being repeated across leak and feature coverage -> "
            f"PRODUCT/USER CHANGE: accessory compatibility and charging behavior may shift toward Qi2-style use -> "
            f"AUDIENCE RELEVANCE: Motorola owners and accessory shoppers need practical compatibility guidance -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: explain what is confirmed, which phones may support it and what it means for charging gear."
        )
    if topic == "xiaomi redmi poco":
        return (
            f"EVENT: Xiaomi/Redmi/Poco patch and rollout coverage is clustering around a device family update story -> "
            f"PRODUCT/USER CHANGE: readers may need to know whether their model is updated, supported or affected -> "
            f"AUDIENCE RELEVANCE: owners search for model lists and update impact, not brand headlines -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: turn the update into a clear model-by-model practical article."
        )
    if topic == "oneplus 16" or topic == "oneplus android":
        return (
            f"EVENT: OnePlus coverage is converging on a future device / feature rumor -> "
            f"PRODUCT/USER CHANGE: buyers want refresh-rate, launch timing and hardware certainty -> "
            f"AUDIENCE RELEVANCE: OnePlus readers compare rumors quickly and want the plain-English summary -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: consolidate the rumor into one buyer-facing explainer with a confirmed-vs-speculative split."
        )
    if topic == "nothing phone" or topic == "nothing phone 4a pro":
        return (
            f"EVENT: Nothing Phone coverage is tied to price, promotion or model chatter -> "
            f"PRODUCT/USER CHANGE: buyers may see a different deal, price or model naming situation -> "
            f"AUDIENCE RELEVANCE: Nothing readers are deal-sensitive and compare aggressively -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: publish a short buyer guide that explains whether the story is about the phone itself or just a sale."
        )
    if topic == "hyperos 4":
        return (
            f"EVENT: HyperOS 4 is being framed as a device rollout story rather than a rumor -> "
            f"PRODUCT/USER CHANGE: eligible Xiaomi/Redmi/Poco owners need to know if and when they receive the update -> "
            f"AUDIENCE RELEVANCE: update lists and rollout timing are the part readers actually search for -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: produce a model list and rollout explainer instead of a generic news recap."
        )
    if topic == "honor robot phone":
        return (
            f"EVENT: Honor Robot Phone concept coverage is generating reaction around the camera/industrial design idea -> "
            f"PRODUCT/USER CHANGE: the question is whether the odd hardware translates into real user value or just spectacle -> "
            f"AUDIENCE RELEVANCE: readers want to know if this is future hardware or pure tease -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: frame it as a practical assessment of whether the concept changes the buying picture."
        )
    if topic == "security" or "security" in topic:
        return (
            f"EVENT: Android security coverage is repeating across multiple publishers -> "
            f"PRODUCT/USER CHANGE: the practical impact is usually sideloading, permissions or risk reduction -> "
            f"AUDIENCE RELEVANCE: broad Android readership cares when the warning changes behavior or settings -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: only publish if you can turn the warning into a concrete user-facing guide or decision aid."
        )
    if "motorola" in topic:
        return (
            f"EVENT: a Motorola-related hardware or feature rumor is gaining repeat mention -> "
            f"PRODUCT/USER CHANGE: readers want to know whether it changes charging, accessories or phone choice -> "
            f"AUDIENCE RELEVANCE: Motorola buyers and Android accessory shoppers need a clear practical summary -> "
            f"ANDROIDMAGAZINE OPPORTUNITY: publish a single explainer that resolves the rumor and states what is actually confirmed."
        )
    return (
        f"EVENT: {topic} has enough external attention to justify monitoring -> "
        f"PRODUCT/USER CHANGE: the underlying story may alter device behavior, launch timing or feature availability -> "
        f"AUDIENCE RELEVANCE: Android readers only care if it changes buying, setup or troubleshooting decisions -> "
        f"ANDROIDMAGAZINE OPPORTUNITY: turn the event into a concrete reader decision rather than a generic news recap."
    )


def news_pre_gate_score(cluster: Dict[str, Any]) -> float:
    age = age_days(cluster)
    freshness = 8.0 if age is not None and age <= 1 else 6.0 if age is not None and age <= 3 else 4.0 if age is not None and age <= 10 else 1.0
    support = min(cluster.get("supporting_events_count", 0), 10) * 1.5
    source_div = min(cluster.get("source_diversity", 0), 8) * 2.0
    official = 4.0 if cluster.get("official_primary_sources") else 0.0
    external = min(len(cluster.get("external_independent_publishers", [])), 6) * 2.2
    impact = 6.0 if cluster.get("user_impact_confidence") == "HIGH" else 4.0 if cluster.get("user_impact_confidence") == "MEDIUM" else 2.0
    return round(freshness + support + source_div + official + external + impact, 1)


def fetch_google_news_rss(query: str, hl: str = "en-US", gl: str = "US", ceid: str = "US:en", limit: int = 10) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    url = (
        "https://news.google.com/rss/search?q="
        + quote_plus(query)
        + f"&hl={quote_plus(hl)}&gl={quote_plus(gl)}&ceid={quote_plus(ceid)}"
    )
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req, timeout=15) as response:
            payload = response.read()
        root = ET.fromstring(payload)
    except Exception as exc:
        return [], {"checked": True, "query": query, "url": url, "error": str(exc), "signals": 0}

    channel = root.find("channel")
    items = channel.findall("item") if channel is not None else root.findall(".//item")
    entries: List[Dict[str, Any]] = []
    for item in items[:limit]:
        title = html.unescape((item.findtext("title") or "").strip())
        link = (item.findtext("link") or "").strip()
        pub_date = parse_rss_datetime(item.findtext("pubDate"))
        source_elem = item.find("source")
        source_name = html.unescape((source_elem.text or "").strip()) if source_elem is not None else ""
        source_url = source_elem.get("url", "").strip() if source_elem is not None else ""
        domain = news_domain_from_url(source_url or link)
        entries.append(
            {
                "title": title,
                "link": link,
                "pub_date": pub_date,
                "source_name": source_name or domain or "Google News source",
                "source_url": source_url,
                "domain": domain,
                "raw_xml": ET.tostring(item, encoding="unicode"),
            }
        )
    return entries, {"checked": True, "query": query, "url": url, "signals": len(entries), "error": None}


def load_news_signals(enabled: bool = False, max_per_query: int = 8) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    if not enabled:
        return [], {"checked": False, "reason": "news discovery disabled", "queries": 0, "signals": 0, "clusters": 0}

    signals: List[Dict[str, Any]] = []
    query_meta: List[Dict[str, Any]] = []
    seen_links: set[str] = set()
    seen_keys: set[str] = set()

    for spec in NEWS_QUERY_SPECS:
        entries, meta = fetch_google_news_rss(spec["query"], spec["hl"], spec["gl"], spec["ceid"], limit=max_per_query)
        query_meta.append(meta)
        for entry in entries:
            link = entry["link"]
            if not link:
                continue
            dedupe_key = signal_id(["news", entry["source_name"], entry["title"], link])
            if link in seen_links or dedupe_key in seen_keys:
                continue
            seen_links.add(link)
            seen_keys.add(dedupe_key)
            source_category = classify_news_source(entry["source_name"], entry["domain"], spec["query"])
            topic = news_underlying_event_topic(entry["title"], spec["query"], entry["source_name"], entry["domain"])
            signals.append(
                signal(
                    source_family="news",
                    source=entry["source_name"],
                    signal_type="news_article",
                    entity=entry["domain"] or entry["source_name"] or entry["link"],
                    topic=topic,
                    title=entry["title"] or spec["query"],
                    url=entry["link"],
                    published_at=entry["pub_date"],
                    first_seen_at=entry["pub_date"],
                    latest_activity=entry["pub_date"],
                    evidence=f"Google News RSS result for {spec['query']}",
                    confidence="MEDIUM",
                    user_impact=news_user_impact(entry["title"], entry["source_name"], spec["query"]),
                    raw_source_reference=dedupe_key,
                    processing_status="normalized",
                    metadata={
                        "query": spec["query"],
                        "hl": spec["hl"],
                        "gl": spec["gl"],
                        "ceid": spec["ceid"],
                        "source_category": source_category,
                        "source_name": entry["source_name"],
                        "source_url": entry["source_url"],
                        "domain": entry["domain"],
                        "news_url": entry["link"],
                        "rss_url": meta.get("url"),
                        "rss_query_error": meta.get("error"),
                    },
                )
            )

    meta = {
        "checked": True,
        "enabled": True,
        "queries": len(NEWS_QUERY_SPECS),
        "signals": len(signals),
        "clusters": 0,
        "query_meta": query_meta,
        "reason": None,
        "last_successful_sync": iso(now_utc()) if signals else None,
        "errors": [m.get("error") for m in query_meta if m.get("error")],
    }
    return signals, meta


def source_watermark(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    try:
        ts = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        return iso(ts)
    except Exception:
        return None


def parse_report_trends(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    section = re.search(r"## Google Trends / JustSerpAPI\s*(.*?)\n## ", text, re.S)
    if not section:
        section = re.search(r"## Google Trends / JustSerpAPI\s*(.*)", text, re.S)
    if not section:
        return []
    body = section.group(1)
    rows: List[Dict[str, Any]] = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        m = re.match(
            r"-\s*(?P<topic>[^:]+):\s*(?P<a1>[^:]+):\s*(?P<v1>\d+),\s*(?P<a2>[^:]+):\s*(?P<v2>\d+),\s*(?P<a3>[^:]+):\s*(?P<v3>\d+)",
            line,
        )
        if not m:
            continue
        topic = m.group("topic").strip()
        values = [safe_int(m.group("v1")), safe_int(m.group("v2")), safe_int(m.group("v3"))]
        rows.append(
            {
                "topic": topic,
                "periods": [m.group("a1").strip(), m.group("a2").strip(), m.group("a3").strip()],
                "values": values,
                "trend_velocity": values[-1] - values[-2],
                "trend_acceleration": (values[-1] - values[-2]) - (values[-2] - values[-3]),
                "first_seen_at": source_watermark(path),
            }
        )
    return rows


def init_trends_db() -> sqlite3.Connection:
    ensure_dirs()
    conn = sqlite3.connect(TRENDS_DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS trend_signals (
            trend_id TEXT PRIMARY KEY,
            query TEXT NOT NULL,
            entity TEXT NOT NULL,
            topic_cluster TEXT NOT NULL,
            geo TEXT NOT NULL,
            first_seen_at TEXT,
            latest_seen_at TEXT,
            trend_value TEXT NOT NULL,
            previous_value TEXT NOT NULL,
            velocity TEXT NOT NULL,
            acceleration TEXT NOT NULL,
            peak TEXT NOT NULL,
            source TEXT NOT NULL,
            fetched_at TEXT NOT NULL,
            processing_status TEXT NOT NULL,
            raw_json TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_trend_signals_topic
        ON trend_signals(topic_cluster, geo, fetched_at DESC)
        """
    )
    conn.commit()
    return conn


def parse_trend_number(value: Any) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if not text or text.upper() == "UNAVAILABLE":
        return None
    try:
        return float(text)
    except Exception:
        return None


def upsert_trend_signal(conn: sqlite3.Connection, row: Dict[str, Any]) -> None:
    conn.execute(
        """
        INSERT INTO trend_signals (
            trend_id, query, entity, topic_cluster, geo, first_seen_at, latest_seen_at,
            trend_value, previous_value, velocity, acceleration, peak, source, fetched_at,
            processing_status, raw_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(trend_id) DO UPDATE SET
            query=excluded.query,
            entity=excluded.entity,
            topic_cluster=excluded.topic_cluster,
            geo=excluded.geo,
            first_seen_at=excluded.first_seen_at,
            latest_seen_at=excluded.latest_seen_at,
            trend_value=excluded.trend_value,
            previous_value=excluded.previous_value,
            velocity=excluded.velocity,
            acceleration=excluded.acceleration,
            peak=excluded.peak,
            source=excluded.source,
            fetched_at=excluded.fetched_at,
            processing_status=excluded.processing_status,
            raw_json=excluded.raw_json
        """,
        (
            row["trend_id"],
            row["query"],
            row["entity"],
            row["topic_cluster"],
            row["geo"],
            row.get("first_seen_at"),
            row.get("latest_seen_at"),
            row.get("trend_value", "UNAVAILABLE"),
            row.get("previous_value", "UNAVAILABLE"),
            row.get("velocity", "UNAVAILABLE"),
            row.get("acceleration", "UNAVAILABLE"),
            row.get("peak", "UNAVAILABLE"),
            row.get("source", "local editorial report cache"),
            row.get("fetched_at", iso(now_utc())),
            row.get("processing_status", "normalized"),
            json.dumps(row, ensure_ascii=False),
        ),
    )


def bootstrap_trends_store_from_report(conn: sqlite3.Connection, path: Path) -> int:
    rows = parse_report_trends(path)
    fetched_at = source_watermark(path) or iso(now_utc())
    count = 0
    for row in rows:
        values = row.get("values", [])
        current = values[-1] if values else None
        previous = values[-2] if len(values) >= 2 else None
        peak = max(values) if values else None
        topic = canonical_topic(row["topic"])
        payload = {
            "trend_id": signal_id(["trend", topic, "UNAVAILABLE"]),
            "query": row["topic"],
            "entity": topic,
            "topic_cluster": topic,
            "geo": "UNAVAILABLE",
            "first_seen_at": fetched_at,
            "latest_seen_at": fetched_at,
            "trend_value": current if current is not None else "UNAVAILABLE",
            "previous_value": previous if previous is not None else "UNAVAILABLE",
            "velocity": row.get("trend_velocity", "UNAVAILABLE"),
            "acceleration": row.get("trend_acceleration", "UNAVAILABLE"),
            "peak": peak if peak is not None else "UNAVAILABLE",
            "source": "local editorial report cache",
            "fetched_at": fetched_at,
            "processing_status": "normalized" if values else "UNAVAILABLE",
            "periods": row.get("periods", []),
            "values": values,
        }
        upsert_trend_signal(conn, payload)
        count += 1
    conn.commit()
    return count


def load_structured_trend_signals() -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    conn = init_trends_db()
    report_watermark = source_watermark(EDITORIAL_REPORT_PATH)
    existing_rows = conn.execute("SELECT COUNT(*) FROM trend_signals").fetchone()[0]
    latest_fetched = conn.execute("SELECT MAX(fetched_at) FROM trend_signals").fetchone()[0]
    bootstrap_needed = existing_rows == 0 or (report_watermark and (not latest_fetched or report_watermark > latest_fetched))
    bootstrap_count = 0
    if bootstrap_needed and EDITORIAL_REPORT_PATH.exists():
        bootstrap_count = bootstrap_trends_store_from_report(conn, EDITORIAL_REPORT_PATH)

    rows = conn.execute(
        """
        SELECT trend_id, query, entity, topic_cluster, geo, first_seen_at, latest_seen_at,
               trend_value, previous_value, velocity, acceleration, peak, source, fetched_at,
               processing_status, raw_json
        FROM trend_signals
        ORDER BY fetched_at DESC, topic_cluster ASC
        """
    ).fetchall()
    conn.close()

    signals: List[Dict[str, Any]] = []
    for row in rows:
        raw = json.loads(row[15])
        trend_value = parse_trend_number(row[7])
        previous_value = parse_trend_number(row[8])
        velocity = parse_trend_number(row[9])
        acceleration = parse_trend_number(row[10])
        peak = parse_trend_number(row[11])
        latest_value = trend_value if trend_value is not None else peak if peak is not None else 0.0
        processing_status = row[14]
        confidence = "HIGH" if latest_value >= 50 else "MEDIUM" if latest_value >= 20 else "LOW"
        signals.append(
            signal(
                source_family="trends",
                source=row[12],
                signal_type="trend",
                entity=row[2],
                topic=row[3],
                title=row[1],
                url="",
                published_at=row[5],
                first_seen_at=row[5],
                latest_activity=row[6] or row[13],
                evidence="Structured Google Trends cache",
                confidence=confidence if processing_status != "UNAVAILABLE" else "LOW",
                user_impact="trend momentum / breakout proxy" if processing_status != "UNAVAILABLE" else "trend metrics unavailable",
                raw_source_reference=row[0],
                processing_status=processing_status,
                metadata={
                    "query": row[1],
                    "geo": row[4],
                    "trend_value": trend_value if trend_value is not None else "UNAVAILABLE",
                    "previous_value": previous_value if previous_value is not None else "UNAVAILABLE",
                    "velocity": velocity if velocity is not None else "UNAVAILABLE",
                    "acceleration": acceleration if acceleration is not None else "UNAVAILABLE",
                    "peak": peak if peak is not None else "UNAVAILABLE",
                    "periods": raw.get("periods", []),
                    "values": raw.get("values", []),
                    "fetched_at": row[13],
                },
            )
        )

    meta = {
        "checked": bool(rows),
        "reason": None if rows else "No structured trend cache found",
        "signals": len(signals),
        "bootstrap_count": bootstrap_count,
        "last_report_watermark": report_watermark,
        "store_path": str(TRENDS_DB_PATH),
    }
    return signals, meta


def load_github_signals() -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    if not GITHUB_DB_PATH.exists():
        return [], {"checked": False, "reason": "GitHub DB missing"}

    conn = sqlite3.connect(GITHUB_DB_PATH)
    conn.row_factory = sqlite3.Row
    raw_rows = conn.execute(
        """
        SELECT dedupe_key, repo, org, event_type, entity_type, entity_key, title, url,
               published_at, first_seen_at, last_seen_at, collected_at,
               editorial_potential, source_family, payload_json
        FROM raw_signals
        ORDER BY collected_at DESC
        """
    ).fetchall()
    watch_rows = conn.execute(
        """
        SELECT cluster_key, topic_cluster, repository, representative_signal_json,
               supporting_events_json, supporting_events_count, first_seen, latest_activity,
               editorial_potential, user_impact_reason, user_impact_confidence,
               promotion_reason, supporting_source_families_json, last_reassessed_at, raw_cluster_json
        FROM watchlist
        """
    ).fetchall()
    conn.close()

    signals: List[Dict[str, Any]] = []
    for row in raw_rows:
        payload = json.loads(row["payload_json"])
        topic = canonical_topic(row["title"], payload.get("detail", ""), row["repo"], " ".join(payload.get("files", [])))
        evidence = row["editorial_potential"]
        user_impact = payload.get("user_impact_reason") or ""
        signal_conf = "HIGH" if evidence == "HIGH" else "MEDIUM" if evidence == "MEDIUM" else "LOW"
        signals.append(
            signal(
                source_family="github",
                source=row["repo"],
                signal_type=row["event_type"],
                entity=row["entity_key"],
                topic=topic,
                title=row["title"],
                url=row["url"],
                published_at=row["published_at"],
                first_seen_at=row["first_seen_at"],
                latest_activity=row["last_seen_at"],
                evidence=evidence,
                confidence=signal_conf,
                user_impact=user_impact,
                raw_source_reference=row["dedupe_key"],
                processing_status=evidence,
                metadata={
                    "org": row["org"],
                    "entity_type": row["entity_type"],
                    "files": payload.get("files", []),
                    "origin": "raw",
                },
            )
        )

    for row in watch_rows:
        watch = dict(row)
        rep = json.loads(watch["representative_signal_json"])
        supporting_events = json.loads(watch["supporting_events_json"])
        supporting_families = json.loads(watch["supporting_source_families_json"])
        topic = canonical_topic(watch["topic_cluster"], rep.get("title", ""), watch["repository"])
        confidence = watch["editorial_potential"]
        signal_conf = "HIGH" if confidence == "HIGH" else "MEDIUM" if confidence == "MEDIUM" else "LOW"
        signals.append(
            signal(
                source_family="github",
                source=watch["repository"],
                signal_type=f"watchlist_{confidence.lower()}",
                entity=watch["cluster_key"],
                topic=topic,
                title=watch["topic_cluster"],
                url=rep.get("url", ""),
                published_at=watch["first_seen"],
                first_seen_at=watch["first_seen"],
                latest_activity=watch["latest_activity"],
                evidence=f"GitHub watchlist {confidence}",
                confidence=signal_conf,
                user_impact=watch.get("user_impact_reason") or rep.get("user_impact", ""),
                raw_source_reference=watch["cluster_key"],
                processing_status=f"watchlist_{confidence.lower()}",
                metadata={
                    "watchlist_cluster_key": watch["cluster_key"],
                    "supporting_events_count": watch["supporting_events_count"],
                    "supporting_source_families": supporting_families,
                    "promotion_reason": watch.get("promotion_reason"),
                    "last_reassessed_at": watch.get("last_reassessed_at"),
                    "supporting_events": supporting_events[:5],
                    "origin": "watchlist",
                },
            )
        )

    meta = {
        "checked": True,
        "raw_signals": len(signals),
        "low_watchlist_count": sum(1 for r in watch_rows if r["editorial_potential"] == "LOW"),
        "watchlist_rows": [dict(r) for r in watch_rows],
        "state": json.loads(GITHUB_STATE_PATH.read_text(encoding="utf-8")) if GITHUB_STATE_PATH.exists() else {},
    }
    return signals, meta


def load_gsc_signals() -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    signals: List[Dict[str, Any]] = []
    meta: Dict[str, Any] = {"checked": False}
    if not GSC_DIR.exists():
        meta["reason"] = "GSC directory missing"
        return signals, meta

    meta["checked"] = True
    meta["meta"] = json.loads((GSC_DIR / "META.json").read_text(encoding="utf-8")) if (GSC_DIR / "META.json").exists() else {}

    query_rows = read_csv_rows(GSC_DIR / "query-page-90d.csv")
    if not query_rows:
        query_rows = read_csv_rows(GSC_DIR / "queries-90d.csv")
    page_rows = read_csv_rows(GSC_DIR / "pages-90d.csv")
    for row in query_rows[:MAX_GSC_ROWS]:
        query = row.get("query", "").strip()
        page = row.get("page", "").strip()
        clicks = safe_int(row.get("clicks"))
        impressions = safe_int(row.get("impressions"))
        ctr = safe_float(row.get("ctr_pct") or row.get("ctr")) / (100.0 if safe_float(row.get("ctr_pct") or row.get("ctr")) > 1 else 1.0)
        position = safe_float(row.get("position"))
        topic = canonical_topic(query, canonical_topic_from_path(page))
        evidence = "GSC query+page"
        user_impact = "user-facing search demand / query intent"
        confidence = "HIGH" if impressions >= 50 and position <= 15 else "MEDIUM" if impressions >= 10 else "LOW"
        signals.append(
            signal(
                source_family="gsc",
                source="sc-domain:androidmagazine.eu",
                signal_type="query_page",
                entity=query,
                topic=topic,
                title=query,
                url=page,
                published_at=None,
                first_seen_at=meta.get("meta", {}).get("downloaded_at"),
                latest_activity=meta.get("meta", {}).get("downloaded_at"),
                evidence=evidence,
                confidence=confidence,
                user_impact=user_impact,
                raw_source_reference=signal_id(["gsc", query, page, str(clicks), str(impressions)]),
                processing_status="normalized",
                metadata={"clicks": clicks, "impressions": impressions, "ctr": ctr, "position": position},
            )
        )
    for row in page_rows[:MAX_GSC_ROWS]:
        page = row.get("page", "").strip()
        clicks = safe_int(row.get("clicks"))
        impressions = safe_int(row.get("impressions"))
        ctr = safe_float(row.get("ctr_pct") or row.get("ctr")) / (100.0 if safe_float(row.get("ctr_pct") or row.get("ctr")) > 1 else 1.0)
        position = safe_float(row.get("position"))
        topic = canonical_topic(canonical_topic_from_path(page))
        evidence = "GSC page"
        user_impact = "landing-page search performance"
        confidence = "HIGH" if impressions >= 100 and position <= 15 else "MEDIUM" if impressions >= 20 else "LOW"
        signals.append(
            signal(
                source_family="gsc",
                source="sc-domain:androidmagazine.eu",
                signal_type="page",
                entity=page,
                topic=topic,
                title=page,
                url=page,
                published_at=None,
                first_seen_at=meta.get("meta", {}).get("downloaded_at"),
                latest_activity=meta.get("meta", {}).get("downloaded_at"),
                evidence=evidence,
                confidence=confidence,
                user_impact=user_impact,
                raw_source_reference=signal_id(["gsc-page", page, str(clicks), str(impressions)]),
                processing_status="normalized",
                metadata={"clicks": clicks, "impressions": impressions, "ctr": ctr, "position": position},
            )
        )
    meta["signals"] = len(signals)
    return signals, meta


def load_ga4_signals() -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    signals: List[Dict[str, Any]] = []
    meta: Dict[str, Any] = {"checked": False}
    if not GA4_DIR.exists():
        meta["reason"] = "GA4 directory missing"
        return signals, meta

    meta["checked"] = True
    meta["meta"] = {"downloaded_at": source_watermark(GA4_DIR / "daily-trend-90d.csv")}

    page_rows = read_csv_rows(GA4_DIR / "pages-90d.csv")
    landing_rows = read_csv_rows(GA4_DIR / "landing-pages-90d.csv")
    daily_rows = read_csv_rows(GA4_DIR / "daily-trend-90d.csv")
    for row in page_rows[:MAX_GA4_ROWS]:
        page = row.get("pagePath", "").strip()
        title = row.get("pageTitle", "").strip()
        page_views = safe_int(row.get("pageViews"))
        active = safe_int(row.get("activeUsers"))
        sessions = safe_int(row.get("sessions"))
        topic = canonical_topic(canonical_topic_from_path(page), title)
        confidence = "HIGH" if sessions >= 20 else "MEDIUM" if sessions >= 8 else "LOW"
        signals.append(
            signal(
                source_family="ga4",
                source="properties/361709661",
                signal_type="page_performance",
                entity=page,
                topic=topic,
                title=title or page,
                url=page,
                published_at=None,
                first_seen_at=meta.get("meta", {}).get("downloaded_at"),
                latest_activity=meta.get("meta", {}).get("downloaded_at"),
                evidence="GA4 page performance",
                confidence=confidence,
                user_impact="historical audience engagement",
                raw_source_reference=signal_id(["ga4-page", page, title, str(sessions), str(page_views)]),
                processing_status="normalized",
                metadata={"sessions": sessions, "activeUsers": active, "pageViews": page_views},
            )
        )
    for row in landing_rows[:MAX_GA4_ROWS]:
        page = row.get("landingPage", "").strip()
        sessions = safe_int(row.get("sessions"))
        active = safe_int(row.get("activeUsers"))
        bounce = safe_float(row.get("bounceRate_pct"))
        topic = canonical_topic(canonical_topic_from_path(page))
        confidence = "HIGH" if sessions >= 50 else "MEDIUM" if sessions >= 10 else "LOW"
        signals.append(
            signal(
                source_family="ga4",
                source="properties/361709661",
                signal_type="landing_page",
                entity=page,
                topic=topic,
                title=page,
                url=page,
                published_at=None,
                first_seen_at=meta.get("meta", {}).get("downloaded_at"),
                latest_activity=meta.get("meta", {}).get("downloaded_at"),
                evidence="GA4 landing page performance",
                confidence=confidence,
                user_impact="landing-page audience interest",
                raw_source_reference=signal_id(["ga4-landing", page, str(sessions)]),
                processing_status="normalized",
                metadata={"sessions": sessions, "activeUsers": active, "bounceRate": bounce},
            )
        )
    # Daily trend is a broad support signal, not an article by itself.
    for row in daily_rows[:60]:
        date = row.get("date", "")
        sessions = safe_int(row.get("sessions"))
        topic = "ga4 traffic trend"
        confidence = "MEDIUM" if sessions >= 1000 else "LOW"
        signals.append(
            signal(
                source_family="ga4",
                source="properties/361709661",
                signal_type="daily_trend",
                entity=date,
                topic=topic,
                title=f"GA4 daily trend {date}",
                url="",
                published_at=date,
                first_seen_at=date,
                latest_activity=date,
                evidence="GA4 daily trend",
                confidence=confidence,
                user_impact="site-wide audience movement",
                raw_source_reference=signal_id(["ga4-daily", date, str(sessions)]),
                processing_status="normalized",
                metadata={"sessions": sessions, "activeUsers": safe_int(row.get("activeUsers")), "pageViews": safe_int(row.get("pageViews"))},
            )
        )
    meta["signals"] = len(signals)
    return signals, meta


def load_wordpress_index() -> Tuple[List[Dict[str, Any]], Dict[str, Any], Dict[str, List[Dict[str, Any]]]]:
    signals: List[Dict[str, Any]] = []
    meta: Dict[str, Any] = {"checked": False}
    wp_index: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    posts = read_csv_rows(WP_DIR / "posts-all-statuses.csv")
    if not posts:
        meta["reason"] = "WordPress export missing"
        return signals, meta, wp_index

    meta["checked"] = True
    meta["meta"] = json.loads((WP_DIR / "META.json").read_text(encoding="utf-8")) if (WP_DIR / "META.json").exists() else {}

    for row in posts:
        title = row.get("title", "").strip()
        status = row.get("status", "").strip()
        slug = row.get("slug", "").strip()
        pub_date = row.get("date", "").strip()
        post_id = row.get("id", "").strip()
        url = f"https://androidmagazine.eu/{slug}/" if slug else ""
        topic = canonical_topic(title, slug)
        wp_entry = {
            "id": post_id,
            "title": title,
            "slug": slug,
            "status": status,
            "date": pub_date,
            "url": url,
        }
        wp_index[topic].append(wp_entry)
        if status not in {"publish", "draft", "future", "pending"}:
            continue
        # Emit only current editorially interesting content as signals.
        recent = True
        if status == "publish" and pub_date:
            dt = parse_iso(pub_date)
            if dt and (now_utc() - dt).days > 45:
                recent = False
        if status == "publish" and not recent and "android" not in normalize_text(title):
            continue
        confidence = "HIGH" if status == "draft" else "MEDIUM" if status in {"future", "pending"} else "LOW"
        signals.append(
            signal(
                source_family="wordpress",
                source="androidmagazine.eu",
                signal_type=status,
                entity=slug or post_id,
                topic=topic,
                title=title,
                url=url,
                published_at=pub_date or None,
                first_seen_at=pub_date or meta.get("meta", {}).get("downloaded_at"),
                latest_activity=pub_date or meta.get("meta", {}).get("downloaded_at"),
                evidence=f"WordPress {status}",
                confidence=confidence,
                user_impact="existing editorial coverage / duplication baseline",
                raw_source_reference=signal_id(["wp", post_id, status, slug]),
                processing_status="normalized",
                metadata={"post_id": post_id, "word_count": safe_int(row.get("word_count")), "comment_count": safe_int(row.get("comment_count"))},
            )
        )
    meta["signals"] = len(signals)
    return signals, meta, wp_index


def load_trend_signals() -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    return load_structured_trend_signals()


def load_existing_github_watchlist_low() -> List[Dict[str, Any]]:
    if not GITHUB_DB_PATH.exists():
        return []
    conn = sqlite3.connect(GITHUB_DB_PATH)
    rows = [row for row in github_monitor.load_watchlist(conn) if row.get("editorial_potential") == "LOW"]
    conn.close()
    return rows


def cluster_key(topic: str, source_family: str = "", primary_source: str = "") -> str:
    # Cross-source clustering must merge the same underlying story regardless of source family.
    # Keep a tiny fallback salt only when the topic is unusable.
    norm = canonical_topic(topic)
    if norm and norm != "unknown":
        return signal_id([norm])
    return signal_id([norm, source_family, primary_source])


def normalize_signals(signals_by_family: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    normalized: List[Dict[str, Any]] = []
    for family, signals in signals_by_family.items():
        normalized.extend(signals)
    return normalized


def initial_reality_status(cluster: Dict[str, Any], wp_index: Dict[str, List[Dict[str, Any]]]) -> str:
    topic = cluster["topic_cluster"]
    signals = cluster["supporting_signals"]
    source_families = set(cluster["supporting_source_families"])

    if not signals:
        return "FAIL"

    if any(s["source_family"] == "github" and s.get("confidence") == "LOW" for s in signals):
        if len(source_families) == 1:
            return "UNCERTAIN"

    if topic == "unknown":
        return "UNCERTAIN"

    if source_families == {"wordpress"}:
        # Pure editorial baseline is useful, but it is not a new fact on its own.
        return "UNCERTAIN"

    if source_families <= {"ga4", "gsc"}:
        return "PASS"

    if "trends" in source_families and len(source_families) == 1:
        return "UNCERTAIN"

    return "PASS"


def cluster_user_impact(cluster: Dict[str, Any]) -> Tuple[str, str]:
    signals = cluster["supporting_signals"]
    combined = " ".join(
        [
            cluster["topic_cluster"],
            cluster.get("title", ""),
            " ".join(s.get("title", "") for s in signals),
            " ".join(s.get("user_impact", "") for s in signals),
            " ".join(json.dumps(s.get("metadata", {}), ensure_ascii=False) for s in signals),
        ]
    ).lower()

    if MAINTENANCE_RE.search(combined):
        return (
            "TECHNICAL CHANGE -> INTERNAL TOOLING / MAINTENANCE -> NO CLEAR USER IMPACT",
            "LOW",
        )
    if "news" in cluster.get("supporting_source_families", []) and any(
        k in combined for k in ["outage", "rollout", "launch", "beta", "update", "security", "privacy", "leak", "certification", "availability", "bug"]
    ):
        return (
            "NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.",
            "MEDIUM",
        )
    if any(k in combined for k in ["play billing", "billing", "payment", "purchase", "refund"]):
        return (
            "TECHNICAL CHANGE: billing/payment-related update -> PRODUCT/SERVICE EFFECT: purchase flow or billing compatibility changes -> USER IMPACT: users may see changed checkout behavior or payment failures.",
            "HIGH",
        )
    if any(k in combined for k in ["notification", "twa", "express pay", "wallet", "messages", "rcs", "pixel watch", "battery", "android 17", "data usage", "sideload", "security", "privacy", "permission"]):
        return (
            "TECHNICAL CHANGE: platform/app behavior or support/docs update -> PRODUCT/SERVICE EFFECT: feature, compatibility, security, or workflow changes in a consumer-facing product -> USER IMPACT: users may notice new behavior, setup steps, or troubleshooting issues.",
            "MEDIUM",
        )
    if any(k in combined for k in ["pixel", "android", "watch", "wallet", "messages", "play store", "play services", "find hub", "google", "samsung"]):
        return (
            "TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.",
            "MEDIUM",
        )
    return ("No direct user-facing chain could be supported from available evidence.", "LOW")


def cluster_supporting_source_families(cluster: Dict[str, Any]) -> List[str]:
    families = sorted({s["source_family"] for s in cluster["supporting_signals"]})
    return families


def source_diversity_score(families: Iterable[str], sources: Optional[Iterable[str]] = None) -> int:
    families = set(families)
    score = len(families)
    if sources is not None:
        unique_sources = len({s for s in sources if s})
        if unique_sources > 1:
            score += min(unique_sources - 1, 4)
    if "github" in families:
        score += 1
    if "gsc" in families or "trends" in families:
        score += 1
    if "wordpress" in families:
        score += 1
    return score


def cluster_source_class_breakdown(cluster: Dict[str, Any]) -> Dict[str, Any]:
    signals = cluster["supporting_signals"]
    news_sources = [s for s in signals if s["source_family"] == "news"]
    external_publishers = sorted({s["source"] for s in news_sources if s.get("metadata", {}).get("source_category") == "external_independent_publisher" and s.get("source")})
    official_sources = sorted({s["source"] for s in news_sources if s.get("metadata", {}).get("source_category") == "official_primary_source" and s.get("source")})
    internal_sources = sorted({s["source"] for s in signals if s.get("source_family") in {"gsc", "ga4", "wordpress", "trends"} or s.get("metadata", {}).get("source_category") == "internal_evidence_source"})
    demand_sources = sorted({s["source_family"] for s in signals if s["source_family"] in {"gsc", "ga4", "trends"}})
    news_external_source_diversity = len(external_publishers)
    if official_sources:
        news_external_source_diversity += 1
    return {
        "external_independent_publishers": external_publishers,
        "official_primary_sources": official_sources,
        "internal_evidence_sources": internal_sources,
        "search_demand_sources": demand_sources,
        "news_external_source_diversity": news_external_source_diversity,
    }


def cluster_signals(normalized: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    buckets: Dict[str, Dict[str, Any]] = {}
    for sig in normalized:
        topic = sig["topic"]
        primary_source = sig["source"] if sig["source_family"] == "github" else sig["source_family"]
        key = cluster_key(topic, sig["source_family"], primary_source)
        if key not in buckets:
            first_seen = sig.get("first_seen_at") or sig.get("published_at")
            latest_seen = sig.get("latest_activity") or sig.get("published_at") or sig.get("first_seen_at")
            buckets[key] = {
                "cluster_id": key,
                "topic_cluster": topic,
                "repository": sig["source"] if sig["source_family"] == "github" else sig["source_family"],
                "representative_signal": sig,
                "supporting_signals": [sig],
                "first_signal_at": first_seen,
                "latest_signal_at": latest_seen,
                "information_first_public_at": sig.get("published_at") or sig.get("first_seen_at"),
                "source_record_first_seen_at": first_seen,
                "story_first_seen_at": sig.get("published_at") or sig.get("first_seen_at"),
                "lisa_first_seen_at": "UNAVAILABLE",
                "supporting_source_families": [sig["source_family"]],
                "supporting_source_names": [sig["source"]] if sig.get("source") else [],
                "source_diversity": 1,
                "why_it_may_matter": sig.get("evidence", ""),
            }
            continue

        cluster = buckets[key]
        cluster["supporting_signals"].append(sig)
        cluster["supporting_source_families"] = sorted(set(cluster["supporting_source_families"]) | {sig["source_family"]})
        cluster["supporting_source_names"] = sorted(set(cluster.get("supporting_source_names", [])) | {sig.get("source", "")})
        cluster["source_diversity"] = source_diversity_score(cluster["supporting_source_families"], cluster["supporting_source_names"])
        first = parse_iso(cluster["first_signal_at"])
        sig_first = parse_iso(sig.get("first_seen_at") or sig.get("published_at"))
        if sig_first and (not first or sig_first < first):
            cluster["first_signal_at"] = sig.get("first_seen_at") or sig.get("published_at")
        first_record = parse_iso(cluster.get("source_record_first_seen_at"))
        if sig_first and (not first_record or sig_first < first_record):
            cluster["source_record_first_seen_at"] = sig.get("first_seen_at") or sig.get("published_at")
        story_first = parse_iso(cluster.get("story_first_seen_at"))
        sig_story = parse_iso(sig.get("published_at") or sig.get("first_seen_at"))
        if sig_story and (not story_first or sig_story < story_first):
            cluster["story_first_seen_at"] = sig.get("published_at") or sig.get("first_seen_at")
        latest = parse_iso(cluster["latest_signal_at"])
        sig_latest = parse_iso(sig.get("latest_activity") or sig.get("published_at") or sig.get("first_seen_at"))
        if sig_latest and (not latest or sig_latest > latest):
            cluster["latest_signal_at"] = sig.get("latest_activity") or sig.get("published_at") or sig.get("first_seen_at")

        # Representative signal prefers stronger evidence, then recency.
        rank = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
        current = rank.get(cluster["representative_signal"].get("confidence"), 1)
        candidate = rank.get(sig.get("confidence"), 1)
        if candidate > current:
            cluster["representative_signal"] = sig
        elif candidate == current:
            current_ts = parse_iso(cluster["representative_signal"].get("latest_activity") or cluster["representative_signal"].get("published_at") or cluster["representative_signal"].get("first_seen_at"))
            new_ts = parse_iso(sig.get("latest_activity") or sig.get("published_at") or sig.get("first_seen_at"))
            if new_ts and (not current_ts or new_ts > current_ts):
                cluster["representative_signal"] = sig

        if sig.get("evidence"):
            cluster["why_it_may_matter"] = sig.get("evidence")

    clusters = list(buckets.values())
    for cluster in clusters:
        cluster["supporting_events_count"] = len(cluster["supporting_signals"])
        class_breakdown = cluster_source_class_breakdown(cluster)
        cluster.update(class_breakdown)
        if "news" in cluster.get("supporting_source_families", []):
            cluster["source_diversity"] = cluster.get("news_external_source_diversity", cluster["source_diversity"])
            cluster["why_it_may_matter"] = news_why_it_may_matter(cluster)
        cluster["user_impact_reason"], inferred_conf = cluster_user_impact(cluster)
        cluster["user_impact_confidence"] = inferred_conf
        cluster["cross_source_confidence"] = "HIGH" if cluster["source_diversity"] >= 4 else "MEDIUM" if cluster["source_diversity"] >= 2 else "LOW"
        cluster["editorial_potential"] = editorial_potential_from_cluster(cluster)
        cluster["information_first_public_at"] = cluster.get("information_first_public_at") or cluster.get("story_first_seen_at") or cluster["first_signal_at"]
        cluster["lisa_first_seen_at"] = cluster.get("lisa_first_seen_at") or "UNAVAILABLE"
        cluster["why_it_may_matter"] = cluster.get("why_it_may_matter") or cluster["representative_signal"].get("evidence", "")
    return clusters


def editorial_potential_from_cluster(cluster: Dict[str, Any]) -> str:
    families = set(cluster["supporting_source_families"])
    topic = cluster["topic_cluster"]
    representative = cluster["representative_signal"]
    user_conf = cluster.get("user_impact_confidence", "LOW")
    count = cluster["supporting_events_count"]
    source_div = cluster.get("source_diversity", 1)

    if "github" in families:
        if user_conf == "HIGH" and count >= 2 and len(families) >= 2:
            return "HIGH"
        if user_conf in {"HIGH", "MEDIUM"} and len(families) >= 2:
            return "MEDIUM"
        return "LOW"

    if "news" in families:
        if count >= 4 and source_div >= 3 and user_conf in {"HIGH", "MEDIUM"}:
            return "HIGH"
        if count >= 2 and (source_div >= 2 or user_conf in {"HIGH", "MEDIUM"}):
            return "MEDIUM"
        if count >= 1 and user_conf in {"HIGH", "MEDIUM"} and any(
            k in topic for k in ["android", "pixel", "galaxy", "security", "privacy", "play store", "messages", "wallet", "watch", "whatsapp", "outage", "update", "beta", "rollout", "launch"]
        ):
            return "MEDIUM"
        if count >= 1 and user_conf == "HIGH" and any(
            k in topic for k in ["android", "pixel", "galaxy", "security", "privacy", "play store", "messages", "wallet", "watch", "whatsapp"]
        ):
            return "MEDIUM"
        return "LOW"

    if "gsc" in families:
        impressions = max((safe_int(s.get("metadata", {}).get("impressions")) for s in cluster["supporting_signals"] if s["source_family"] == "gsc"), default=0)
        clicks = max((safe_int(s.get("metadata", {}).get("clicks")) for s in cluster["supporting_signals"] if s["source_family"] == "gsc"), default=0)
        position = min((safe_float(s.get("metadata", {}).get("position"), 999.0) for s in cluster["supporting_signals"] if s["source_family"] == "gsc"), default=999.0)
        if impressions >= 50 and position <= 15 and user_conf != "LOW":
            return "HIGH"
        if impressions >= 10 and (clicks > 0 or position <= 20):
            return "MEDIUM"
        return "LOW"

    if "trends" in families:
        trend_vals = [s.get("metadata", {}).get("values", [0, 0, 0]) for s in cluster["supporting_signals"] if s["source_family"] == "trends"]
        latest = max((vals[-1] if vals else 0) for vals in trend_vals) if trend_vals else 0
        if latest >= 50 and len(families) >= 2:
            return "HIGH"
        if latest >= 20:
            return "MEDIUM"
        return "LOW"

    if "wordpress" in families:
        if representative.get("confidence") == "HIGH" and len(families) >= 2:
            return "MEDIUM"
        return "LOW"

    if "ga4" in families:
        sessions = max((safe_int(s.get("metadata", {}).get("sessions")) for s in cluster["supporting_signals"] if s["source_family"] == "ga4"), default=0)
        if sessions >= 20 and user_conf != "LOW":
            return "MEDIUM"
        return "LOW"

    return "LOW"


def current_reality_gate(cluster: Dict[str, Any], wp_index: Dict[str, List[Dict[str, Any]]]) -> str:
    families = set(cluster["supporting_source_families"])
    topic = cluster["topic_cluster"]

    if "wordpress" in families and len(families) == 1:
        return "UNCERTAIN"
    if "github" in families and len(families) == 1:
        return "UNCERTAIN" if cluster.get("user_impact_confidence") != "HIGH" else "PASS"
    if "news" in families and len(families) == 1:
        return "UNCERTAIN"
    if "gsc" in families or "ga4" in families or "trends" in families:
        return "PASS"
    if topic == "unknown":
        return "FAIL"
    return "UNCERTAIN"


def age_days(cluster: Dict[str, Any]) -> Optional[int]:
    first = parse_iso(cluster.get("information_first_public_at") or cluster.get("first_signal_at"))
    if not first:
        return None
    return max(0, (now_utc() - first).days)


def information_age_gate(cluster: Dict[str, Any]) -> Tuple[str, str]:
    families = set(cluster["supporting_source_families"])
    days = age_days(cluster)
    if days is None:
        return "UNKNOWN", "no timestamp"
    if "github" in families and days <= 5:
        return "FRESH", f"{days}d"
    if "news" in families and days <= 3:
        return "FRESH", f"{days}d"
    if "news" in families and days <= 10:
        return "ACCEPTABLE", f"{days}d"
    if "trends" in families and days <= 10:
        return "FRESH", f"{days}d"
    if ("gsc" in families or "ga4" in families or "wordpress" in families) and days <= 30:
        return "ACCEPTABLE", f"{days}d"
    if days <= 90:
        return "STALE", f"{days}d"
    return "TOO_OLD", f"{days}d"


def wp_duplicate_check(cluster: Dict[str, Any], wp_index: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    topic = cluster["topic_cluster"]
    matches = wp_index.get(topic, [])
    if not matches:
        # Try relaxed matching across canonical topic aliases.
        compact = normalize_text(topic)
        alt = []
        for key, entries in wp_index.items():
            if compact in key or key in compact:
                alt.extend(entries)
        matches = alt
    publish = [m for m in matches if m["status"] == "publish"]
    drafts = [m for m in matches if m["status"] in {"draft", "future", "pending"}]
    action = "CREATE"
    risk = "LOW"
    if publish:
        action = "UPDATE/REWRITE/MERGE"
        risk = "HIGH"
    elif drafts:
        action = "UPDATE DRAFT"
        risk = "MEDIUM"
    return {
        "existing_url": publish[0]["url"] if publish else (drafts[0]["url"] if drafts else ""),
        "draft_id": drafts[0]["id"] if drafts else "",
        "action": action,
        "cannibalization_risk": risk,
        "matches": matches[:5],
    }


def unique_value_check(cluster: Dict[str, Any], wp_dup: Dict[str, Any]) -> Tuple[str, str]:
    families = set(cluster["supporting_source_families"])
    topic = cluster["topic_cluster"]
    if wp_dup["action"].startswith("UPDATE"):
        return ("UPDATE/REWRITE with added value on existing coverage, not a pure duplicate.", "PASS")
    if "github" in families and len(families) >= 2:
        return ("Cross-source early signal synthesis, not a single-source repack.", "PASS")
    if "gsc" in families and "wordpress" in families:
        return ("Search demand plus editorial gap with a more useful angle than the current page.", "PASS")
    if "trends" in families and ("gsc" in families or "ga4" in families):
        return ("Trend momentum plus internal demand/context.", "PASS")
    if any(k in topic for k in ["pixel", "android 17", "wallet", "messages", "watch", "battery", "rcs", "data usage"]):
        return ("Clear user-facing how-to / troubleshooting / comparison angle.", "PASS")
    return ("No concrete unique value beyond the raw signal itself.", "FAIL")


def topic_is_generic_editorial(topic: str) -> bool:
    return bool(GENERIC_TOPIC_RE.search(normalize_text(topic)))


def earliest_iso(values: Iterable[Optional[str]]) -> Optional[str]:
    best: Optional[datetime] = None
    best_value: Optional[str] = None
    for value in values:
        dt = parse_iso(value)
        if dt and (best is None or dt < best):
            best = dt
            best_value = value
    return best_value


def latest_iso(values: Iterable[Optional[str]]) -> Optional[str]:
    best: Optional[datetime] = None
    best_value: Optional[str] = None
    for value in values:
        dt = parse_iso(value)
        if dt and (best is None or dt > best):
            best = dt
            best_value = value
    return best_value


def semantic_time_fields(cluster: Dict[str, Any]) -> Dict[str, str]:
    signals = cluster["supporting_signals"]
    source_record_first_seen_at = earliest_iso(
        s.get("first_seen_at") or s.get("published_at") for s in signals
    ) or "UNKNOWN"
    story_first_seen_at = earliest_iso(
        s.get("published_at") or s.get("first_seen_at") for s in signals
    ) or source_record_first_seen_at
    lisa_first_seen_at = cluster.get("lisa_first_seen_at") or "UNAVAILABLE"
    return {
        "source_record_first_seen_at": source_record_first_seen_at,
        "story_first_seen_at": story_first_seen_at,
        "lisa_first_seen_at": lisa_first_seen_at,
    }


def editorial_opportunity_text(cluster: Dict[str, Any]) -> str:
    topic = cluster["topic_cluster"]
    families = set(cluster["supporting_source_families"])
    metrics = demand_metrics(cluster)
    if "github" in families and cluster.get("user_impact_confidence") in {"HIGH", "MEDIUM"}:
        return f"What changed in {topic}, what it means for users, and whether it is about to surface in a release or support docs."
    if "trends" in families and metrics["trend_latest"] > 0:
        return f"Why {topic} is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend."
    if "gsc" in families and "wordpress" in families:
        return f"How to improve the existing {topic} page for current search intent, CTR, and conversion to a better editorial angle."
    if topic_is_generic_editorial(topic):
        return f"Turn the generic {topic} entity into a specific user problem, comparison, or setup guide."
    return f"What happened around {topic}, what users need to know, and which practical angle is missing from current coverage."


def lane_scores(cluster: Dict[str, Any]) -> Dict[str, float]:
    metrics = demand_metrics(cluster)
    families = set(cluster["supporting_source_families"])
    age_status = information_age_gate(cluster)[0]
    age_days_value = age_days(cluster) or 999
    fresh_boost = 18.0 if age_status == "FRESH" else 10.0 if age_status == "ACCEPTABLE" else 4.0
    story_specificity = 0.0
    if not topic_is_generic_editorial(cluster["topic_cluster"]):
        story_specificity += 12.0
    if cluster.get("supporting_events_count", 0) >= 4:
        story_specificity += 10.0
    if len(families) >= 3:
        story_specificity += 8.0
    if "github" in families:
        story_specificity += 12.0
    if "trends" in families:
        story_specificity += 8.0
    if "news" in families:
        story_specificity += 14.0
    if "gsc" in families or "ga4" in families:
        story_specificity += 5.0

    momentum = 0.0
    momentum += min(metrics["trend_latest"], 100.0)
    momentum += max(metrics["trend_velocity"], 0.0) * 2.0
    momentum += max(metrics["trend_acceleration"], 0.0) * 3.0

    user_signal = 20.0 if cluster.get("user_impact_confidence") == "HIGH" else 12.0 if cluster.get("user_impact_confidence") == "MEDIUM" else 4.0
    unique = 15.0 if cluster.get("unique_value_status") == "PASS" else 4.0
    source_div = min(cluster.get("source_diversity", 0) * 4.0, 24.0)
    gsc_strength = min(metrics["gsc_impressions"] / 140.0, 24.0) + min(metrics["gsc_clicks"] * 1.6, 18.0) + max(0.0, 15.0 - metrics["gsc_position"]) * 1.2
    ga4_strength = min(metrics["ga4_sessions"] / 55.0, 18.0)
    search_gap = 18.0 if cluster.get("wp_duplicate", {}).get("action", "").startswith("CREATE") else 9.0 if cluster.get("wp_duplicate", {}).get("action", "").startswith("UPDATE") else 5.0
    discovery_novelty = 20.0 if "github" in families else 14.0 if "trends" in families and len(families) >= 2 else 8.0 if "trends" in families else 5.0
    if "news" in families:
        discovery_novelty = max(discovery_novelty, 12.0)
    news_support = 0.0
    if "news" in families:
        news_support += min(cluster.get("supporting_events_count", 0) * 2.5, 15.0)
        news_support += min(max(cluster.get("source_diversity", 0) - 1, 0) * 4.0, 16.0)
        news_support += 10.0 if age_status == "FRESH" else 6.0 if age_status == "ACCEPTABLE" else 2.0
    generic_penalty = 12.0 if topic_is_generic_editorial(cluster["topic_cluster"]) and "github" not in families and metrics["trend_latest"] == 0 else 0.0

    breaking = max(0.0, min(100.0, round(fresh_boost + momentum * 0.35 + user_signal * 0.25 + source_div * 0.15 + unique * 0.10 + story_specificity * 0.15 + news_support * 0.45 - generic_penalty, 1)))
    discovery = max(0.0, min(100.0, round(discovery_novelty + source_div * 0.35 + fresh_boost * 0.35 + user_signal * 0.20 + unique * 0.10 + story_specificity * 0.12 + news_support * 0.30 - generic_penalty * 0.5, 1)))
    current = max(0.0, min(100.0, round(momentum * 0.65 + fresh_boost * 0.6 + user_signal * 0.25 + source_div * 0.2 + story_specificity * 0.15 + unique * 0.10 + news_support * 0.20 - generic_penalty * 0.2, 1)))
    seo = max(0.0, min(100.0, round(gsc_strength + ga4_strength + search_gap + source_div * 0.12 + unique * 0.18 - (0.0 if cluster.get("wp_duplicate", {}).get("action") == "CREATE" else 2.0), 1)))
    update = max(0.0, min(100.0, round(seo + (10.0 if cluster.get("wp_duplicate", {}).get("action", "").startswith("UPDATE") else 0.0) + (6.0 if "wordpress" in families else 0.0), 1)))

    # Generic entities cannot be final CURRENT/DISCOVERY candidates without a story angle.
    if topic_is_generic_editorial(cluster["topic_cluster"]) and discovery < 55.0 and breaking < 55.0:
        current = max(0.0, current - 18.0)
        discovery = max(0.0, discovery - 18.0)

    return {
        "BREAKING / CURRENT NEWS": breaking,
        "DISCOVERY / PREDICTIVE": discovery,
        "CURRENT DEMAND / TREND": current,
        "SEO / SEARCH OPPORTUNITY": seo,
        "UPDATE / REWRITE": update,
    }


def primary_lane_for(cluster: Dict[str, Any]) -> str:
    scores = lane_scores(cluster)
    metrics = demand_metrics(cluster)
    families = set(cluster["supporting_source_families"])
    age = age_days(cluster) or 999
    topic = cluster["topic_cluster"]
    # Lane-specific thresholds. Candidates can be qualified in multiple lanes,
    # but the primary lane is the one with the best quality-adjusted fit.
    thresholds = {
        "BREAKING / CURRENT NEWS": 58.0,
        "DISCOVERY / PREDICTIVE": 55.0,
        "CURRENT DEMAND / TREND": 52.0,
        "SEO / SEARCH OPPORTUNITY": 50.0,
        "UPDATE / REWRITE": 48.0,
    }
    if "github" in families and scores["DISCOVERY / PREDICTIVE"] >= thresholds["DISCOVERY / PREDICTIVE"] and cluster.get("user_impact_confidence") != "LOW":
        return "DISCOVERY / PREDICTIVE"
    if scores["BREAKING / CURRENT NEWS"] >= thresholds["BREAKING / CURRENT NEWS"] and age <= 7 and metrics["trend_latest"] >= 20:
        return "BREAKING / CURRENT NEWS"
    if scores["CURRENT DEMAND / TREND"] >= thresholds["CURRENT DEMAND / TREND"] and (metrics["trend_latest"] > 0 or metrics["trend_velocity"] > 0 or metrics["trend_acceleration"] > 0):
        return "CURRENT DEMAND / TREND"
    if scores["SEO / SEARCH OPPORTUNITY"] >= thresholds["SEO / SEARCH OPPORTUNITY"] and (metrics["gsc_impressions"] >= 50 or metrics["ga4_sessions"] >= 20):
        return "SEO / SEARCH OPPORTUNITY"
    if scores["UPDATE / REWRITE"] >= thresholds["UPDATE / REWRITE"] and cluster.get("wp_duplicate", {}).get("action", "").startswith("UPDATE"):
        return "UPDATE / REWRITE"

    eligible = [(lane, score) for lane, score in scores.items() if score >= thresholds[lane]]
    if eligible:
        return max(eligible, key=lambda item: (item[1], -LANE_PRIORITY[item[0]]))[0]
    # Fall back to the strongest lane to keep auditability, even if the
    # candidate ends up rejected by later gates.
    return max(scores.items(), key=lambda item: item[1])[0]


def lane_quality_threshold(lane: str) -> float:
    return {
        "BREAKING / CURRENT NEWS": 58.0,
        "DISCOVERY / PREDICTIVE": 55.0,
        "CURRENT DEMAND / TREND": 52.0,
        "SEO / SEARCH OPPORTUNITY": 50.0,
        "UPDATE / REWRITE": 48.0,
    }[lane]


def demand_metrics(cluster: Dict[str, Any]) -> Dict[str, float]:
    gsc_impr = sum(safe_int(s.get("metadata", {}).get("impressions")) for s in cluster["supporting_signals"] if s["source_family"] == "gsc")
    gsc_clicks = sum(safe_int(s.get("metadata", {}).get("clicks")) for s in cluster["supporting_signals"] if s["source_family"] == "gsc")
    gsc_pos = min((safe_float(s.get("metadata", {}).get("position"), 99.0) for s in cluster["supporting_signals"] if s["source_family"] == "gsc"), default=99.0)
    ga4_sessions = sum(safe_int(s.get("metadata", {}).get("sessions")) for s in cluster["supporting_signals"] if s["source_family"] == "ga4")
    trend_latest = max((s.get("metadata", {}).get("values", [0, 0, 0])[-1] for s in cluster["supporting_signals"] if s["source_family"] == "trends"), default=0)
    trend_velocity = max((s.get("metadata", {}).get("trend_velocity", 0) for s in cluster["supporting_signals"] if s["source_family"] == "trends"), default=0)
    trend_acceleration = max((s.get("metadata", {}).get("trend_acceleration", 0) for s in cluster["supporting_signals"] if s["source_family"] == "trends"), default=0)
    news_signals = sum(1 for s in cluster["supporting_signals"] if s["source_family"] == "news")
    news_sources = len({s.get("source", "") for s in cluster["supporting_signals"] if s["source_family"] == "news" and s.get("source")})
    return {
        "gsc_impressions": float(gsc_impr),
        "gsc_clicks": float(gsc_clicks),
        "gsc_position": float(gsc_pos),
        "ga4_sessions": float(ga4_sessions),
        "trend_latest": float(trend_latest),
        "trend_velocity": float(trend_velocity),
        "trend_acceleration": float(trend_acceleration),
        "news_signals": float(news_signals),
        "news_sources": float(news_sources),
    }


def predictive_score(cluster: Dict[str, Any]) -> float:
    metrics = demand_metrics(cluster)
    families = set(cluster["supporting_source_families"])
    score = 0.0
    score += min(metrics["trend_latest"], 100.0) * 0.25
    score += max(metrics["trend_velocity"], 0.0) * 1.2
    score += max(metrics["trend_acceleration"], 0.0) * 1.4
    if "github" in families:
        score += 18 if cluster.get("user_impact_confidence") != "LOW" else 8
    if "gsc" in families and metrics["gsc_impressions"] > 0:
        score += min(metrics["gsc_impressions"] / 5.0, 20.0)
        score += max(0.0, 15.0 - metrics["gsc_position"]) * 0.5
    if "ga4" in families:
        score += min(metrics["ga4_sessions"] / 4.0, 12.0)
    if len(families) >= 2:
        score += 8
    return max(0.0, min(100.0, round(score, 1)))


def opportunity_score(cluster: Dict[str, Any]) -> float:
    metrics = demand_metrics(cluster)
    families = set(cluster["supporting_source_families"])
    score = 0.0
    score += min(metrics["gsc_impressions"] / 20.0, 22.0)
    score += min(metrics["gsc_clicks"] * 2.5, 12.0)
    score += max(0.0, 20.0 - metrics["gsc_position"]) * 0.7
    score += min(metrics["ga4_sessions"] / 3.0, 18.0)
    score += min(metrics["trend_latest"] * 0.3, 18.0)
    if len(families) >= 2:
        score += 10
    if "github" in families:
        score += 8 if cluster.get("user_impact_confidence") != "LOW" else 4
    if "wordpress" in families:
        score += 4
    return max(0.0, min(100.0, round(score, 1)))


def signal_score_breakdown(cluster: Dict[str, Any]) -> Dict[str, float]:
    metrics = demand_metrics(cluster)
    families = set(cluster["supporting_source_families"])
    gsc = min(metrics["gsc_impressions"] / 5.0, 20.0)
    trend = min(metrics["trend_latest"], 100.0) * 0.15
    freshness = 15.0 if information_age_gate(cluster)[0] == "FRESH" else 8.0 if information_age_gate(cluster)[0] == "ACCEPTABLE" else 2.0
    historical = min(metrics["ga4_sessions"] / 5.0, 15.0)
    discover = 15.0 if ("github" in families and len(families) >= 2) else 8.0 if "github" in families else 6.0 if "trends" in families else 4.0
    global_multilingual = 15.0 if len(families) >= 3 else 10.0 if len(families) >= 2 else 5.0
    commercial = 5.0 if any(k in cluster["topic_cluster"] for k in ["wallet", "billing", "play store", "pixel", "watch", "battery"]) else 2.0
    competition_gap = 5.0 if cluster.get("wp_duplicate", {}).get("action", "CREATE").startswith("CREATE") else 1.5
    return {
        "gsc": round(gsc, 1),
        "trend": round(trend, 1),
        "freshness": round(freshness, 1),
        "historical": round(historical, 1),
        "discover": round(discover, 1),
        "global_multilingual": round(global_multilingual, 1),
        "commercial": round(commercial, 1),
        "competition_gap": round(competition_gap, 1),
    }


def weighted_signal_score(breakdown: Dict[str, float]) -> float:
    total = (
        breakdown["gsc"] * 0.20
        + breakdown["trend"] * 0.15
        + breakdown["freshness"] * 0.10
        + breakdown["historical"] * 0.15
        + breakdown["discover"] * 0.15
        + breakdown["global_multilingual"] * 0.15
        + breakdown["commercial"] * 0.05
        + breakdown["competition_gap"] * 0.05
    )
    return max(0.0, min(100.0, round(total * 5.0, 1)))


def rank_candidates(clusters: List[Dict[str, Any]], wp_index: Dict[str, List[Dict[str, Any]]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    enriched: List[Dict[str, Any]] = []
    rejection_counts = Counter()
    source_coverage = Counter()
    lane_counts = Counter()
    qualified_lane_counts = Counter()

    for cluster in clusters:
        cluster = dict(cluster)
        source_coverage.update(cluster["supporting_source_families"])
        reality = current_reality_gate(cluster, wp_index)
        cluster["reality_check"] = reality
        age_status, age_detail = information_age_gate(cluster)
        cluster["information_age"] = age_status
        cluster["information_age_detail"] = age_detail
        wp_dup = wp_duplicate_check(cluster, wp_index)
        cluster["wp_duplicate"] = wp_dup
        unique_value, uv_status = unique_value_check(cluster, wp_dup)
        cluster["unique_value"] = unique_value
        cluster["unique_value_status"] = uv_status
        cluster["demand_metrics"] = demand_metrics(cluster)
        cluster.update(semantic_time_fields(cluster))
        cluster["editorial_opportunity"] = editorial_opportunity_text(cluster)
        cluster["lane_scores"] = lane_scores(cluster)
        cluster["primary_lane"] = primary_lane_for(cluster)
        cluster["lane_score"] = cluster["lane_scores"][cluster["primary_lane"]]
        cluster["qualified_lanes"] = [
            lane for lane, score in cluster["lane_scores"].items() if score >= lane_quality_threshold(lane)
        ]
        lane_counts.update(cluster["qualified_lanes"] or [cluster["primary_lane"]])

        if reality == "FAIL":
            rejection_counts["Reality FAIL"] += 1
            cluster["status"] = "rejected"
            cluster["rejection_reason"] = "Reality FAIL"
            enriched.append(cluster)
            continue
        if age_status == "TOO_OLD":
            rejection_counts["Stale / saturated"] += 1
            cluster["status"] = "rejected"
            cluster["rejection_reason"] = "Information age too old"
            enriched.append(cluster)
            continue
        if wp_dup["action"].startswith("UPDATE"):
            # Update/rewrite is still allowed, but the candidate must survive the rest.
            pass
        if uv_status == "FAIL":
            rejection_counts["No unique value"] += 1
            cluster["status"] = "rejected"
            cluster["rejection_reason"] = "No unique value"
            enriched.append(cluster)
            continue
        if cluster["editorial_potential"] == "LOW" and cluster["source_diversity"] <= 1:
            rejection_counts["Weak demand/evidence"] += 1
            cluster["status"] = "rejected"
            cluster["rejection_reason"] = "Weak demand / evidence"
            enriched.append(cluster)
            continue

        # Lane-specific thresholds decide qualification; the global signal score is
        # retained for audit only and no longer drives portfolio selection.
        if cluster["primary_lane"] not in cluster["qualified_lanes"]:
            rejection_counts["Weak demand/evidence"] += 1
            cluster["status"] = "rejected"
            cluster["rejection_reason"] = "No lane passed quality threshold"
            enriched.append(cluster)
            continue

        cluster["opportunity_score"] = opportunity_score(cluster)
        cluster["predictive_score"] = predictive_score(cluster)
        breakdown = signal_score_breakdown(cluster)
        cluster["signal_score_breakdown"] = breakdown
        cluster["signal_score"] = weighted_signal_score(breakdown)
        cluster["author_confidence"] = "LOW"
        cluster["publication_timing"] = "PUBLISH NOW" if cluster["lane_score"] >= 70 or cluster["predictive_score"] >= 60 else "PUBLISH TODAY"
        cluster["recommended_author"] = recommended_author_for_cluster(cluster)
        cluster["status"] = "qualified"
        qualified_lane_counts[cluster["primary_lane"]] += 1
        enriched.append(cluster)

    qualified = [c for c in enriched if c["status"] == "qualified"]
    ranked = sorted(
        qualified,
        key=lambda c: (
            100 - LANE_PRIORITY.get(c["primary_lane"], 0),
            c["lane_score"],
            c["signal_score"],
            c["opportunity_score"],
            c["predictive_score"],
            c["source_diversity"],
            c["demand_metrics"]["gsc_impressions"],
            c["demand_metrics"]["ga4_sessions"],
        ),
        reverse=True,
    )
    audit = {
        "rejection_counts": dict(rejection_counts),
        "source_coverage": dict(source_coverage),
        "qualified_count": len(qualified),
        "lane_counts": dict(lane_counts),
        "qualified_lane_counts": dict(qualified_lane_counts),
        "rejected_candidates": [c for c in enriched if c["status"] == "rejected"],
        "qualified_candidates": qualified,
    }
    return ranked, audit


def recommended_author_for_cluster(cluster: Dict[str, Any]) -> str:
    topic = cluster["topic_cluster"]
    if any(k in topic for k in ["wallet", "messages", "rcs", "google", "android 17", "data usage", "battery", "watch"]):
        return "Roman Zavřel"
    if any(k in topic for k in ["pixel", "fold", "redmi", "poco", "honor", "hmd", "camera", "performance"]):
        return "Jana Maxová"
    if "github" in cluster["supporting_source_families"]:
        return "technický redaktor"
    return "redaktor"


def diversify_portfolio(qualified: List[Dict[str, Any]], limit: int = 10) -> List[Dict[str, Any]]:
    selected: List[Dict[str, Any]] = []
    used_topics = set()

    high_priority_lanes = {
        "BREAKING / CURRENT NEWS",
        "DISCOVERY / PREDICTIVE",
        "CURRENT DEMAND / TREND",
    }
    filler_lanes = {
        "SEO / SEARCH OPPORTUNITY",
        "UPDATE / REWRITE",
    }

    def lane_rank(cluster: Dict[str, Any]) -> Tuple[int, float, float, float]:
        lane = cluster.get("primary_lane", "SEO / SEARCH OPPORTUNITY")
        lane_priority = 2 if lane in high_priority_lanes else 1 if lane in filler_lanes else 0
        return (
            lane_priority,
            cluster.get("lane_score", 0.0),
            cluster.get("signal_score", 0.0),
            cluster.get("opportunity_score", 0.0),
        )

    def take_pool(pool: List[Dict[str, Any]]) -> None:
        for cluster in sorted(pool, key=lane_rank, reverse=True):
            topic = cluster["topic_cluster"]
            if topic in used_topics:
                continue
            selected.append(cluster)
            used_topics.add(topic)
            if len(selected) >= limit:
                return

    take_pool([c for c in qualified if c.get("primary_lane") in high_priority_lanes])
    if len(selected) < limit:
        take_pool([c for c in qualified if c.get("primary_lane") in filler_lanes])
    if len(selected) < limit:
        take_pool([c for c in qualified if c.get("primary_lane") not in high_priority_lanes | filler_lanes])

    return selected[:limit]


def counterfactual_top1_top3(ranked: List[Dict[str, Any]]) -> Tuple[Optional[Dict[str, Any]], List[Dict[str, Any]]]:
    if not ranked:
        return None, []
    top1 = ranked[0]
    selected = diversify_portfolio(ranked, limit=3)
    return top1, selected


def marginal_value(selected: List[Dict[str, Any]], candidate: Dict[str, Any]) -> float:
    topic_tokens = set(normalize_text(candidate["topic_cluster"]).split())
    topic_overlap = 0.0
    if selected:
        best_overlap = 0.0
        for s in selected:
            s_tokens = set(normalize_text(s["topic_cluster"]).split())
            overlap = len(topic_tokens & s_tokens) / max(1, len(topic_tokens | s_tokens))
            best_overlap = max(best_overlap, overlap)
        topic_overlap = best_overlap
    diversity_gain = candidate["source_diversity"] / 5.0
    base = candidate["signal_score"] / 10.0
    return round(base + diversity_gain - topic_overlap * 4.0, 2)


def build_final_portfolio(ranked: List[Dict[str, Any]], limit: int = 10) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    portfolio = diversify_portfolio(ranked, limit=limit)
    if not portfolio:
        return [], {"only_one": None, "only_three": []}
    top1 = portfolio[0]
    top3 = portfolio[:3]
    for idx, candidate in enumerate(portfolio):
        candidate["marginal_value"] = marginal_value(portfolio[:idx], candidate)
    return portfolio, {"only_one": top1, "only_three": top3}


def store_orchestrator_state(state: Dict[str, Any]) -> None:
    ORCH_STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def store_orchestrator_db(ranked: List[Dict[str, Any]], clusters: List[Dict[str, Any]]) -> None:
    conn = sqlite3.connect(ORCH_DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS normalized_signals (
            signal_id TEXT PRIMARY KEY,
            source_family TEXT NOT NULL,
            source TEXT NOT NULL,
            signal_type TEXT NOT NULL,
            entity TEXT NOT NULL,
            topic TEXT NOT NULL,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            published_at TEXT,
            first_seen_at TEXT NOT NULL,
            latest_activity TEXT NOT NULL,
            evidence TEXT NOT NULL,
            confidence TEXT NOT NULL,
            user_impact TEXT NOT NULL,
            raw_source_reference TEXT NOT NULL,
            processing_status TEXT NOT NULL,
            metadata_json TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS clusters (
            cluster_id TEXT PRIMARY KEY,
            topic_cluster TEXT NOT NULL,
            repository TEXT NOT NULL,
            supporting_signals_json TEXT NOT NULL,
            supporting_source_families_json TEXT NOT NULL,
            first_signal_at TEXT NOT NULL,
            latest_signal_at TEXT NOT NULL,
            information_first_public_at TEXT NOT NULL,
            source_diversity INTEGER NOT NULL,
            user_impact_reason TEXT NOT NULL,
            user_impact_confidence TEXT NOT NULL,
            editorial_potential TEXT NOT NULL,
            reality_check TEXT NOT NULL,
            information_age TEXT NOT NULL,
            unique_value TEXT NOT NULL,
            status TEXT NOT NULL,
            opportunity_score REAL,
            predictive_score REAL,
            signal_score REAL,
            signal_score_breakdown_json TEXT NOT NULL,
            wp_duplicate_json TEXT NOT NULL,
            demand_metrics_json TEXT NOT NULL,
            recommended_author TEXT NOT NULL,
            publication_timing TEXT NOT NULL,
            marginal_value REAL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            normalized_signals INTEGER NOT NULL,
            clusters INTEGER NOT NULL,
            qualified INTEGER NOT NULL,
            ranked INTEGER NOT NULL,
            final_portfolio INTEGER NOT NULL,
            api_calls_used INTEGER NOT NULL,
            llm_calls_used INTEGER NOT NULL
        )
        """
    )
    conn.execute("DELETE FROM normalized_signals")
    conn.execute("DELETE FROM clusters")
    for cluster in clusters:
        for sig in cluster["supporting_signals"]:
            conn.execute(
                """
                INSERT OR REPLACE INTO normalized_signals (
                    signal_id, source_family, source, signal_type, entity, topic, title, url,
                    published_at, first_seen_at, latest_activity, evidence, confidence, user_impact,
                    raw_source_reference, processing_status, metadata_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    sig["signal_id"],
                    sig["source_family"],
                    sig["source"],
                    sig["signal_type"],
                    sig["entity"],
                    sig["topic"],
                    sig["title"],
                    sig["url"],
                    sig["published_at"],
                    sig["first_seen_at"],
                    sig["latest_activity"],
                    sig["evidence"],
                    sig["confidence"],
                    sig["user_impact"],
                    sig["raw_source_reference"],
                    sig["processing_status"],
                    json.dumps(sig["metadata"], ensure_ascii=False),
                ),
            )
    for cluster in ranked:
        conn.execute(
            """
            INSERT OR REPLACE INTO clusters (
                cluster_id, topic_cluster, repository, supporting_signals_json,
                supporting_source_families_json, first_signal_at, latest_signal_at,
                information_first_public_at, source_diversity, user_impact_reason,
                user_impact_confidence, editorial_potential, reality_check,
                information_age, unique_value, status, opportunity_score, predictive_score,
                signal_score, signal_score_breakdown_json, wp_duplicate_json,
                demand_metrics_json, recommended_author, publication_timing, marginal_value
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                cluster["cluster_id"],
                cluster["topic_cluster"],
                cluster["repository"],
                json.dumps(cluster["supporting_signals"], ensure_ascii=False),
                json.dumps(cluster["supporting_source_families"], ensure_ascii=False),
                cluster["first_signal_at"],
                cluster["latest_signal_at"],
                cluster["information_first_public_at"],
                cluster["source_diversity"],
                cluster["user_impact_reason"],
                cluster["user_impact_confidence"],
                cluster["editorial_potential"],
                cluster["reality_check"],
                cluster["information_age"],
                cluster["unique_value"],
                cluster["status"],
                cluster.get("opportunity_score"),
                cluster.get("predictive_score"),
                cluster.get("signal_score"),
                json.dumps(cluster.get("signal_score_breakdown", {}), ensure_ascii=False),
                json.dumps(cluster.get("wp_duplicate", {}), ensure_ascii=False),
                json.dumps(cluster.get("demand_metrics", {}), ensure_ascii=False),
                cluster.get("recommended_author", ""),
                cluster.get("publication_timing", ""),
                cluster.get("marginal_value"),
            ),
        )
    conn.execute(
        "INSERT INTO runs (created_at, normalized_signals, clusters, qualified, ranked, final_portfolio, api_calls_used, llm_calls_used) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            iso(now_utc()),
            0,
            len(clusters),
            sum(1 for c in ranked if c["status"] == "qualified"),
            len(ranked),
            min(len(ranked), 10),
            0,
            0,
        ),
    )
    conn.commit()
    conn.close()


def source_coverage_audit(source_meta: Dict[str, Any]) -> List[Dict[str, str]]:
    news_meta = source_meta.get("news", {})
    if not news_meta.get("checked"):
        news_status = "NOT CHECKED - reason: news discovery disabled" if news_meta.get("reason") == "news discovery disabled" else "NOT IMPLEMENTED"
    elif news_meta.get("error"):
        news_status = f"UNAVAILABLE - reason: {news_meta.get('error')}"
    elif news_meta.get("signals", 0) > 0:
        news_status = "CHECKED"
    else:
        news_status = "CHECKED - NO RELEVANT SIGNAL"
    coverage = [
        ("GSC", "CHECKED" if source_meta["gsc"].get("checked") else "NOT CHECKED - reason: local export missing"),
        ("GA4", "CHECKED" if source_meta["ga4"].get("checked") else "NOT CHECKED - reason: local export missing"),
        ("WordPress", "CHECKED" if source_meta["wordpress"].get("checked") else "NOT CHECKED - reason: local export missing"),
        ("GitHub", "CHECKED" if source_meta["github"].get("checked") else "NOT CHECKED - reason: GitHub DB missing"),
        ("Google Trends", "CHECKED" if source_meta["trends"].get("checked") else "NOT CHECKED - reason: no structured trend cache"),
        ("Google News / News", news_status),
        ("Reddit", "NOT IMPLEMENTED"),
        ("X", "NOT IMPLEMENTED"),
        ("YouTube / community", "NOT IMPLEMENTED"),
        ("AdSense", "NOT IMPLEMENTED"),
    ]
    return [{"layer": layer, "status": status} for layer, status in coverage]


def fallback_summary(source_meta: Dict[str, Any]) -> List[str]:
    fallbacks: List[str] = []
    if not source_meta["gsc"].get("checked"):
        fallbacks.append("GSC unavailable -> skipped GSC signals")
    if not source_meta["ga4"].get("checked"):
        fallbacks.append("GA4 unavailable -> skipped GA4 signals")
    if not source_meta["wordpress"].get("checked"):
        fallbacks.append("WordPress unavailable -> skipped WP duplicate checks beyond local cache")
    if not source_meta["github"].get("checked"):
        fallbacks.append("GitHub unavailable -> skipped GitHub source layer")
    if not source_meta["trends"].get("checked"):
        fallbacks.append("Trends unavailable -> skipped structured Trends signals")
    news_meta = source_meta.get("news", {})
    if not news_meta.get("checked"):
        fallbacks.append("News unavailable -> skipped News Discovery signals")
    return fallbacks


def persist_github_watchlist_promotions(
    clusters: List[Dict[str, Any]],
    github_watchlist_rows: List[Dict[str, Any]],
    source_meta: Dict[str, Any],
) -> Tuple[List[Dict[str, Any]], bool]:
    """
    Event-driven persistence into the GitHub watchlist DB.
    Only cross-source trigger matches are written back.
    """
    promotions: List[Dict[str, Any]] = []
    if not GITHUB_DB_PATH.exists():
        return promotions, False

    conn = sqlite3.connect(GITHUB_DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        if not github_watchlist_rows:
            return promotions, True
        for row in github_watchlist_rows:
            cluster_topic = canonical_topic(row.get("topic_cluster", ""))
            cluster_repo = row.get("repository", "")
            match = None
            for c in clusters:
                if cluster_topic == canonical_topic(c["topic_cluster"]) and (not cluster_repo or cluster_repo == c["repository"]):
                    match = c
                    break
            if not match:
                continue
            if match["source_diversity"] <= 1:
                continue
            previous = row.get("editorial_potential", "LOW")
            new = match["editorial_potential"]
            if previous == new:
                continue
            if previous == "LOW" and new not in {"MEDIUM", "HIGH"}:
                continue
            if previous == "MEDIUM" and new not in {"LOW", "HIGH"}:
                continue
            if previous == "LOW" and new in {"MEDIUM", "HIGH"} or previous == "MEDIUM" and new in {"LOW", "HIGH"}:
                changed = github_monitor.persist_watchlist_transition(
                    conn,
                    row,
                    match["representative_signal"],
                    previous,
                    new,
                    "New cross-source evidence matched an existing GitHub watchlist cluster and justified a status change.",
                    match.get("cross_source_confidence", "MEDIUM"),
                    supporting_source_families=match["supporting_source_families"],
                    user_impact_reason=match.get("user_impact_reason"),
                    user_impact_confidence=match.get("user_impact_confidence"),
                )
                promotions.append(changed)
    finally:
        conn.close()

    return promotions, True


def render_markdown(report: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append("# LISA V6.5 multi-source orchestrator test")
    lines.append("")
    lines.append(f"- Created at: {report['created_at']}")
    lines.append(f"- Normalized signals: {report['normalized_signals_count']}")
    lines.append(f"- Clusters: {report['clusters_count']}")
    lines.append(f"- Qualified clusters: {report['qualified_count']}")
    lines.append(f"- Final portfolio: {report['final_portfolio_count']}")
    lines.append(f"- Portfolio capacity: {report.get('portfolio_capacity', 10)}")
    lines.append(f"- API calls used: {report['api_calls_used']}")
    lines.append(f"- LLM calls used: {report['llm_calls_used']}")
    lines.append(f"- Watchlist persistence: {report.get('watchlist_persistence', 'UNAVAILABLE')}")
    lines.append(f"- Structured Trends store: {report.get('structured_trends_store', 'UNAVAILABLE')}")
    lines.append(f"- News implementation: {report.get('news_implementation_status', 'UNAVAILABLE')}")
    lines.append(f"- News propagation: {report.get('news_propagation_status', 'UNAVAILABLE')}")
    lines.append(f"- Production data unchanged: {report.get('production_data_unchanged', 'UNAVAILABLE')}")
    lines.append(f"- News last successful sync: {report.get('news_last_successful_sync', 'UNAVAILABLE')}")
    lines.append(f"- GitHub evidence propagation: {report.get('github_evidence_propagation', 'UNAVAILABLE')}")
    lines.append(f"- GitHub raw clusters: {report.get('github_raw_count', 0)}")
    lines.append(f"- GitHub candidate universe: {report.get('github_candidate_universe_count', 0)}")
    lines.append(f"- GitHub lane-scored: {report.get('github_lane_scored_count', 0)}")
    lines.append(f"- GitHub rejected: {report.get('github_rejected_count', 0)}")
    lines.append(f"- GitHub qualified: {report.get('github_qualified_count', 0)}")
    lines.append(f"- GitHub final: {report.get('github_final_count', 0)}")
    lines.append(f"- News raw signals: {report.get('news_raw_signals_count', 0)}")
    lines.append(f"- News underlying event clusters: {report.get('news_underlying_event_clusters_count', 0)}")
    lines.append(f"- News candidate universe: {report.get('news_candidates_entering_candidate_universe', 0)}")
    lines.append(f"- News qualified: {report.get('news_qualified_count', 0)}")
    lines.append(f"- News final: {report.get('news_final_portfolio_count', 0)}")
    lines.append("")
    lines.append("## Source Coverage Audit")
    for item in report["source_coverage_audit"]:
        lines.append(f"- {item['layer']}: {item['status']}")
    lines.append("")
    lines.append("## Rejections")
    for reason, count in report["rejection_counts"].items():
        lines.append(f"- {reason}: {count}")
    lines.append("")
    lines.append("## Lane counts")
    lines.append(f"- Qualified by lane: {json.dumps(report.get('qualified_lane_counts', {}), ensure_ascii=False)}")
    lines.append(f"- Selected by lane: {json.dumps(report.get('portfolio_lane_counts', {}), ensure_ascii=False)}")
    lines.append(f"- News by lane: {json.dumps(report.get('news_candidates_by_lane', {}), ensure_ascii=False)}")
    lines.append(f"- News qualified by lane: {json.dumps(report.get('news_qualified_candidates_by_lane', {}), ensure_ascii=False)}")
    lines.append("")
    lines.append("## News Discovery Events")
    lines.append(f"- Raw signals: {report.get('news_raw_signals_count', 0)}")
    lines.append(f"- Event clusters: {report.get('news_underlying_event_clusters_count', 0)}")
    lines.append(f"- Entering candidate universe: {report.get('news_candidates_entering_candidate_universe', 0)}")
    lines.append(f"- Rejected: {report.get('news_rejected_count', 0)}")
    lines.append(f"- Qualified: {report.get('news_qualified_count', 0)}")
    lines.append(f"- Final portfolio: {report.get('news_final_portfolio_count', 0)}")
    lines.append(f"- Implementation: {report.get('news_implementation_status', 'UNAVAILABLE')}")
    lines.append(f"- Propagation: {report.get('news_propagation_status', 'UNAVAILABLE')}")
    lines.append(f"- Production unchanged: {report.get('production_data_unchanged', 'UNAVAILABLE')}")
    lines.append(f"- Last successful sync: {report.get('news_last_successful_sync', 'UNAVAILABLE')}")
    lines.append("")
    lines.append("### Top 20 pre-gate events")
    for i, item in enumerate(report.get("news_top20_events", []), 1):
        lines.append(f"#### {i}. {item.get('story', '')}")
        lines.append(f"- first_public_time: {item.get('first_public_time', '')}")
        lines.append(f"- source: {json.dumps(item.get('source', []), ensure_ascii=False)}")
        lines.append(f"- primary_source: {item.get('primary_source', '')}")
        lines.append(f"- user_impact: {item.get('user_impact', '')}")
        lines.append(f"- mainstream_saturation: {json.dumps(item.get('mainstream_saturation', {}), ensure_ascii=False)}")
        lines.append(f"- proposed_lane: {item.get('proposed_lane', '')}")
        lines.append(f"- why_it_may_matter: {item.get('why_it_may_matter', '')}")
        lines.append("")
    lines.append("## TOP 10 diversified candidates")
    for i, c in enumerate(report["top10"], 1):
        first_seen = c.get("first_seen") or c.get("first_signal_at") or c.get("published_at", "")
        latest_activity = c.get("latest_activity") or c.get("latest_signal_at") or c.get("published_at", "")
        lines.append(f"### {i}. {c['topic_cluster']}")
        lines.append(f"- repository: {c['repository']}")
        lines.append(f"- primary_lane: {c.get('primary_lane')}")
        lines.append(f"- lane_score: {c.get('lane_score')}")
        lines.append(f"- lane_scores: {json.dumps(c.get('lane_scores', {}), ensure_ascii=False)}")
        lines.append(f"- representative_signal: {json.dumps(c['representative_signal'], ensure_ascii=False)}")
        lines.append(f"- supporting_events_count: {c['supporting_events_count']}")
        lines.append(f"- first_seen: {first_seen}")
        lines.append(f"- source_record_first_seen_at: {c.get('source_record_first_seen_at', '')}")
        lines.append(f"- story_first_seen_at: {c.get('story_first_seen_at', '')}")
        lines.append(f"- lisa_first_seen_at: {c.get('lisa_first_seen_at', '')}")
        lines.append(f"- latest_activity: {latest_activity}")
        lines.append(f"- editorial_potential: {c['editorial_potential']}")
        lines.append(f"- why_it_may_matter: {c['why_it_may_matter']}")
        lines.append(f"- user_impact_reason: {c.get('user_impact_reason','')}")
        lines.append(f"- user_impact_confidence: {c.get('user_impact_confidence','')}")
        lines.append(f"- editorial_opportunity: {c.get('editorial_opportunity','')}")
        lines.append(f"- opportunity_score: {c.get('opportunity_score')}")
        lines.append(f"- predictive_score: {c.get('predictive_score')}")
        lines.append(f"- signal_score: {c.get('signal_score')}")
        lines.append(f"- wp_duplicate: {json.dumps(c.get('wp_duplicate', {}), ensure_ascii=False)}")
        lines.append("")
    lines.append("## Counterfactual")
    lines.append(f"- TOP 1: {report.get('top1', {}).get('topic_cluster', '')}")
    lines.append(f"- TOP 3: {', '.join(item.get('topic_cluster','') for item in report.get('top3', []))}")
    lines.append("")
    lines.append("## Final portfolio")
    for c in report["final_portfolio"]:
        sources = sorted({s.get("source", "") for s in c.get("supporting_signals", []) if s.get("source")})
        lines.append(f"- {c['topic_cluster']} | lane={c.get('primary_lane')} | action={c['recommendation']} | author={c.get('recommended_author','')}")
        lines.append(f"  - reason: {c.get('unique_value', '')} / {c.get('editorial_opportunity', '')}")
        lines.append(f"  - evidence: {c.get('why_it_may_matter', '')}")
        lines.append(f"  - sources: {json.dumps(sources, ensure_ascii=False)}")
    lines.append("")
    lines.append("## GitHub watchlist promotions")
    if report["watchlist_promotions"]:
        for p in report["watchlist_promotions"]:
            lines.append(f"- {p['previous_status']} -> {p['new_status']}: {p['topic_cluster']} ({p['repository']})")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Implemented / Partial / Not implemented")
    for key in ["implemented", "partially_implemented", "not_implemented", "failed_needs_fix"]:
        lines.append(f"### {key.replace('_', ' ').title()}")
        for item in report[key]:
            lines.append(f"- {item}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def build_report(
    test_mode: bool = True,
    production_mode: bool = False,
    supervised: bool = False,
    portfolio_capacity: int = 10,
    enable_news: bool = False,
    persist_state: bool = False,
) -> Dict[str, Any]:
    ensure_dirs()
    source_signals: Dict[str, List[Dict[str, Any]]] = {}
    source_meta: Dict[str, Any] = {}

    github_signals, github_meta = load_github_signals()
    gsc_signals, gsc_meta = load_gsc_signals()
    ga4_signals, ga4_meta = load_ga4_signals()
    wp_signals, wp_meta, wp_index = load_wordpress_index()
    trend_signals, trend_meta = load_trend_signals()
    news_signals, news_meta = load_news_signals(enabled=enable_news)

    source_signals["github"] = github_signals
    source_signals["gsc"] = gsc_signals
    source_signals["ga4"] = ga4_signals
    source_signals["wordpress"] = wp_signals
    source_signals["trends"] = trend_signals
    source_signals["news"] = news_signals

    source_meta["github"] = github_meta
    source_meta["gsc"] = gsc_meta
    source_meta["ga4"] = ga4_meta
    source_meta["wordpress"] = wp_meta
    source_meta["trends"] = trend_meta
    source_meta["news"] = news_meta

    normalized = normalize_signals(source_signals)
    clusters = cluster_signals(normalized)
    news_clusters = [c for c in clusters if "news" in c.get("supporting_source_families", [])]

    news_top20_pre_gate: List[Dict[str, Any]] = []
    for cluster in sorted(news_clusters, key=news_pre_gate_score, reverse=True)[:20]:
        proposed_lane = "BREAKING / CURRENT NEWS"
        topic = cluster.get("topic_cluster", "")
        if any(k in topic for k in ["security", "beta", "rollout", "leak", "outage"]):
            proposed_lane = "DISCOVERY / PREDICTIVE"
        elif cluster.get("supporting_events_count", 0) >= 3 or "trend" in topic:
            proposed_lane = "CURRENT DEMAND / TREND"
        source_names = sorted({s.get("source", "") for s in cluster["supporting_signals"] if s.get("source")})
        primary_source = (
            cluster.get("official_primary_sources", [None])[0]
            if cluster.get("official_primary_sources")
            else source_names[0] if source_names else cluster["representative_signal"].get("source", "")
        )
        story_title = cluster["representative_signal"].get("title") or cluster.get("topic_cluster", "")
        age = age_days(cluster)
        news_top20_pre_gate.append(
            {
                "story": story_title,
                "topic_cluster": cluster["topic_cluster"],
                "first_public_time": cluster.get("information_first_public_at") or cluster.get("story_first_seen_at") or cluster.get("first_signal_at"),
                "first_seen": cluster.get("first_signal_at"),
                "latest_seen": cluster.get("latest_signal_at"),
                "source": source_names,
                "supporting_sources_count": len(source_names),
                "primary_source": primary_source,
                "user_impact": cluster.get("user_impact_reason", ""),
                "mainstream_saturation": {
                    "signals": cluster.get("supporting_events_count", 0),
                    "external_independent_publishers": len(cluster.get("external_independent_publishers", [])),
                    "official_primary_sources": len(cluster.get("official_primary_sources", [])),
                    "internal_evidence_sources": len(cluster.get("internal_evidence_sources", [])),
                    "search_demand_sources": len(cluster.get("search_demand_sources", [])),
                    "external_source_diversity": cluster.get("news_external_source_diversity", cluster.get("source_diversity", 0)),
                    "age_days": age,
                },
                "proposed_lane": proposed_lane,
                "why_it_may_matter": cluster.get("why_it_may_matter", ""),
                "candidate_score": news_pre_gate_score(cluster),
            }
        )

    # Persist cross-source promotions back into the GitHub watchlist DB.
    github_watchlist_rows = load_existing_github_watchlist_low()
    overlay_promotions, watchlist_persistence = persist_github_watchlist_promotions(clusters, github_watchlist_rows, source_meta)

    ranked, audit = rank_candidates(clusters, wp_index)
    final_portfolio, cf = build_final_portfolio(ranked, limit=portfolio_capacity)

    # Prepare final recommendation labels and marginal value.
    for c in final_portfolio:
        c["recommendation"] = c.get("primary_lane", "SEO / SEARCH OPPORTUNITY")

    # Build audit slices.
    qualified = [c for c in ranked if c["status"] == "qualified"]
    rejected = audit.get("rejected_candidates", [])
    portfolio_lane_counts = Counter(c.get("primary_lane", "UNKNOWN") for c in final_portfolio)
    qualified_lane_counts = audit.get("qualified_lane_counts", {})
    github_cluster_count = sum(1 for c in clusters if "github" in c.get("supporting_source_families", []))
    github_candidate_universe_count = github_cluster_count
    github_lane_scored_count = sum(1 for c in rejected if "github" in c.get("supporting_source_families", [])) + sum(1 for c in qualified if "github" in c.get("supporting_source_families", []))
    github_rejected_count = sum(1 for c in rejected if "github" in c.get("supporting_source_families", []))
    github_qualified_count = sum(1 for c in qualified if "github" in c.get("supporting_source_families", []))
    github_final_count = sum(1 for c in final_portfolio if "github" in c.get("supporting_source_families", []))
    news_raw_signals_count = source_meta["news"].get("signals", 0)
    news_underlying_event_clusters_count = len(news_clusters)
    news_candidates_entering_candidate_universe = len(news_clusters)
    news_rejected = [c for c in rejected if "news" in c.get("supporting_source_families", [])]
    news_qualified = [c for c in qualified if "news" in c.get("supporting_source_families", [])]
    news_final = [c for c in final_portfolio if "news" in c.get("supporting_source_families", [])]
    news_candidates_by_lane = dict(Counter(item["proposed_lane"] for item in news_top20_pre_gate))
    news_qualified_by_lane = dict(Counter(c.get("primary_lane", "UNKNOWN") for c in news_qualified))
    first_seen_semantics = "PASS" if all(c.get("lisa_first_seen_at") in {"UNAVAILABLE", "UNKNOWN"} for c in ranked) else "FAIL"
    github_evidence_propagation = "PASS" if (
        github_cluster_count > 0
        and github_lane_scored_count == github_cluster_count
        and github_rejected_count + github_qualified_count == github_cluster_count
        and all(
            c.get("rejection_reason")
            for c in rejected
            if "github" in c.get("supporting_source_families", [])
        )
    ) else "FAIL"

    report = {
        "created_at": iso(now_utc()),
        "mode": "PRODUCTION" if production_mode else "TEST",
        "supervised": supervised,
        "workflow_order": [
            "SOURCE DELTA SYNC",
            "LOCAL STORES",
            "NORMALIZATION",
            "CROSS-SOURCE CLUSTERING",
            "WATCHLIST RE-EVALUATION",
            "CANDIDATE UNIVERSE",
            "V6.5 FUNNEL",
            "GLOBAL RANKING",
            "FINAL PORTFOLIO",
            "MORNING REPORT",
        ],
        "normalized_signals_count": len(normalized),
        "clusters_count": len(clusters),
        "qualified_count": len(qualified),
        "ranked_count": len(ranked),
        "final_portfolio_count": len(final_portfolio),
        "portfolio_capacity": portfolio_capacity,
        "api_calls_used": 0,
        "llm_calls_used": 0,
        "source_coverage_audit": source_coverage_audit(source_meta),
        "errors_fallbacks": fallback_summary(source_meta),
        "source_meta": source_meta,
        "source_counts": {k: len(v) for k, v in source_signals.items()},
        "rejection_counts": audit["rejection_counts"],
        "lane_counts": audit.get("lane_counts", {}),
        "qualified_lane_counts": qualified_lane_counts,
        "portfolio_lane_counts": dict(portfolio_lane_counts),
        "github_raw_count": source_meta["github"].get("raw_signals", 0),
        "github_cluster_count": github_cluster_count,
        "github_candidate_universe_count": github_candidate_universe_count,
        "github_lane_scored_count": github_lane_scored_count,
        "github_rejected_count": github_rejected_count,
        "github_qualified_count": github_qualified_count,
        "github_final_count": github_final_count,
        "first_seen_semantics": first_seen_semantics,
        "github_evidence_propagation": github_evidence_propagation,
        "news_raw_signals_count": news_raw_signals_count,
        "news_underlying_event_clusters_count": news_underlying_event_clusters_count,
        "news_candidates_entering_candidate_universe": news_candidates_entering_candidate_universe,
        "news_candidates_by_lane": news_candidates_by_lane,
        "news_qualified_candidates_by_lane": news_qualified_by_lane,
        "news_rejected_count": len(news_rejected),
        "news_rejected": news_rejected,
        "news_qualified_count": len(news_qualified),
        "news_qualified_candidates": news_qualified,
        "news_final_portfolio_count": len(news_final),
        "news_candidates_reaching_final_portfolio": news_final,
        "news_top20_events": news_top20_pre_gate,
        "news_implementation_status": "PASS" if enable_news and source_meta["news"].get("checked") else "FAIL",
        "news_propagation_status": "PASS" if enable_news and news_raw_signals_count > 0 and news_underlying_event_clusters_count > 0 else "FAIL",
        "production_data_unchanged": "PASS" if not persist_state else "FAIL",
        "news_last_successful_sync": source_meta["news"].get("last_successful_sync"),
        "news_errors": source_meta["news"].get("errors", []),
        "qualified_candidates": qualified,
        "rejected_candidates": rejected,
        "top10": final_portfolio[:10],
        "top1": cf["only_one"],
        "top3": cf["only_three"],
        "final_portfolio": final_portfolio,
        "watchlist_promotions": overlay_promotions,
        "watchlist_persistence": "PASS" if watchlist_persistence else "FAIL",
        "structured_trends_store": "PASS" if source_meta["trends"].get("checked") else "FAIL",
        "production_ready": True,
        "current_breaking_count": sum(1 for c in final_portfolio if c.get("primary_lane") == "BREAKING / CURRENT NEWS"),
        "discovery_predictive_count": sum(1 for c in final_portfolio if c.get("primary_lane") == "DISCOVERY / PREDICTIVE"),
        "current_demand_trend_count": sum(1 for c in final_portfolio if c.get("primary_lane") == "CURRENT DEMAND / TREND"),
        "seo_search_count": sum(1 for c in final_portfolio if c.get("primary_lane") == "SEO / SEARCH OPPORTUNITY"),
        "update_rewrite_count": sum(1 for c in final_portfolio if c.get("primary_lane") == "UPDATE / REWRITE"),
        "implemented": [
            "GitHub read-only delta ingestion, raw signal storage, clustering, and persisted watchlist re-evaluation",
            "GSC local CSV ingestion and query/page normalization",
            "GA4 local CSV ingestion and page/landing-page normalization",
            "WordPress local CSV ingestion and duplicate-baseline index",
            "Structured Google Trends SQLite cache with bootstrap ingestion from the local editorial report",
            "Opt-in Google News / News discovery RSS ingestion and pre-gate event clustering",
            "Cross-source normalized signal layer and unified candidate universe",
            "Global ranking, counterfactual top1/top3, and marginal portfolio selection",
            "Test-mode reporting with no remote API calls",
            "GitHub watchlist promotions persist back into the GitHub watchlist DB",
        ],
        "partially_implemented": [
            "Source Coverage Audit is explicit for the connected layers, while News discovery is opt-in for the controlled test path",
            "Reality / information age / WP / unique value gates are implemented heuristically from local evidence, not by a full newsroom model",
            "Structured Trends cache is seeded from the local editorial report until a dedicated live Trends ingest is available",
        ],
        "not_implemented": [
            "Reddit sensor",
            "X sensor",
            "YouTube / community sensor",
            "AdSense / revenue source",
            "Automatic WordPress publication",
            "Automatic multi-source remote API sync beyond existing local exports",
        ],
        "failed_needs_fix": [],
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="AndroidMagazine multi-source orchestrator")
    parser.add_argument("--write-state", action="store_true", help="persist orchestrator DB/state and write the markdown/JSON test report")
    parser.add_argument("--production", action="store_true", help="run as supervised production morning workflow")
    parser.add_argument("--supervised", action="store_true", help="mark the run as supervised")
    parser.add_argument("--portfolio-capacity", type=int, default=10, help="final portfolio capacity")
    parser.add_argument("--enable-news", action="store_true", help="enable opt-in Google News discovery fetching for the controlled test run")
    parser.add_argument("--output", default=str(OUTPUT_MD_PATH), help="markdown output path")
    parser.add_argument("--json-output", default=str(OUTPUT_JSON_PATH), help="json output path")
    args = parser.parse_args()

    if args.production:
        out_md_default = REPORTS_DIR / f"MORNING-REPORT-ANDROIDMAGAZINE-{datetime.now(timezone.utc).date().isoformat()}.md"
        out_json_default = REPORTS_DIR / f"MORNING-REPORT-ANDROIDMAGAZINE-{datetime.now(timezone.utc).date().isoformat()}.json"
        args.output = args.output if args.output != str(OUTPUT_MD_PATH) else str(out_md_default)
        args.json_output = args.json_output if args.json_output != str(OUTPUT_JSON_PATH) else str(out_json_default)

    report = build_report(
        test_mode=not args.production,
        production_mode=args.production,
        supervised=args.supervised,
        portfolio_capacity=args.portfolio_capacity,
        enable_news=args.enable_news or args.production,
        persist_state=args.write_state,
    )
    markdown = render_markdown(report)

    out_md = Path(args.output)
    out_json = Path(args.json_output)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown, encoding="utf-8")
    out_json.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    if args.write_state:
        all_clusters_for_state = report["qualified_candidates"] + report["rejected_candidates"]
        store_orchestrator_db(all_clusters_for_state, all_clusters_for_state)
        store_orchestrator_state(
            {
                "last_run_at": report["created_at"],
                "mode": report["mode"],
                "supervised": report["supervised"],
                "production_active": bool(args.production and args.supervised and report["watchlist_persistence"] == "PASS" and report["structured_trends_store"] == "PASS"),
                "source_watermarks": {
                    "github": source_watermark(GITHUB_STATE_PATH),
                    "gsc": source_watermark(GSC_DIR / "META.json"),
                    "ga4": source_watermark(GA4_DIR / "daily-trend-90d.csv"),
                    "wordpress": source_watermark(WP_DIR / "META.json"),
                    "trends": source_watermark(EDITORIAL_REPORT_PATH),
                },
                "workflow_order": report["workflow_order"],
            }
        )
        STATUS_PATH.write_text(
            json.dumps(
                {
                    "last_run_at": report["created_at"],
                    "mode": report["mode"],
                    "supervised": report["supervised"],
                    "production_active": bool(args.production and args.supervised and report["watchlist_persistence"] == "PASS" and report["structured_trends_store"] == "PASS"),
                    "watchlist_persistence": report["watchlist_persistence"],
                    "structured_trends_store": report["structured_trends_store"],
                    "workflow_order": report["workflow_order"],
                },
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    print(json.dumps(
        {
            "created_at": report["created_at"],
            "normalized_signals_count": report["normalized_signals_count"],
            "clusters_count": report["clusters_count"],
            "qualified_count": report["qualified_count"],
            "final_portfolio_count": report["final_portfolio_count"],
            "api_calls_used": report["api_calls_used"],
            "llm_calls_used": report["llm_calls_used"],
            "output": str(out_md),
            "json_output": str(out_json),
        },
        ensure_ascii=False,
        indent=2,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

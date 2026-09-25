#!/usr/bin/env python3
import base64
import csv
import datetime as dt
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build


SITE = "letemsvetemapplem.eu"
WP_BASE = "https://www.letemsvetemapplem.eu"
GA4_PROPERTY = "361706440"
GSC_SITE = "sc-domain:letemsvetemapplem.eu"
ROOT = Path("/Users/lisa/.openclaw/workspace")
REPORTS_DIR = ROOT / "reports"
MAG_DIR = ROOT / "magazines" / "letemsvetemapplem"
GA4_DIR = MAG_DIR / "analytics" / "ga4"
GSC_DIR = MAG_DIR / "analytics" / "gsc"
WP_DIR = MAG_DIR / "wordpress"
TODAY = dt.date.today()
END_DATE = TODAY - dt.timedelta(days=1)
START_DATE = dt.date(2025, 5, 1)

GENERIC_CATEGORY_NAMES = {
    "Vše o Apple",
    "Bleskovky",
    "Top články",
    "Galerie",
    "Ověřeno šéfredaktorem",
    "Tiskové zprávy",
}

NOISE_SLUG_PARTS = {
    "forum",
    "live-text",
    "soutez",
}

LOCALE_SEGMENTS = {
    "ja",
    "it",
    "ru",
    "es",
    "de",
    "fr",
    "pt",
    "pl",
    "hu",
    "sk",
    "en",
}

TOPIC_RULES = [
    (
        "Lego a sběratelství",
        [
            r"\blego\b",
            r"\bstar destroyer\b",
            r"\bpán[a-z]* prsten[uoa]?\b",
            r"\bhelmov",
            r"\bucs\b",
            r"\bplaystation 1\b",
        ],
        {"Lego a sběratelství"},
    ),
    (
        "Historie a retro",
        [
            r"steve jobs",
            r"apple historie",
            r"\bhistorie\b",
            r"nostalg",
            r"sony ericsson",
            r"nokia",
            r"retro",
            r"v detstvi",
            r"v dětství",
        ],
        {"Apple Historie"},
    ),
    (
        "Návody a řešení problémů",
        [
            r"^jak\b",
            r"\bnávod\b",
            r"\btip\b",
            r"\btrik\b",
            r"\bpostup\b",
            r"\bvypnout\b",
            r"\bzapnout\b",
            r"\bnastavit\b",
            r"\bopravit\b",
            r"\bnefunguje\b",
            r"\bvyřešit\b",
            r"\bco dělat\b",
            r"\bco delat\b",
            r"\bjak zjistit\b",
            r"\bjak stáhnout\b",
            r"\bjak stahnout\b",
        ],
        {"Návody", "Aplikace ZDARMA"},
    ),
    (
        "Aplikace a služby",
        [
            r"\bapp store\b",
            r"\baplikac",
            r"\bspotify\b",
            r"\bwhatsapp\b",
            r"\binstagram\b",
            r"\bfacebook\b",
            r"\bnetflix\b",
            r"\bicloud\b",
            r"\bapple music\b",
            r"\bapple tv\+\b",
            r"\bsafari\b",
            r"\bmail\b",
            r"\bmaps\b",
            r"\bimessage\b",
            r"\bfacetime\b",
            r"\bsiri\b",
            r"\bchatgpt\b",
            r"\bgemini\b",
        ],
        {"Aplikace ZDARMA"},
    ),
    (
        "Apple Watch",
        [
            r"apple watch",
            r"\bwatchos\b",
            r"\bultra 4\b",
            r"\bwatch 12\b",
        ],
        {"Apple Watch"},
    ),
    (
        "Mac a macOS",
        [
            r"\bmacbook\b",
            r"\bimac\b",
            r"\bmac mini\b",
            r"\bmac pro\b",
            r"\bmac studio\b",
            r"\bmacos\b",
            r"\bm1\b",
            r"\bm2\b",
            r"\bm3\b",
            r"\bm4\b",
            r"\bm5\b",
            r"\bm6\b",
        ],
        {"Mac"},
    ),
    (
        "iPad",
        [
            r"\bipad\b",
            r"\bipados\b",
        ],
        {"iPad"},
    ),
    (
        "AirPods a audio",
        [
            r"\bairpods\b",
            r"\bearpods\b",
            r"\bbeats\b",
            r"\bhomepod\b",
        ],
        {"Apple TV"},
    ),
    (
        "Apple TV a video",
        [
            r"\bapple tv\b",
            r"\bappletv\b",
            r"\btvos\b",
        ],
        {"Apple TV"},
    ),
    (
        "Vision Pro a XR",
        [
            r"vision pro",
            r"\bvisionos\b",
            r"\bxr\b",
            r"\bvr\b",
            r"\bar\b",
        ],
        {"Apple Vision Pro"},
    ),
    (
        "iPhone a iOS",
        [
            r"\biphone\b",
            r"\bios\b",
            r"\bface id\b",
            r"\bdynamic island\b",
            r"\biphone se\b",
        ],
        {"iPhone"},
    ),
    (
        "Recenze",
        [
            r"\brecenze\b",
            r"\breview\b",
            r"\btest\b",
        ],
        {"Recenze"},
    ),
    (
        "Slevy a nákupy",
        [
            r"\bzdarma\b",
            r"\bsleva\b",
            r"\bzlevn",
            r"\bakce\b",
            r"\balza\b",
            r"\bnejlev",
            r"\bcena\b",
            r"\bjen pro čr\b",
            r"\bjen pro cr\b",
        ],
        {"Jen pro ČR"},
    ),
]

FORMAT_RULES = [
    ("Návod", [r"^jak\b", r"\bnávod\b", r"\bpostup\b", r"\btip\b", r"\btrik\b", r"\bvypnout\b", r"\bnastavit\b"]),
    ("Spekulace a úniky", [r"\bunik", r"\búnik", r"\bočekává", r"\bocekava", r"\bchystá", r"\bchysta", r"\bprý\b", r"\bmožná\b", r"\bmozna\b", r"\bdatum\b", r"\brender"]),
    ("Novinka", [r"\bpředstavil", r"\bpredstavil", r"\boznám", r"\boznam", r"\bvydal", r"\bspustil", r"\bpřináší", r"\bprichazi", r"\bnovink"]),
    ("Sleva", [r"\bzdarma\b", r"\bsleva\b", r"\bzlevn", r"\bakce\b", r"\balza\b"]),
    ("Recenze", [r"\brecenze\b", r"\breview\b", r"\btest\b"]),
    ("Komentář a historie", [r"steve jobs", r"\bhistorie\b", r"nostalg", r"retro"]),
]


def load_env():
    with open(os.path.expanduser("~/.openclaw/openclaw.json")) as f:
        cfg = json.load(f)
    env = cfg.get("env", {})
    return env, env.get("vars", {})


ENV, ENV_VARS = load_env()


def get_env(name, default=""):
    return ENV.get(name) or ENV_VARS.get(name) or default


for key in [
    "WP_LSA_URL",
    "WP_LSA_USER",
    "WP_LSA_PASS",
]:
    if get_env(key):
        os.environ[key] = get_env(key)


def ensure_dirs():
    for path in (REPORTS_DIR, GA4_DIR, GSC_DIR, WP_DIR):
        path.mkdir(parents=True, exist_ok=True)


def service_account_path():
    candidates = [
        Path(os.path.expanduser("~/.openclaw/creds/android-magazine-sa.json")),
        Path(os.path.expanduser("~/.openclaw/workspace/android-magazine-sa.json")),
    ]
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(f"Missing service account file: {candidates}")


def build_services():
    sa_path = str(service_account_path())
    ga4_creds = service_account.Credentials.from_service_account_file(
        sa_path, scopes=["https://www.googleapis.com/auth/analytics.readonly"]
    )
    gsc_creds = service_account.Credentials.from_service_account_file(
        sa_path, scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    ga4 = build("analyticsdata", "v1beta", credentials=ga4_creds, cache_discovery=False)
    gsc = build("searchconsole", "v1", credentials=gsc_creds, cache_discovery=False)
    return ga4, gsc


def request_json(url, headers=None, timeout=30):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())


def log(message):
    print(message, flush=True)


def wp_headers():
    user = get_env("WP_LSA_USER", "Lisa")
    password = get_env("WP_LSA_PASS")
    if not password:
        raise RuntimeError("WP_LSA_PASS missing")
    token = base64.b64encode(f"{user}:{password}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def month_ranges(start_date, end_date):
    cursor = dt.date(start_date.year, start_date.month, 1)
    last = dt.date(end_date.year, end_date.month, 1)
    ranges = []
    while cursor <= last:
        if cursor.month == 12:
            next_month = dt.date(cursor.year + 1, 1, 1)
        else:
            next_month = dt.date(cursor.year, cursor.month + 1, 1)
        month_end = min(end_date, next_month - dt.timedelta(days=1))
        month_start = max(start_date, cursor)
        ranges.append((month_start, month_end))
        cursor = next_month
    return ranges


def clean_text(text):
    text = html.unescape(text or "")
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def normalize_path(url_or_path):
    if not url_or_path:
        return ""
    parsed = urllib.parse.urlparse(url_or_path)
    path = parsed.path if parsed.scheme else url_or_path
    path = urllib.parse.unquote(path or "")
    if not path.startswith("/"):
        path = "/" + path
    path = re.sub(r"/{2,}", "/", path)
    if not path.endswith("/"):
        path += "/"
    parts = [part for part in path.split("/") if part]
    if parts and parts[0].lower() in LOCALE_SEGMENTS:
        parts = parts[1:]
    path = "/" + "/".join(parts) + "/"
    path = re.sub(r"/{2,}", "/", path)
    return path


def is_article_path(path):
    if not path:
        return False
    if any(part in path for part in ("/tag/", "/category/", "/author/", "/page/")):
        return False
    if any(part in path for part in ("/wp-content/", "/feed/", "/amp/")):
        return False
    parts = [part for part in path.split("/") if part]
    if not parts:
        return False
    if parts[0] in LOCALE_SEGMENTS:
        parts = parts[1:]
    if len(parts) < 4:
        return False
    if not all(p.isdigit() for p in parts[:3]):
        return False
    if any(noise in parts[3] for noise in NOISE_SLUG_PARTS):
        return False
    return True


def choose_primary_category(category_names):
    usable = [name for name in category_names if name not in GENERIC_CATEGORY_NAMES]
    if "Návody" in usable:
        return "Návody a řešení problémů"
    if "Apple Historie" in usable:
        return "Historie a retro"
    if "Aplikace ZDARMA" in usable:
        return "Aplikace a služby"
    priority = [
        "iPhone",
        "Mac",
        "iPad",
        "Apple Watch",
        "Apple TV",
        "Apple Vision Pro",
        "Recenze",
        "Jen pro ČR",
    ]
    for name in priority:
        if name in usable:
            mapping = {
                "iPhone": "iPhone a iOS",
                "Mac": "Mac a macOS",
                "iPad": "iPad",
                "Apple Watch": "Apple Watch",
                "Apple TV": "Apple TV a video",
                "Apple Vision Pro": "Vision Pro a XR",
                "Recenze": "Recenze",
                "Jen pro ČR": "Slevy a nákupy",
            }
            return mapping[name]
    return ""


def match_rule(text, category_names, rules):
    text_l = text.lower()
    category_names = set(category_names)
    for label, patterns, categories in rules:
        if categories.intersection(category_names):
            return label
        for pattern in patterns:
            if re.search(pattern, text_l):
                return label
    return ""


def infer_topic(title, slug, category_names):
    text = f"{title} {slug}"
    chosen = choose_primary_category(category_names)
    if chosen:
        return chosen
    chosen = match_rule(text, category_names, TOPIC_RULES)
    return chosen or "Ostatní Apple / mix"


def infer_format(title, slug, category_names):
    if "Návody" in category_names:
        return "Návod"
    text = f"{title} {slug}".lower()
    for label, patterns in FORMAT_RULES:
        if any(re.search(pattern, text) for pattern in patterns):
            return label
    return "Běžná novinka"


def fetch_categories():
    log("WP categories: start")
    headers = wp_headers()
    category_map = {}
    page = 1
    total_pages = None
    while True:
        query = urllib.parse.urlencode(
            {
                "per_page": 100,
                "page": page,
                "_fields": "id,name,parent,count",
                "orderby": "id",
                "order": "asc",
            }
        )
        req = urllib.request.Request(f"{WP_BASE}/wp-json/wp/v2/categories?{query}", headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            rows = json.loads(resp.read())
            if total_pages is None:
                total_pages = int(resp.headers.get("X-WP-TotalPages", "1"))
        for row in rows:
            category_map[row["id"]] = row["name"]
        page += 1
        if total_pages and page > total_pages:
            break
        time.sleep(0.1)
    log(f"WP categories: done ({len(category_map)})")
    return category_map


def fetch_posts(category_map):
    log("WP posts: start")
    headers = wp_headers()
    posts = []
    page = 1
    total_pages = None
    while True:
        query = urllib.parse.urlencode(
            {
                "per_page": 100,
                "page": page,
                "status": "publish",
                "orderby": "date",
                "order": "desc",
                "after": f"{START_DATE.isoformat()}T00:00:00",
                "_fields": "id,date,slug,link,title,categories",
            }
        )
        req = urllib.request.Request(f"{WP_BASE}/wp-json/wp/v2/posts?{query}", headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            rows = json.loads(resp.read())
            if total_pages is None:
                total_pages = int(resp.headers.get("X-WP-TotalPages", "1"))
        if not rows:
            break
        for row in rows:
            path = normalize_path(row.get("link", ""))
            if not is_article_path(path):
                continue
            categories = [category_map.get(cat_id, str(cat_id)) for cat_id in row.get("categories", [])]
            title = clean_text(row.get("title", {}).get("rendered", ""))
            slug = row.get("slug", "")
            post_date = dt.datetime.fromisoformat(row["date"]).date()
            posts.append(
                {
                    "post_id": row["id"],
                    "date": post_date.isoformat(),
                    "path": path,
                    "title": title,
                    "slug": slug,
                    "categories": categories,
                    "topic": infer_topic(title, slug, categories),
                    "format": infer_format(title, slug, categories),
                }
            )
        page += 1
        if page % 10 == 0:
            log(f"WP posts: page {page - 1}/{total_pages or '?'} ({len(posts)} posts kept)")
        if total_pages and page > total_pages:
            break
        time.sleep(0.1)
    log(f"WP posts: done ({len(posts)})")
    return posts


def ga4_date_str(d):
    return d.isoformat()


def fetch_ga4_month(ga4, start_date, end_date):
    rows = []
    offset = 0
    limit = 100000
    total_row_count = None
    while True:
        body = {
            "dateRanges": [{"startDate": ga4_date_str(start_date), "endDate": ga4_date_str(end_date)}],
            "dimensions": [{"name": "landingPage"}],
            "metrics": [
                {"name": "sessions"},
                {"name": "activeUsers"},
                {"name": "screenPageViews"},
                {"name": "engagementRate"},
                {"name": "averageSessionDuration"},
            ],
            "dimensionFilter": {
                "filter": {
                    "fieldName": "landingPage",
                    "stringFilter": {
                        "matchType": "FULL_REGEXP",
                        "value": "^/([a-z]{2}/)?[0-9]{4}/[0-9]{2}/[0-9]{2}/.*",
                    },
                }
            },
            "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}],
            "limit": limit,
            "offset": offset,
        }
        resp = ga4.properties().runReport(property=f"properties/{GA4_PROPERTY}", body=body).execute()
        if total_row_count is None:
            total_row_count = resp.get("rowCount", 0)
        chunk = resp.get("rows", [])
        if not chunk:
            break
        rows.extend(chunk)
        offset += len(chunk)
        if len(chunk) < limit or offset >= total_row_count:
            break
    return {
        "rows": rows,
        "rowCount": total_row_count or 0,
        "dataLossFromOtherRow": resp.get("metadata", {}).get("dataLossFromOtherRow", False),
    }


def fetch_ga4(ga4):
    log("GA4: start")
    page_metrics = defaultdict(lambda: defaultdict(float))
    month_meta = []
    for start_date, end_date in month_ranges(START_DATE, END_DATE):
        log(f"GA4: {start_date:%Y-%m} start")
        payload = fetch_ga4_month(ga4, start_date, end_date)
        month_meta.append(
            {
                "month": start_date.strftime("%Y-%m"),
                "row_count": payload["rowCount"],
                "data_loss_from_other": payload["dataLossFromOtherRow"],
                "retrieved_rows": len(payload["rows"]),
            }
        )
        for row in payload["rows"]:
            path = normalize_path(row["dimensionValues"][0]["value"])
            if not is_article_path(path):
                continue
            values = row["metricValues"]
            sessions = float(values[0]["value"])
            active_users = float(values[1]["value"])
            page_views = float(values[2]["value"])
            engagement_rate = float(values[3]["value"])
            avg_session_duration = float(values[4]["value"])
            page_metrics[path]["sessions"] += sessions
            page_metrics[path]["active_users"] += active_users
            page_metrics[path]["page_views"] += page_views
            page_metrics[path]["engagement_rate_weighted"] += engagement_rate * sessions
            page_metrics[path]["avg_session_duration_weighted"] += avg_session_duration * sessions
        log(
            f"GA4: {start_date:%Y-%m} done rows={len(payload['rows'])} rowCount={payload['rowCount']} "
            f"other={payload['dataLossFromOtherRow']}"
        )
        time.sleep(0.2)
    for metrics in page_metrics.values():
        sessions = metrics["sessions"] or 1.0
        metrics["engagement_rate"] = metrics["engagement_rate_weighted"] / sessions
        metrics["avg_session_duration"] = metrics["avg_session_duration_weighted"] / sessions
    log(f"GA4: done ({len(page_metrics)} paths)")
    return page_metrics, month_meta


def fetch_gsc_dimension(gsc, dimension):
    log(f"GSC {dimension}: start")
    totals = defaultdict(lambda: defaultdict(float))
    month_meta = []
    for start_date, end_date in month_ranges(START_DATE, END_DATE):
        start_row = 0
        month_rows = 0
        pages = 0
        log(f"GSC {dimension}: {start_date:%Y-%m} start")
        while True:
            body = {
                "startDate": start_date.isoformat(),
                "endDate": end_date.isoformat(),
                "dimensions": [dimension],
                "rowLimit": 25000,
                "startRow": start_row,
                "dataState": "final",
            }
            resp = gsc.searchanalytics().query(siteUrl=GSC_SITE, body=body).execute()
            rows = resp.get("rows", [])
            if not rows:
                break
            month_rows += len(rows)
            pages += 1
            for row in rows:
                key = row["keys"][0]
                if dimension == "page":
                    key = normalize_path(key)
                    if not is_article_path(key):
                        continue
                totals[key]["clicks"] += float(row.get("clicks", 0.0))
                totals[key]["impressions"] += float(row.get("impressions", 0.0))
                totals[key]["position_weighted"] += float(row.get("position", 0.0)) * float(row.get("impressions", 0.0))
            if len(rows) < 25000:
                break
            start_row += 25000
            log(f"GSC {dimension}: {start_date:%Y-%m} fetched {month_rows} rows so far")
        month_meta.append({"month": start_date.strftime("%Y-%m"), "dimension": dimension, "rows": month_rows})
        log(f"GSC {dimension}: {start_date:%Y-%m} done rows={month_rows} pages={pages}")
        time.sleep(0.2)
    for values in totals.values():
        impressions = values["impressions"] or 1.0
        values["ctr"] = values["clicks"] / impressions
        values["position"] = values["position_weighted"] / impressions
    log(f"GSC {dimension}: done ({len(totals)} keys)")
    return totals, month_meta


def query_topic(query):
    text = query.lower()
    if re.search(r"\blego\b|\bstar destroyer\b|\bhelmov|\bpán[a-z]* prsten", text):
        return "Lego a sběratelství"
    if re.search(r"steve jobs|nostalg|retro|sony ericsson|nokia", text):
        return "Historie a retro"
    if re.search(r"^jak\b|návod|vypnout|zapnout|nastavit|nefunguje|stáhnout|stahnout|co dělat|co delat", text):
        return "Návody a řešení problémů"
    if re.search(r"apple watch|watchos|ultra 4|watch 12", text):
        return "Apple Watch"
    if re.search(r"macbook|imac|mac mini|mac pro|mac studio|macos|\bm[1-6]\b", text):
        return "Mac a macOS"
    if re.search(r"\bipad\b|\bipados\b", text):
        return "iPad"
    if re.search(r"airpods|earpods|beats|homepod", text):
        return "AirPods a audio"
    if re.search(r"apple tv|appletv|tvos", text):
        return "Apple TV a video"
    if re.search(r"vision pro|visionos|\bxr\b|\bvr\b|\bar\b", text):
        return "Vision Pro a XR"
    if re.search(r"app store|icloud|spotify|whatsapp|instagram|facebook|netflix|apple music|siri|chatgpt|gemini", text):
        return "Aplikace a služby"
    if re.search(r"iphone|ios|face id|dynamic island", text):
        return "iPhone a iOS"
    if re.search(r"recenze|review|test", text):
        return "Recenze"
    if re.search(r"zdarma|sleva|zlevn|akce|alza|cena", text):
        return "Slevy a nákupy"
    return "Ostatní Apple / mix"


def write_csv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def to_int(v):
    return int(round(v or 0))


def pct(v):
    return round((v or 0) * 100, 1)


def aggregate(posts, ga4_pages, gsc_pages, gsc_queries):
    posts_by_path = {post["path"]: post for post in posts}
    topic_stats = defaultdict(lambda: defaultdict(float))
    format_stats = defaultdict(lambda: defaultdict(float))
    page_rows = []

    for post in posts:
        path = post["path"]
        topic = post["topic"]
        fmt = post["format"]
        ga = ga4_pages.get(path, {})
        gs = gsc_pages.get(path, {})
        page_row = {
            "path": path,
            "title": post["title"],
            "date": post["date"],
            "topic": topic,
            "format": fmt,
            "categories": " | ".join(post["categories"]),
            "ga4_sessions": to_int(ga.get("sessions", 0)),
            "ga4_page_views": to_int(ga.get("page_views", 0)),
            "ga4_active_users": to_int(ga.get("active_users", 0)),
            "ga4_engagement_rate": round(ga.get("engagement_rate", 0.0), 4),
            "ga4_avg_session_duration": round(ga.get("avg_session_duration", 0.0), 1),
            "gsc_clicks": to_int(gs.get("clicks", 0)),
            "gsc_impressions": to_int(gs.get("impressions", 0)),
            "gsc_ctr": round(gs.get("ctr", 0.0), 4),
            "gsc_position": round(gs.get("position", 0.0), 2),
        }
        page_rows.append(page_row)

        for bucket, label in ((topic_stats, topic), (format_stats, fmt)):
            bucket[label]["posts"] += 1
            bucket[label]["ga4_sessions"] += ga.get("sessions", 0)
            bucket[label]["ga4_page_views"] += ga.get("page_views", 0)
            bucket[label]["ga4_active_users"] += ga.get("active_users", 0)
            bucket[label]["ga4_engagement_rate_weighted"] += ga.get("engagement_rate", 0) * ga.get("sessions", 0)
            bucket[label]["ga4_avg_session_duration_weighted"] += ga.get("avg_session_duration", 0) * ga.get("sessions", 0)
            bucket[label]["gsc_clicks"] += gs.get("clicks", 0)
            bucket[label]["gsc_impressions"] += gs.get("impressions", 0)
            bucket[label]["gsc_position_weighted"] += gs.get("position", 0) * gs.get("impressions", 0)

    for query, values in gsc_queries.items():
        topic = query_topic(query)
        topic_stats[topic]["query_clicks"] += values["clicks"]
        topic_stats[topic]["query_impressions"] += values["impressions"]
        topic_stats[topic]["query_position_weighted"] += values["position"] * values["impressions"]

    def finalize(bucket):
        rows = []
        total_sessions = sum(v["ga4_sessions"] for v in bucket.values()) or 1.0
        total_clicks = sum(v["gsc_clicks"] for v in bucket.values()) or 1.0
        total_query_impressions = sum(v["query_impressions"] for v in bucket.values()) or 1.0
        for label, values in bucket.items():
            posts_count = values["posts"] or 0.0
            sessions = values["ga4_sessions"]
            clicks = values["gsc_clicks"]
            query_impr = values["query_impressions"]
            row = {
                "label": label,
                "posts": to_int(posts_count),
                "ga4_sessions": to_int(sessions),
                "ga4_page_views": to_int(values["ga4_page_views"]),
                "ga4_active_users": to_int(values["ga4_active_users"]),
                "ga4_share": sessions / total_sessions,
                "ga4_sessions_per_post": sessions / posts_count if posts_count else 0.0,
                "ga4_engagement_rate": (values["ga4_engagement_rate_weighted"] / sessions) if sessions else 0.0,
                "ga4_avg_session_duration": (values["ga4_avg_session_duration_weighted"] / sessions) if sessions else 0.0,
                "gsc_clicks": to_int(clicks),
                "gsc_impressions": to_int(values["gsc_impressions"]),
                "gsc_share": clicks / total_clicks,
                "gsc_clicks_per_post": clicks / posts_count if posts_count else 0.0,
                "gsc_position": (values["gsc_position_weighted"] / values["gsc_impressions"]) if values["gsc_impressions"] else 0.0,
                "query_clicks": to_int(values["query_clicks"]),
                "query_impressions": to_int(query_impr),
                "query_impression_share": query_impr / total_query_impressions,
                "query_position": (values["query_position_weighted"] / query_impr) if query_impr else 0.0,
            }
            rows.append(row)
        return rows

    topic_rows = finalize(topic_stats)
    format_rows = finalize(format_stats)

    return page_rows, topic_rows, format_rows


def rank_rows(rows, volume_floor):
    eligible = [row for row in rows if row["posts"] >= volume_floor]
    if not eligible:
        return []
    max_sessions = max(row["ga4_sessions_per_post"] for row in eligible) or 1.0
    max_clicks = max(row["gsc_clicks_per_post"] for row in eligible) or 1.0
    max_query = max(row["query_impressions"] for row in eligible) or 1.0
    for row in eligible:
        row["efficiency_score"] = (
            0.45 * (row["ga4_sessions_per_post"] / max_sessions)
            + 0.35 * (row["gsc_clicks_per_post"] / max_clicks)
            + 0.20 * (row["query_impressions"] / max_query)
        )
    return sorted(eligible, key=lambda row: row["efficiency_score"], reverse=True)


def top_pages_by_metric(page_rows, metric, limit=15):
    return sorted(page_rows, key=lambda row: row[metric], reverse=True)[:limit]


def build_markdown(topic_rows, format_rows, page_rows, ga4_meta, gsc_page_meta, gsc_query_meta):
    topic_ranked = rank_rows(topic_rows, volume_floor=20)
    weak_topics = [row for row in sorted(topic_rows, key=lambda row: row["efficiency_score"] if "efficiency_score" in row else 0) if row["posts"] >= 20][:8]
    strongest = topic_ranked[:10]
    weakest = sorted(
        [row for row in topic_rows if row["posts"] >= 20],
        key=lambda row: (
            row["ga4_sessions_per_post"],
            row["gsc_clicks_per_post"],
            row["query_impressions"],
        ),
    )[:10]
    format_ranked = rank_rows(format_rows, volume_floor=25)
    top_ga4_pages = top_pages_by_metric(page_rows, "ga4_sessions", limit=15)
    top_gsc_pages = top_pages_by_metric(page_rows, "gsc_clicks", limit=15)
    low_pages = [
        row
        for row in sorted(page_rows, key=lambda row: (row["ga4_sessions"], row["gsc_clicks"]))
        if row["ga4_sessions"] <= 30 and row["gsc_clicks"] <= 10
    ][:20]

    lines = []
    lines.append("# LSA tematická analýza za posledních 16 měsíců")
    lines.append("")
    lines.append(f"Období: **{START_DATE.isoformat()} až {END_DATE.isoformat()}**")
    lines.append("")
    lines.append("## Co z toho plyne")
    lines.append("")
    if strongest:
        top = strongest[0]
        lines.append(
            f"- Nejsilnější oblast podle kombinace `GA4 + GSC + query demand` je **{top['label']}** "
            f"({top['posts']} článků, {to_int(top['ga4_sessions'])} sessions, {to_int(top['gsc_clicks'])} GSC kliků)."
        )
    if len(strongest) > 1:
        second = strongest[1]
        lines.append(
            f"- Hned za ní je **{second['label']}**, která drží vysokou čtenost i vyhledávací poptávku."
        )
    if weakest:
        weak = weakest[0]
        lines.append(
            f"- Nejvíc přestřelená oblast s dost objemem, ale slabým návratem je **{weak['label']}** "
            f"({weak['posts']} článků, jen {to_int(weak['ga4_sessions_per_post'])} sessions/článek a "
            f"{to_int(weak['gsc_clicks_per_post'])} GSC kliků/článek)."
        )
    if format_ranked:
        lines.append(
            f"- Z formátů nejlépe funguje **{format_ranked[0]['label']}**, zatímco nejslabší velké formáty jsou níž v reportu."
        )
    lines.append("")
    lines.append("## Silná témata")
    lines.append("")
    for row in strongest:
        lines.append(
            f"- **{row['label']}**: {row['posts']} článků | {to_int(row['ga4_sessions'])} sessions "
            f"({pct(row['ga4_share'])} % GA4) | {to_int(row['gsc_clicks'])} GSC kliků | "
            f"{to_int(row['ga4_sessions_per_post'])} sessions/článek | {to_int(row['gsc_clicks_per_post'])} kliků/článek"
        )
    lines.append("")
    lines.append("## Slabá témata")
    lines.append("")
    for row in weakest:
        lines.append(
            f"- **{row['label']}**: {row['posts']} článků | {to_int(row['ga4_sessions'])} sessions | "
            f"{to_int(row['gsc_clicks'])} GSC kliků | {to_int(row['ga4_sessions_per_post'])} sessions/článek | "
            f"{to_int(row['gsc_clicks_per_post'])} kliků/článek"
        )
    lines.append("")
    lines.append("## Formáty")
    lines.append("")
    for row in format_ranked[:8]:
        lines.append(
            f"- **{row['label']}**: {row['posts']} článků | {to_int(row['ga4_sessions'])} sessions | "
            f"{to_int(row['gsc_clicks'])} GSC kliků | {to_int(row['ga4_sessions_per_post'])} sessions/článek"
        )
    lines.append("")
    lines.append("## Top GA4 články")
    lines.append("")
    for row in top_ga4_pages:
        lines.append(f"- **{row['title']}** ({row['topic']}) — {row['ga4_sessions']} sessions | {row['path']}")
    lines.append("")
    lines.append("## Top GSC články")
    lines.append("")
    for row in top_gsc_pages:
        lines.append(
            f"- **{row['title']}** ({row['topic']}) — {row['gsc_clicks']} kliků | {row['gsc_impressions']} impresí | {row['path']}"
        )
    lines.append("")
    lines.append("## Kandidáti na omezení")
    lines.append("")
    for row in low_pages:
        lines.append(
            f"- **{row['title']}** ({row['topic']}) — {row['ga4_sessions']} sessions | {row['gsc_clicks']} kliků | {row['path']}"
        )
    lines.append("")
    lines.append("## Doporučení")
    lines.append("")
    for row in strongest[:5]:
        lines.append(f"- Posílit **{row['label']}**. Tady už publikum i Google prokazatelně reagují.")
    for row in weakest[:5]:
        lines.append(f"- Omezit nebo zpřísnit výběr u **{row['label']}**. Publikační objem je vysoký, návrat nízký.")
    lines.append("")
    lines.append("## Technická poznámka")
    lines.append("")
    any_ga4_loss = any(item.get("data_loss_from_other") for item in ga4_meta)
    if any_ga4_loss:
        lines.append(
            "- `GA4` byla kvůli vysoké kardinalitě tahána po měsících jen pro článkové landing pages. "
            "Některé měsíce hlásily `dataLossFromOtherRow`, takže GA4 část je velmi silná pro trendy a témata, "
            "ale neberu ji jako 100% absolutní census všech landing pages."
        )
    else:
        lines.append(
            "- `GA4` byla kvůli vysoké kardinalitě tahána po měsících jen pro článkové landing pages. "
            "Ve finálním běhu se podařilo stáhnout všechny měsíce bez `dataLossFromOtherRow`."
        )
    lines.append("- `GSC` stránky i dotazy jsou paginované po měsících a agregované přes celé období.")
    lines.append("- `WP` je použito jako zdroj publikačního objemu a kategorií.")
    lines.append("")
    lines.append("## Meta")
    lines.append("")
    lines.append(f"- GA4 měsíce: {len(ga4_meta)}")
    lines.append(f"- GSC page měsíce: {len(gsc_page_meta)}")
    lines.append(f"- GSC query měsíce: {len(gsc_query_meta)}")
    return "\n".join(lines) + "\n"


def main():
    ensure_dirs()
    log("Build services")
    ga4, gsc = build_services()
    category_map = fetch_categories()
    posts = fetch_posts(category_map)
    ga4_pages, ga4_meta = fetch_ga4(ga4)
    gsc_pages, gsc_page_meta = fetch_gsc_dimension(gsc, "page")
    gsc_queries, gsc_query_meta = fetch_gsc_dimension(gsc, "query")

    log("Aggregate")
    page_rows, topic_rows, format_rows = aggregate(posts, ga4_pages, gsc_pages, gsc_queries)
    topic_ranked = rank_rows(topic_rows, volume_floor=20)
    format_ranked = rank_rows(format_rows, volume_floor=25)

    stamp = TODAY.strftime("%Y%m%d")
    write_csv(WP_DIR / f"posts-16m-{stamp}.csv", posts, ["post_id", "date", "path", "title", "slug", "categories", "topic", "format"])
    write_csv(
        GA4_DIR / f"landing-pages-16m-{stamp}.csv",
        [
            {
                "path": path,
                "sessions": to_int(values["sessions"]),
                "active_users": to_int(values["active_users"]),
                "page_views": to_int(values["page_views"]),
                "engagement_rate": round(values["engagement_rate"], 4),
                "avg_session_duration": round(values["avg_session_duration"], 1),
            }
            for path, values in sorted(ga4_pages.items())
        ],
        ["path", "sessions", "active_users", "page_views", "engagement_rate", "avg_session_duration"],
    )
    write_csv(
        GSC_DIR / f"pages-16m-{stamp}.csv",
        [
            {
                "path": path,
                "clicks": to_int(values["clicks"]),
                "impressions": to_int(values["impressions"]),
                "ctr": round(values["ctr"], 4),
                "position": round(values["position"], 2),
            }
            for path, values in sorted(gsc_pages.items())
        ],
        ["path", "clicks", "impressions", "ctr", "position"],
    )
    write_csv(
        GSC_DIR / f"queries-16m-{stamp}.csv",
        [
            {
                "query": query,
                "topic": query_topic(query),
                "clicks": to_int(values["clicks"]),
                "impressions": to_int(values["impressions"]),
                "ctr": round(values["ctr"], 4),
                "position": round(values["position"], 2),
            }
            for query, values in sorted(gsc_queries.items())
        ],
        ["query", "topic", "clicks", "impressions", "ctr", "position"],
    )
    write_csv(
        REPORTS_DIR / f"lsa_topic_pages_16m_{stamp}.csv",
        sorted(page_rows, key=lambda row: row["ga4_sessions"], reverse=True),
        [
            "path",
            "title",
            "date",
            "topic",
            "format",
            "categories",
            "ga4_sessions",
            "ga4_page_views",
            "ga4_active_users",
            "ga4_engagement_rate",
            "ga4_avg_session_duration",
            "gsc_clicks",
            "gsc_impressions",
            "gsc_ctr",
            "gsc_position",
        ],
    )
    write_csv(
        REPORTS_DIR / f"lsa_topic_summary_16m_{stamp}.csv",
        sorted(topic_ranked or topic_rows, key=lambda row: row["ga4_sessions"], reverse=True),
        [
            "label",
            "posts",
            "ga4_sessions",
            "ga4_page_views",
            "ga4_active_users",
            "ga4_share",
            "ga4_sessions_per_post",
            "ga4_engagement_rate",
            "ga4_avg_session_duration",
            "gsc_clicks",
            "gsc_impressions",
            "gsc_share",
            "gsc_clicks_per_post",
            "gsc_position",
            "query_clicks",
            "query_impressions",
            "query_impression_share",
            "query_position",
            "efficiency_score",
        ],
    )

    report_path = REPORTS_DIR / f"lsa_tematicka_analyza_16m_{stamp}.md"
    report_path.write_text(
        build_markdown(topic_rows, format_rows, page_rows, ga4_meta, gsc_page_meta, gsc_query_meta),
        encoding="utf-8",
    )

    meta_path = REPORTS_DIR / f"lsa_tematicka_analyza_16m_{stamp}.json"
    meta_path.write_text(
        json.dumps(
            {
                "site": SITE,
                "start_date": START_DATE.isoformat(),
                "end_date": END_DATE.isoformat(),
                "posts_count": len(posts),
                "ga4_paths": len(ga4_pages),
                "gsc_pages": len(gsc_pages),
                "gsc_queries": len(gsc_queries),
                "ga4_month_meta": ga4_meta,
                "gsc_page_meta": gsc_page_meta,
                "gsc_query_meta": gsc_query_meta,
                "top_topics": topic_ranked[:10],
                "top_formats": format_ranked[:10],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    log("Done")
    print(json.dumps({"report": str(report_path), "meta": str(meta_path), "posts": len(posts)}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)

#!/usr/bin/env python3
"""
Lisa Pre-flight Check — spustit PŘED každým ranním cyklem
Výstup: PASS (vše OK) nebo FAIL (co nefunguje + ETA instrukce)
"""
import datetime
import os, sys, json, urllib.parse, urllib.request, base64
from google.oauth2 import service_account
from googleapiclient.discovery import build

RESULTS = {}

# --- 1. GA4 (all 3 active sites) ---
SA_PATH = os.path.expanduser("~/.openclaw/workspace/android-magazine-sa.json")
try:
    creds = service_account.Credentials.from_service_account_file(
        SA_PATH, scopes=["https://www.googleapis.com/auth/analytics.readonly"])
    svc = build("analyticsdata", "v1beta", credentials=creds, cache_discovery=False)
    ga4_properties = {
        "LSA": "361706440",
        "Android": "361709661",
        "Samsung": "361723333",
    }
    for name, property_id in ga4_properties.items():
        svc.properties().runReport(property=f"properties/{property_id}", body={
            "dateRanges": [{"startDate": "1daysAgo","endDate": "yesterday"}],
            "metrics": [{"name":"sessions"}],
            "limit": 1,
        }).execute()
        RESULTS[f"GA4_{name}"] = "PASS"
except Exception as e:
    RESULTS["GA4"] = f"FAIL: {str(e)[:80]}"

# --- 2. GSC (all 3 active sites) ---
try:
    creds = service_account.Credentials.from_service_account_file(
        SA_PATH, scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
    svc = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    gsc_sites = {
        "LSA": "sc-domain:letemsvetemapplem.eu",
        "Android": "sc-domain:androidmagazine.eu",
        "Samsung": "sc-domain:samsungmagazine.eu",
    }
    body = {
        "startDate": (datetime.date.today() - datetime.timedelta(days=7)).isoformat(),
        "endDate": (datetime.date.today() - datetime.timedelta(days=1)).isoformat(),
        "dimensions": ["date"],
        "rowLimit": 1,
    }
    for name, site_url in gsc_sites.items():
        svc.searchanalytics().query(siteUrl=site_url, body=body).execute()
        RESULTS[f"GSC_{name}"] = "PASS"
except Exception as e:
    RESULTS["GSC"] = f"FAIL: {str(e)[:80]}"

# --- 3. Manticore (all 3 active sites) ---
MANTICORE_URL = "https://searchnew.tfsys.eu/results"
MANTICORE_USER = "lisa.ai.textfactory.cz"
MANTICORE_PASS = os.environ.get("MANTICORE_PASS", "")
try:
    if not MANTICORE_PASS:
        raise RuntimeError("MANTICORE_PASS missing")
    token = base64.b64encode(f"{MANTICORE_USER}:{MANTICORE_PASS}".encode()).decode()
    for name, tf_user in {
        "LSA": "letemsvetemapplem.eu",
        "Android": "androidmagazine.eu",
        "Samsung": "samsungmagazine.eu",
    }.items():
        query = urllib.parse.urlencode({
            "tf_user": tf_user,
            "s": "test",
            "count": 1,
            "post_status": "any",
        })
        req = urllib.request.Request(
            f"{MANTICORE_URL}?{query}",
            headers={"Authorization": f"Basic {token}"}
        )
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read())
            RESULTS[f"Manticore_{name}"] = f"PASS ({len(data.get('docs', []))} docs)"
except Exception as e:
    RESULTS["Manticore"] = f"FAIL: {str(e)[:80]}"

# --- 4. WordPress auth (všechny 3 weby) ---
WP_SITES = {
    "LSA": ("https://www.letemsvetemapplem.eu/wp-json/wp/v2/posts?per_page=1", "Lisa", os.environ.get("WP_LSA_PASS","")),
    "Android": ("https://androidmagazine.eu/wp-json/wp/v2/posts?per_page=1", "Lisa", os.environ.get("WP_ANDROID_PASS","")),
    "Samsung": ("https://samsungmagazine.eu/wp-json/wp/v2/posts?per_page=1", "LisaAI", os.environ.get("WP_SAMSUNG_PASS","")),
}
for name, (url, user, pwd) in WP_SITES.items():
    try:
        token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
        req = urllib.request.Request(url, headers={"Authorization": f"Basic {token}"})
        with urllib.request.urlopen(req, timeout=8) as r:
            posts = json.loads(r.read())
            RESULTS[f"WP_{name}"] = f"PASS ({len(posts)} posts)"
    except Exception as e:
        RESULTS[f"WP_{name}"] = f"FAIL: {str(e)[:60]}"

# --- Výstup ---
print("\n=== LISA PRE-FLIGHT CHECK ===")
all_pass = True
for k, v in RESULTS.items():
    icon = "✅" if v.startswith("PASS") else "❌"
    print(f"  {icon} {k}: {v}")
    if not v.startswith("PASS"):
        all_pass = False

print(f"\n{'✅ VŠECHNO OK — cyklus může běžet' if all_pass else '❌ STOP — opravit výše uvedené před spuštěním cyklu'}")
sys.exit(0 if all_pass else 1)

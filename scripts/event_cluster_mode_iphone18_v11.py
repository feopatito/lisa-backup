#!/usr/bin/env python3
"""
LISA Search Opportunity Engine | Event Cluster Mode v1.0
Run: iPhone 18 / keynote 2026-09-09 / letemsvetemapplem.eu

Produces:
- reports/iphone18_event_cluster_mode_20260831.md
- reports/iphone18_event_cluster_mode_20260831.pdf
- reports/iphone18_event_cluster_mode_20260831.json
"""

from __future__ import annotations

import csv
import json
import math
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Callable

from google.oauth2 import service_account
from googleapiclient.discovery import build
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


ROOT = Path("/Users/lisa/.openclaw/workspace")
REPORTS = ROOT / "reports"
SA_FILE = ROOT / "android-magazine-sa.json"
SITE = "sc-domain:letemsvetemapplem.eu"
STAMP = "20260831"

LOCAL_GSC_JSON = REPORTS / "lsa_evergreen_gsc_16m_20260826.json"
WP_POSTS = ROOT / "magazines/letemsvetemapplem/wordpress/posts-16m-20260831.csv"
GA4_PAGES = ROOT / "magazines/letemsvetemapplem/analytics/ga4/landing-pages-16m-20260831.csv"

OUT_MD = REPORTS / f"iphone18_event_cluster_mode_{STAMP}.md"
OUT_PDF = REPORTS / f"iphone18_event_cluster_mode_{STAMP}.pdf"
OUT_JSON = REPORTS / f"iphone18_event_cluster_mode_{STAMP}.json"

CURRENT_START = "2026-08-01"
CURRENT_END = "2026-08-30"
CURRENT_PRE_START = "2026-08-24"
CURRENT_PRE_END = "2026-08-30"
PRIMARY_WINDOW = "2026-08-31 až 2026-09-16"
PRIMARY_ANALOG_START = "2025-08-31"
PRIMARY_ANALOG_END = "2025-09-16"
ANALOG_PRE_START = "2025-08-24"
ANALOG_PRE_END = "2025-08-30"


def build_gsc():
    creds = service_account.Credentials.from_service_account_file(
        str(SA_FILE), scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def gsc_pull(service, start_date: str, end_date: str, dimensions: list[str], regex: str, country: str | None = None):
    rows = []
    filters = []
    if country:
        filters.append({"dimension": "country", "operator": "equals", "expression": country})
    filters.append({"dimension": "query", "operator": "includingRegex", "expression": regex})
    for start_row in range(0, 25000, 2500):
        body = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions,
            "rowLimit": 2500,
            "startRow": start_row,
            "dataState": "all",
            "dimensionFilterGroups": [{"filters": filters}],
        }
        resp = service.searchanalytics().query(siteUrl=SITE, body=body).execute()
        batch = resp.get("rows", [])
        rows.extend(batch)
        if len(batch) < 2500:
            break
    return rows


def load_json(path: Path):
    with path.open() as f:
        return json.load(f)


def load_wp_posts():
    posts = {}
    with WP_POSTS.open(newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or row[0] == "id":
                continue
            posts[row[2]] = {
                "date": row[1],
                "title": row[3],
                "slug": row[4],
                "topic": row[6],
                "format": row[7],
            }
    return posts


def load_ga4_pages():
    pages = {}
    with GA4_PAGES.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pages[row["path"]] = {
                "sessions": int(row["sessions"]),
                "views": int(row["page_views"]),
                "engagement_rate": float(row["engagement_rate"]),
                "avg_session_duration": float(row["avg_session_duration"]),
            }
    return pages


def slug_to_abs(path_or_url: str) -> str:
    if path_or_url.startswith("http"):
        return path_or_url
    return "https://www.letemsvetemapplem.eu" + path_or_url


def url_to_path(url: str) -> str:
    if url.startswith("https://www.letemsvetemapplem.eu"):
        return url.replace("https://www.letemsvetemapplem.eu", "")
    return url


def sum_metric(rows, key):
    return sum(float(r.get(key, 0) or 0) for r in rows)


def weighted_position(rows):
    impressions = sum_metric(rows, "impressions")
    if impressions <= 0:
        return 0.0
    return sum(float(r["position"]) * float(r["impressions"]) for r in rows) / impressions


def pct(value):
    return f"{value * 100:.2f}%"


ENTITY_REGEX = r"iphone ?18|iphone18|iphone ultra"
ANALOG_REGEX = r"iphone ?17|iphone17|iphone air"

MODIFIERS = [
    "cena", "price", "preis", "prezzo", "precio", "pris", "τιμη", "ár",
    "kdy vyjde", "kdy bude", "date", "release", "launch", "datum", "představ", "predstav",
    "barv", "color", "farbe", "colo", "renk", "bordo", "burgundy", "red", "červen",
    "foto", "camera", "fotoapar", "zoom", "teleobj", "clona",
    "design", "vzhled", "dynamic island", "face id", "display", "displej",
    "preorder", "předobjed", "predobjed", "dostup", "kde koupit", "buy", "koupit",
    "vs", "srovn", "rozdil", "wait", "počkat", "pockat",
]


def qnorm(q: str) -> str:
    return q.lower().strip()


def base_entity(q: str) -> bool:
    q = qnorm(q)
    return ("iphone 18" in q) or ("iphone18" in q) or ("apple iphone 18" in q)


def ultra_entity(q: str) -> bool:
    return "iphone ultra" in qnorm(q)


def match_generic_hub(q: str) -> bool:
    q = qnorm(q)
    if ultra_entity(q):
        return False
    if not base_entity(q):
        return False
    return not any(x in q for x in MODIFIERS)


def match_generic_pro_max(q: str) -> bool:
    q = qnorm(q)
    if ultra_entity(q):
        return False
    if "iphone 18 pro max" not in q and "iphone18pro max" not in q and "iphone18pro max" not in q:
        return False
    return not any(x in q for x in MODIFIERS if x not in {"pro"})


def match_price(q: str) -> bool:
    q = qnorm(q)
    if ultra_entity(q):
        return False
    return base_entity(q) and any(x in q for x in ["cena", "price", "preis", "prezzo", "precio", "pris", "τιμη", "ár"])


def match_release(q: str) -> bool:
    q = qnorm(q)
    if ultra_entity(q):
        return False
    return base_entity(q) and any(x in q for x in ["kdy vyjde", "kdy bude", "date", "release", "launch", "datum", "představ", "predstav"])


def match_preorders(q: str) -> bool:
    q = qnorm(q)
    if ultra_entity(q):
        return False
    return base_entity(q) and any(x in q for x in ["předobjed", "predobjed", "preorder", "dostup", "kde koupit", "buy", "koupit"])


def match_colors(q: str) -> bool:
    q = qnorm(q)
    if ultra_entity(q):
        return False
    return base_entity(q) and any(x in q for x in ["barv", "color", "farbe", "colo", "renk", "bordo", "burgundy", "red", "červen"])


def match_ultra_hub(q: str) -> bool:
    q = qnorm(q)
    if not ultra_entity(q):
        return False
    return not any(x in q for x in ["cena", "price", "barv", "color", "kdy", "date", "predstav", "preorder", "buy", "koupit"])


def match_ultra_price(q: str) -> bool:
    q = qnorm(q)
    return ultra_entity(q) and any(x in q for x in ["cena", "price"])


def analog_generic(q: str) -> bool:
    q = qnorm(q)
    if "iphone air" in q:
        return not any(x in q for x in MODIFIERS)
    return ("iphone 17" in q or "iphone17" in q or "apple iphone 17" in q) and not any(x in q for x in MODIFIERS)


def analog_price(q: str) -> bool:
    q = qnorm(q)
    return (("iphone 17" in q or "iphone air" in q) and any(x in q for x in ["cena", "price", "preis", "prezzo", "precio", "pris", "τιμη", "ár"]))


def analog_release(q: str) -> bool:
    q = qnorm(q)
    return (("iphone 17" in q or "iphone air" in q) and any(x in q for x in ["kdy vyjde", "kdy bude", "date", "release", "launch", "datum", "představ", "predstav"]))


def analog_preorders(q: str) -> bool:
    q = qnorm(q)
    return (("iphone 17" in q or "iphone air" in q) and any(x in q for x in ["předobjed", "predobjed", "preorder", "dostup", "kde koupit", "buy", "koupit"]))


def analog_colors(q: str) -> bool:
    q = qnorm(q)
    return (("iphone 17" in q or "iphone air" in q) and any(x in q for x in ["barv", "color", "farbe", "colo", "renk", "bordo", "burgundy", "red", "červen"]))


def analog_pro_max(q: str) -> bool:
    q = qnorm(q)
    return ("iphone 17 pro max" in q) and not any(x in q for x in MODIFIERS if x not in {"pro"})


def analog_ultra_hub(q: str) -> bool:
    q = qnorm(q)
    return ("iphone air" in q) and not any(x in q for x in ["cena", "price", "barv", "color", "kdy", "date", "predstav", "preorder", "buy", "koupit"])


def analog_ultra_price(q: str) -> bool:
    q = qnorm(q)
    return ("iphone air" in q) and any(x in q for x in ["cena", "price"])


CLUSTERS = [
    {
        "id": "generic_hub",
        "intent": "iPhone 18 / Pro / Pro Max overview hub",
        "user_job": "Uživatel chce na jednom místě rychle zjistit, co o celé řadě iPhone 18 už víme a na co se zaměřit před keynote.",
        "action": "MERGE",
        "target_url": "https://www.letemsvetemapplem.eu/2026/08/08/iphone-18-pro-je-uz-za-dvermi-toto-je-12-nejvetsich-novinek-ktere-ma-nabidnout/",
        "title": "iPhone 18: co víme o celé řadě, jaké modely přijdou a co čekat od keynote",
        "h1": "iPhone 18: co víme o celé řadě, modelech Pro, Pro Max a Ultra",
        "change": "Zastavit rozptyl mezi desítkami rumor URL a přepsat cílovou stránku do role hlavního přehledu: modely, nejjistější novinky, co je potvrzené vs. leak, interní rozcestník na cenu, datum, barvy a Ultra.",
        "links": [
            "https://www.letemsvetemapplem.eu/2026/07/27/iphone-18-pro-cena-2026/",
            "https://www.letemsvetemapplem.eu/2026/08/26/iphone-18-pro-date/",
            "https://www.letemsvetemapplem.eu/2026/08/06/iphone-ultra-specifikace-cena-a-vse-ostatni-co-potrebujete-vedet/",
        ],
        "deadline": "NOW",
        "why_now": "Je to největší search bucket v clusteru a zároveň největší chaos v URL mapě. Každý další leak teď dál ředí signály. Konsolidace má smysl ještě před hlavní eventovou špičkou.",
        "risk": "cannibalization",
        "confidence": "HIGH",
        "current_match": match_generic_hub,
        "analog_match": analog_generic,
        "diagnosis": "CANNIBALIZATION RISK",
    },
    {
        "id": "price",
        "intent": "PRICE / české ceny iPhone 18",
        "user_job": "Uživatel chce vědět, kolik budou stát modely iPhone 18 v Česku a jaké cenové rozdíly čekat mezi Pro, Pro Max a Ultra.",
        "action": "UPDATE",
        "target_url": "https://www.letemsvetemapplem.eu/2026/07/27/iphone-18-pro-cena-2026/",
        "title": "iPhone 18 cena v Česku: kolik mohou stát Pro, Pro Max a Ultra",
        "h1": "iPhone 18 cena v Česku: odhad cen všech modelů",
        "change": "Doplnit jednu jasnou českou cenovou tabulku, co je analytický odhad a co je leak, odlišit Pro / Pro Max / Ultra a přidat sekci co může s cenou zahýbat po keynote.",
        "links": [
            "https://www.letemsvetemapplem.eu/2026/08/26/iphone-18-pro-date/",
            "https://www.letemsvetemapplem.eu/2026/08/31/iphone-18-pro-preorders/",
            "https://www.letemsvetemapplem.eu/2026/08/06/iphone-ultra-specifikace-cena-a-vse-ostatni-co-potrebujete-vedet/",
        ],
        "deadline": "NOW",
        "why_now": "Cena má silný intent už před keynote a po eventu tradičně vyletí ještě víc. Správná URL už existuje, ale téma si dnes dělí příliš mnoho cenových leaků.",
        "risk": "split signal",
        "confidence": "HIGH",
        "current_match": match_price,
        "analog_match": analog_price,
        "diagnosis": "SPLIT SIGNAL",
    },
    {
        "id": "release",
        "intent": "RELEASE DATE / keynote datum / kdy vyjde",
        "user_job": "Uživatel chce přesně vědět, kdy Apple iPhone 18 ukáže a kdy se reálně čeká spuštění prodeje.",
        "action": "MERGE",
        "target_url": "https://www.letemsvetemapplem.eu/2026/08/26/iphone-18-pro-date/",
        "title": "Kdy vyjde iPhone 18 a kdy bude keynote: datum představení, prodeje a důležité termíny",
        "h1": "Kdy vyjde iPhone 18: keynote, předobjednávky a start prodeje",
        "change": "Sloučit event-date intent do jedné URL, jasně oddělit keynote, předobjednávky a první prodejní den. Dnešní problém je, že Google tahá víc různých článků s lehce jinou interpretací téhož data.",
        "links": [
            "https://www.letemsvetemapplem.eu/2026/08/31/iphone-18-pro-preorders/",
            "https://www.letemsvetemapplem.eu/2026/08/08/iphone-18-pro-je-uz-za-dvermi-toto-je-12-nejvetsich-novinek-ktere-ma-nabidnout/",
        ],
        "deadline": "NOW",
        "why_now": "Datum je D-9 evergreen v rámci eventu: peak jde před keynote a znovu při potvrzení na pódiu. Pokud se intent nesjednotí teď, redakce si sama sebere část budoucích kliků.",
        "risk": "cannibalization",
        "confidence": "HIGH",
        "current_match": match_release,
        "analog_match": analog_release,
        "diagnosis": "WRONG PAGE / CANNIBALIZATION RISK",
    },
    {
        "id": "ultra_hub",
        "intent": "iPhone Ultra hub",
        "user_job": "Uživatel chce pochopit, co je iPhone Ultra zač, v čem se liší od Pro modelů a zda opravdu dorazí už letos.",
        "action": "UPDATE",
        "target_url": "https://www.letemsvetemapplem.eu/2026/08/06/iphone-ultra-specifikace-cena-a-vse-ostatni-co-potrebujete-vedet/",
        "title": "iPhone Ultra: cena, datum, specifikace a vše, co zatím víme",
        "h1": "iPhone Ultra: co o prvním skládacím iPhonu víme",
        "change": "Udržet z této URL skutečný hub pro Ultra: co je potvrzené, odlišit ji od Pro modelů, dát cenu/datum/specs na jednu stránku a odkázat na separátní srovnání s Pro.",
        "links": [
            "https://www.letemsvetemapplem.eu/2026/07/27/iphone-ultra-cena-kolik-bude-stat-prvni-skladaci-telefon-od-applu/",
            "https://www.letemsvetemapplem.eu/2026/07/27/iphone-ultra-predstaveni/",
            "https://www.letemsvetemapplem.eu/2026/08/08/iphone-18-pro-je-uz-za-dvermi-toto-je-12-nejvetsich-novinek-ktere-ma-nabidnout/",
        ],
        "deadline": "NOW",
        "why_now": "Ultra už má vlastní významný search bucket a čtenářský job je odlišný od běžného iPhonu 18. Výhoda je, že LSA už má relativně vhodnou hub URL, takže tady není nutné zakládat novou.",
        "risk": "split signal",
        "confidence": "HIGH",
        "current_match": match_ultra_hub,
        "analog_match": analog_ultra_hub,
        "diagnosis": "CLEAN WINNER WITH LEAK SPILLOVER",
    },
    {
        "id": "colors",
        "intent": "COLORS / barvy",
        "user_job": "Uživatel chce rychle zjistit, v jakých barvách mají nové iPhony dorazit a které varianty jsou nejpravděpodobnější.",
        "action": "MERGE",
        "target_url": "https://www.letemsvetemapplem.eu/2026/08/04/tyto-barvy-iphone-18-pro-dorazi-na-podzim-jedna-z-nich-vypada-naprosto-fantasticky/",
        "title": "iPhone 18 barvy: jaké varianty čekat u Pro, Pro Max a Ultra",
        "h1": "iPhone 18 barvy: přehled očekávaných variant",
        "change": "Sloučit barevné leaky do jedné referenční URL, přidat tabulku model x barva x jistota informace a omezit vznik dalších téměř duplicitních color článků.",
        "links": [
            "https://www.letemsvetemapplem.eu/2026/08/08/iphone-18-pro-je-uz-za-dvermi-toto-je-12-nejvetsich-novinek-ktere-ma-nabidnout/",
            "https://www.letemsvetemapplem.eu/2026/08/06/iphone-ultra-specifikace-cena-a-vse-ostatni-co-potrebujete-vedet/",
        ],
        "deadline": "NEXT 72H",
        "why_now": "Barvy tradičně rostou těsně před keynote a pak znovu v noci po potvrzení. Tady už teď vidíme slušný objem, ale je rozbitý do příliš mnoha podobných článků.",
        "risk": "cannibalization",
        "confidence": "HIGH",
        "current_match": match_colors,
        "analog_match": analog_colors,
        "diagnosis": "CANNIBALIZATION RISK",
    },
    {
        "id": "pro_max_diff",
        "intent": "Pro Max differences / proč vzít Pro Max místo Pro",
        "user_job": "Uživatel chce vědět, co navíc Pro Max přinese proti Pro a zda ten rozdíl stojí za vyšší cenu i větší rozměry.",
        "action": "UPDATE",
        "target_url": "https://www.letemsvetemapplem.eu/2026/08/18/iphone-18-pro-max-ma-dostat-neco-co-iphone-18-pro-mit-nebude-apple-chysta-exkluzivni-vylepseni-fotoaparatu/",
        "title": "iPhone 18 Pro Max vs Pro: co bude exkluzivní a komu se vyplatí větší model",
        "h1": "iPhone 18 Pro Max vs Pro: hlavní rozdíly",
        "change": "Přepsat článek z jednorázového foto leak kusu na evergreen eventovou landing page pro rozdíly Pro Max vs Pro: foťák, baterie, velikost, cena a cílový uživatel.",
        "links": [
            "https://www.letemsvetemapplem.eu/2026/07/27/iphone-18-pro-cena-2026/",
            "https://www.letemsvetemapplem.eu/2026/08/08/iphone-18-pro-je-uz-za-dvermi-toto-je-12-nejvetsich-novinek-ktere-ma-nabidnout/",
        ],
        "deadline": "NEXT 72H",
        "why_now": "Query na Pro Max jsou velké, ale Google je teď posílá na články, které řeší jen dílčí leak. Přeskládání na 'rozdíly a rozhodnutí' má lepší clickability i delší život po eventu.",
        "risk": "wrong page",
        "confidence": "MEDIUM",
        "current_match": match_generic_pro_max,
        "analog_match": analog_pro_max,
        "diagnosis": "WRONG PAGE",
    },
    {
        "id": "preorders",
        "intent": "PREORDERS / dostupnost / kde koupit",
        "user_job": "Uživatel chce vědět, kdy a kde spustí Apple předobjednávky a jak se dostat k telefonu co nejdřív.",
        "action": "UPDATE",
        "target_url": "https://www.letemsvetemapplem.eu/2026/08/31/iphone-18-pro-preorders/",
        "title": "iPhone 18 předobjednávky: kdy začnou, v kolik a co čekat v Česku",
        "h1": "iPhone 18 předobjednávky: vše o startu a dostupnosti",
        "change": "Nechat URL připravenou jako event-night landing page. Doplnit český timing, checklist pro nákup, odkazy na ceny a rozdíl mezi keynote datem a reálným startem objednávek.",
        "links": [
            "https://www.letemsvetemapplem.eu/2026/08/26/iphone-18-pro-date/",
            "https://www.letemsvetemapplem.eu/2026/07/27/iphone-18-pro-cena-2026/",
        ],
        "deadline": "PRE-EVENT",
        "why_now": "Aktuální poptávka je ještě malá, ale historicky je to intent, který skáče těsně před spuštěním a v den potvrzení. Smysl není honit kliky dnes, ale připravit správnou URL ještě před eventem.",
        "risk": "uncertain demand until official timing",
        "confidence": "MEDIUM",
        "current_match": match_preorders,
        "analog_match": analog_preorders,
        "diagnosis": "NO TARGET HISTORY / GOOD TIMING PREP",
    },
]


def top_queries_for_cluster(rows, matcher: Callable[[str], bool], limit=10):
    matched = [r for r in rows if matcher(r["keys"][0])]
    matched.sort(key=lambda r: (r["impressions"], r["clicks"]), reverse=True)
    return [r["keys"][0] for r in matched[:limit]]


def aggregate_query_rows(rows, matcher: Callable[[str], bool]):
    out = [r for r in rows if matcher(r["keys"][0])]
    return {
        "impressions": round(sum_metric(out, "impressions")),
        "clicks": round(sum_metric(out, "clicks")),
        "ctr": (sum_metric(out, "clicks") / sum_metric(out, "impressions")) if sum_metric(out, "impressions") else 0.0,
        "position": weighted_position(out),
        "queries": len(out),
        "rows": out,
    }


def aggregate_query_page_rows(rows, matcher: Callable[[str], bool]):
    out = [r for r in rows if matcher(r["keys"][0])]
    pages = defaultdict(lambda: {"impressions": 0.0, "clicks": 0.0})
    for r in out:
        page = r["keys"][1]
        pages[page]["impressions"] += float(r["impressions"])
        pages[page]["clicks"] += float(r["clicks"])
    ranked = sorted(pages.items(), key=lambda kv: kv[1]["impressions"], reverse=True)
    total = sum(v["impressions"] for _, v in ranked)
    return {
        "urls_count": len(ranked),
        "winner_share": (ranked[0][1]["impressions"] / total) if ranked and total else 0.0,
        "top_pages": ranked[:8],
        "total_impressions": total,
    }


def aggregate_daily(rows, matcher: Callable[[str], bool]):
    days = defaultdict(lambda: {"impressions": 0.0, "clicks": 0.0})
    for r in rows:
        query, day = r["keys"]
        if not matcher(query):
            continue
        days[day]["impressions"] += float(r["impressions"])
        days[day]["clicks"] += float(r["clicks"])
    ordered = sorted(days.items())
    return ordered


def rolling_sum(ordered_days, count):
    if not ordered_days:
        return 0.0, 0.0
    tail = ordered_days[-count:]
    return sum(v["impressions"] for _, v in tail), sum(v["clicks"] for _, v in tail)


def trend_text(ordered_days):
    imp7, clk7 = rolling_sum(ordered_days, 7)
    imp14, clk14 = rolling_sum(ordered_days, 14)
    imp28, clk28 = rolling_sum(ordered_days, 28)
    return {
        "7d": {"impressions": round(imp7), "clicks": round(clk7)},
        "14d": {"impressions": round(imp14), "clicks": round(clk14)},
        "28d": {"impressions": round(imp28), "clicks": round(clk28)},
    }


def analog_summary(ordered_days):
    if not ordered_days:
        return {"impressions": 0, "clicks": 0, "peak_day": None, "peak_impressions": 0}
    peak_day, peak_payload = max(ordered_days, key=lambda item: item[1]["impressions"])
    return {
        "impressions": round(sum(v["impressions"] for _, v in ordered_days)),
        "clicks": round(sum(v["clicks"] for _, v in ordered_days)),
        "peak_day": peak_day,
        "peak_impressions": round(peak_payload["impressions"]),
    }


def forecast(cluster_id: str, current_daily, analog_primary_daily, analog_pre_daily, current_ctr, current_pos, action, diagnosis):
    current_pre_imp = rolling_sum(current_daily, 7)[0]
    analog_pre_imp = rolling_sum(analog_pre_daily, 7)[0]
    analog_primary_imp = analog_summary(analog_primary_daily)["impressions"]
    if analog_pre_imp > 0:
        scale = current_pre_imp / analog_pre_imp
    else:
        scale = 1.0
    scale = max(0.55, min(2.2, scale))
    forecast_imp = round(analog_primary_imp * scale)

    if current_pos <= 2.5:
        delta = 0.008
    elif current_pos <= 4.5:
        delta = 0.015
    else:
        delta = 0.025
    if action == "MERGE":
        delta += 0.005
    if "CANNIBALIZATION" in diagnosis or "WRONG PAGE" in diagnosis or "SPLIT" in diagnosis:
        delta += 0.005
    if cluster_id == "preorders":
        delta += 0.02
    attainable_ctr = min(0.24, current_ctr + delta)
    base = max(0, round(forecast_imp * (attainable_ctr - current_ctr)))
    return {
        "forecast_impressions": forecast_imp,
        "incremental_low": round(base * 0.6),
        "incremental_base": base,
        "incremental_high": round(base * 1.45),
        "scale_vs_analog_pre": round(scale, 2),
        "attainable_ctr": attainable_ctr,
    }


def find_internal_links(urls):
    return [u.replace("https://www.letemsvetemapplem.eu", "") for u in urls]


def build_report():
    gsc = build_gsc()
    local = load_json(LOCAL_GSC_JSON)
    wp_posts = load_wp_posts()
    ga4 = load_ga4_pages()

    q16 = local["queries_16m_cze"]
    q90 = local["queries_90d_cze"]

    current_qp = gsc_pull(gsc, CURRENT_START, CURRENT_END, ["query", "page"], ENTITY_REGEX, "cze")
    current_qd = gsc_pull(gsc, CURRENT_START, CURRENT_END, ["query", "date"], ENTITY_REGEX, "cze")
    current_country = gsc_pull(gsc, CURRENT_START, CURRENT_END, ["country"], ENTITY_REGEX, None)
    current_device = gsc_pull(gsc, CURRENT_START, CURRENT_END, ["device"], ENTITY_REGEX, "cze")
    analog_primary_qd = gsc_pull(gsc, PRIMARY_ANALOG_START, PRIMARY_ANALOG_END, ["query", "date"], ANALOG_REGEX, "cze")
    analog_pre_qd = gsc_pull(gsc, ANALOG_PRE_START, ANALOG_PRE_END, ["query", "date"], ANALOG_REGEX, "cze")

    results = []
    for cfg in CLUSTERS:
        hist = aggregate_query_rows(q16, cfg["current_match"])
        current = aggregate_query_rows(current_qp, cfg["current_match"])
        pages = aggregate_query_page_rows(current_qp, cfg["current_match"])
        trend_now = trend_text(aggregate_daily(current_qd, cfg["current_match"]))
        analog_primary = analog_summary(aggregate_daily(analog_primary_qd, cfg["analog_match"]))
        analog_pre = aggregate_daily(analog_pre_qd, cfg["analog_match"])
        fc = forecast(
            cfg["id"],
            aggregate_daily(current_qd, cfg["current_match"]),
            aggregate_daily(analog_primary_qd, cfg["analog_match"]),
            analog_pre,
            current["ctr"],
            current["position"],
            cfg["action"],
            cfg["diagnosis"],
        )

        target_path = url_to_path(cfg["target_url"])
        target_ga4 = ga4.get(target_path, {"sessions": 0, "views": 0, "engagement_rate": 0.0, "avg_session_duration": 0.0})
        target_meta = wp_posts.get(target_path, {"date": "n/a", "title": target_path})

        item = {
            "intent": cfg["intent"],
            "id": cfg["id"],
            "user_job": cfg["user_job"],
            "action": cfg["action"],
            "target_url": cfg["target_url"],
            "suggested_title": cfg["title"],
            "suggested_h1": cfg["h1"],
            "content_gap": cfg["change"],
            "internal_links": find_internal_links(cfg["links"]),
            "deadline": cfg["deadline"],
            "why_now": cfg["why_now"],
            "risk": cfg["risk"],
            "confidence": cfg["confidence"],
            "diagnosis": cfg["diagnosis"],
            "current_period": f"{CURRENT_START} až {CURRENT_END}",
            "current_impressions": current["impressions"],
            "current_clicks": current["clicks"],
            "current_ctr": current["ctr"],
            "weighted_position": current["position"],
            "trend_7_14_28": trend_now,
            "historical_analog": analog_primary,
            "existing_urls": [
                {
                    "url": page,
                    "impressions": round(values["impressions"]),
                    "clicks": round(values["clicks"]),
                    "share": round(values["impressions"] / pages["total_impressions"] * 100, 1) if pages["total_impressions"] else 0,
                }
                for page, values in pages["top_pages"][:5]
            ],
            "forecast_impressions": fc["forecast_impressions"],
            "incremental_low": fc["incremental_low"],
            "incremental_base": fc["incremental_base"],
            "incremental_high": fc["incremental_high"],
            "attainable_ctr": fc["attainable_ctr"],
            "scale_vs_analog_pre": fc["scale_vs_analog_pre"],
            "query_cluster": top_queries_for_cluster(q90, cfg["current_match"], 12),
            "hist_16m_impressions": hist["impressions"],
            "hist_16m_clicks": hist["clicks"],
            "urls_count": pages["urls_count"],
            "winner_share": pages["winner_share"],
            "target_ga4": target_ga4,
            "target_meta": target_meta,
        }
        results.append(item)

    results = [r for r in results if r["incremental_base"] >= 25 or r["current_impressions"] >= 3000]
    results.sort(key=lambda r: r["incremental_base"], reverse=True)
    for idx, row in enumerate(results, 1):
        row["rank"] = idx

    create_count = sum(1 for r in results if r["action"] == "CREATE")
    update_count = sum(1 for r in results if r["action"] == "UPDATE")
    merge_count = sum(1 for r in results if r["action"] == "MERGE")
    keep_count = sum(1 for r in results if r["action"] == "KEEP")

    current_top_countries = [
        {
            "country": row["keys"][0],
            "impressions": round(float(row["impressions"])),
            "clicks": round(float(row["clicks"])),
            "ctr": float(row["ctr"]),
        }
        for row in current_country[:8]
    ]
    current_devices = [
        {
            "device": row["keys"][0],
            "impressions": round(float(row["impressions"])),
            "clicks": round(float(row["clicks"])),
            "ctr": float(row["ctr"]),
        }
        for row in current_device[:5]
    ]

    report = {
        "meta": {
            "site": "letemsvetemapplem.eu",
            "entity": "iPhone 18",
            "event": "Apple keynote / představení iPhone 18",
            "event_date": "2026-09-09",
            "primary_window": PRIMARY_WINDOW,
            "secondary_window": "2026-09-17 až 2026-10-24",
            "current_gsc_period": f"{CURRENT_START} až {CURRENT_END}",
            "historical_limit_note": "GSC historicky dovoluje max. 16 měsíců, takže plný prelaunch iPhone 16 a iPhone 15 není dostupný. Hlavní analog je iPhone 17 a pro Ultra/Air vstupuje i iPhone Air.",
        },
        "executive_summary": {
            "strong_opportunities": len(results),
            "create": create_count,
            "update": update_count,
            "merge": merge_count,
            "keep": keep_count,
            "estimated_base_incremental_clicks": sum(r["incremental_base"] for r in results),
            "top_3_actions_now": [
                "Sloučit generic iPhone 18 intent do jednoho hlavního hubu a přestat ho rozbíjet mezi rumor články.",
                "Přepsat a sjednotit date / release / preorder intent, protože právě tam teď Google střídá více částečně chybných URL.",
                "U price a Ultra hubu dotáhnout referenční landing pages dřív, než přijde keynote peak.",
            ],
            "biggest_blocker": "Největší brzda clusteru není malá poptávka, ale roztříštěná URL mapa. LSA má search demand, ale zbytečně ji tříští do mnoha leak článků místo několika cílových stránek.",
        },
        "top_opportunities": results,
        "rejected_ideas": [
            {
                "idea": "iPhone 17 vs iPhone 18 a iPhone 17 Pro vs iPhone 18 Pro jako top search zásahy",
                "reason": "Aktuální CZ search data jsou výrazně slabší než u generic/date/price/color intentů. Tyhle kusy mohou fungovat redakčně nebo v Discoveru, ale teď nejsou mezi TOP search opportunities.",
            },
            {
                "idea": "Samostatný článek pro každou barvu iPhone 18 Pro",
                "reason": "Patří do jednoho color intentu. Další separace by jen zhoršila kanibalizaci.",
            },
            {
                "idea": "X emoji k keynote nebo jak sledovat keynote živě jako search top opportunity",
                "reason": "Tohle jsou spíš Discover side-bets; search intent je proti hlavním eventovým dotazům malý nebo navigační.",
            },
            {
                "idea": "Čistě camera-only nebo design-only standalone URL bez širšího user jobu",
                "reason": "V současných datech nemají dost velký samostatný search upside proti price/date/generic/Ultra hubům.",
            },
        ],
        "cannibalization_map": [
            {
                "intent": "Generic iPhone 18 / Pro / Pro Max",
                "competing_urls": [r["url"] for r in results[0]["existing_urls"][:5]] if results else [],
                "resolution": "Jeden hlavní hub + zbytek interně odkázat jako supporting pieces; netvořit další generic summary URL.",
            },
            {
                "intent": "Release date / kdy vyjde",
                "competing_urls": [
                    "https://www.letemsvetemapplem.eu/2026/07/30/kdy-vyjde-iphone-18-vime-apple-odhali-svuj-novy-zakladni-model/",
                    "https://www.letemsvetemapplem.eu/2026/08/26/iphone-18-pro-date/",
                    "https://www.letemsvetemapplem.eu/2026/08/21/iphone-18-pro-dorazi-uz-za-par-tydnu-tohle-je-nejpravdepodobnejsi-datum-predobjednavek/",
                ],
                "resolution": "Sjednotit date intent do jedné referenční URL a zbylé články z ní interně odkazovat.",
            },
            {
                "intent": "Price",
                "competing_urls": [
                    "https://www.letemsvetemapplem.eu/2026/07/27/iphone-18-pro-cena-2026/",
                    "https://www.letemsvetemapplem.eu/2026/06/27/vime-o-kolik-ma-zdrazit-iphone-18-pro-max/",
                    "https://www.letemsvetemapplem.eu/2026/08/04/cena-iphone-18-pro-vyvolava-obavy-zdrazeni-o-tretinu-je-ale-nepravdepodobne/",
                ],
                "resolution": "Držet jednu price URL s tabulkou a ostatní cenové leaky používat jen jako zdroje a interní odkazy.",
            },
            {
                "intent": "Colors",
                "competing_urls": [
                    "https://www.letemsvetemapplem.eu/2026/08/04/tyto-barvy-iphone-18-pro-dorazi-na-podzim-jedna-z-nich-vypada-naprosto-fantasticky/",
                    "https://www.letemsvetemapplem.eu/2026/05/23/barvy-iphone-18-pro-potvrzeny-dalsim-unikem-fotky/",
                    "https://www.letemsvetemapplem.eu/2026/08/11/iphone-18-pro-dostane-barvu-jakou-apple-jeste-nepouzil-uz-ted-vime-jak-presne-bude-vypadat/",
                ],
                "resolution": "Z jedné URL udělat color hub a další variace už jen aktualizovat uvnitř ní.",
            },
        ],
        "discover_side_bets": [
            {
                "idea": "Apple Keynote 2026 livestream: představení iPhone 18 Pro živě",
                "reason": "Má smysl pro Discover a realtime interest, ale není to jedna z největších search opportunities v clusteru.",
            },
            {
                "idea": "5 teorií, co by mohla prozrazovat pozvánka na představení iPhone 18 Pro a Ultra",
                "reason": "Dobrý clickbait/discovery kus, ale slabší search economics než date/price/generic intent.",
            },
        ],
        "missing_data": [
            {
                "missing": "Plná GSC historie iPhone 16 a iPhone 15 prelaunch oken",
                "impact": "Snižuje confidence u historických multiplikátorů. GSC má limit 16 měsíců, takže plný starší prelaunch už z API nevytáhneme.",
            },
            {
                "missing": "Čerstvá Search Console data za posledních 48-72 hodin po 2026-08-30",
                "impact": "Mírně snižuje confidence u intentů kolem dnešní preorders URL. To je normální GSC lag.",
            },
            {
                "missing": "Live SERP snapshot po intentu",
                "impact": "Diagnóza clickability a zero-click risku je silná, ale ne podložená dedikovaným dnešním SERP crawllem pro každou query variantu.",
            },
        ],
        "execution_plan_24h": [
            "Přepsat hlavní iPhone 18 hub z 8. 8. do role jediné referenční landing page pro generic intent.",
            "Sjednotit release/date intent kolem jedné URL a jasně oddělit keynote datum, předobjednávky a prodej.",
            "Na price URL doplnit českou tabulku všech modelů a odstranit nejistotu mezi Pro, Pro Max a Ultra.",
            "Připravit preorders URL jako event-night landing page a silně ji interně propojit z date a price stránek.",
            "Z Ultra URL udělat hlavní rozcestník pro fold/Ultra dotazy a přestat rozbíjet generic Ultra intent do leaku o barvách či videích.",
        ],
        "country_split_current": current_top_countries,
        "device_split_current_cz": current_devices,
    }
    return report


def build_markdown(report):
    lines = []
    meta = report["meta"]
    summary = report["executive_summary"]
    lines.append("# LISA | Search Opportunity Engine | Event Cluster Mode")
    lines.append("")
    lines.append("## EXECUTIVE SUMMARY")
    lines.append(f"- Strong opportunities found: {summary['strong_opportunities']}")
    lines.append(f"- CREATE: {summary['create']}")
    lines.append(f"- UPDATE: {summary['update']}")
    lines.append(f"- MERGE: {summary['merge']}")
    lines.append(f"- KEEP: {summary['keep']}")
    lines.append(f"- Estimated BASE incremental clicks in PRIMARY_WINDOW: {summary['estimated_base_incremental_clicks']}")
    lines.append("- Top 3 actions now:")
    lines.append(f"  1. {summary['top_3_actions_now'][0]}")
    lines.append(f"  2. {summary['top_3_actions_now'][1]}")
    lines.append(f"  3. {summary['top_3_actions_now'][2]}")
    lines.append(f"- Biggest current blocker: {summary['biggest_blocker']}")
    lines.append("")
    lines.append("## TOP OPPORTUNITIES")
    lines.append("# | Intent | Action | Target URL | Impressions | Clicks | CTR | W. Position | Trend | Forecast Impressions | Incremental Clicks BASE | Confidence | Deadline")
    for row in report["top_opportunities"]:
        trend = row["trend_7_14_28"]
        trend_text_value = f"7d {trend['7d']['impressions']} / 14d {trend['14d']['impressions']} / 28d {trend['28d']['impressions']}"
        lines.append(
            f"{row['rank']} | {row['intent']} | {row['action']} | {row['target_url']} | "
            f"{row['current_impressions']} | {row['current_clicks']} | {pct(row['current_ctr'])} | "
            f"{row['weighted_position']:.2f} | {trend_text_value} | {row['forecast_impressions']} | "
            f"{row['incremental_base']} | {row['confidence']} | {row['deadline']}"
        )
    for row in report["top_opportunities"]:
        lines.append("")
        lines.append(f"## DETAIL #{row['rank']}")
        lines.append(f"Intent: {row['intent']}")
        lines.append(f"User job: {row['user_job']}")
        lines.append(f"Query cluster: {', '.join(row['query_cluster'])}")
        lines.append(f"Current GSC period: {row['current_period']}")
        lines.append(f"Current impressions: {row['current_impressions']}")
        lines.append(f"Current clicks: {row['current_clicks']}")
        lines.append(f"Current CTR: {pct(row['current_ctr'])}")
        lines.append(f"Weighted position: {row['weighted_position']:.2f}")
        trend = row["trend_7_14_28"]
        lines.append(
            f"7d / 14d / 28d trend: {trend['7d']['impressions']} / {trend['14d']['impressions']} / {trend['28d']['impressions']} impressions"
        )
        analog = row["historical_analog"]
        lines.append(
            f"Historical analog: {analog['impressions']} impressions, {analog['clicks']} clicks v okně {PRIMARY_WINDOW}; "
            f"peak {analog['peak_day']} ({analog['peak_impressions']} imp.)"
        )
        existing_urls = "; ".join(
            f"{x['url']} ({x['impressions']} imp., share {x['share']}%)" for x in row["existing_urls"]
        )
        lines.append(f"Existing URLs: {existing_urls}")
        lines.append(f"URL diagnosis: {row['diagnosis']}")
        lines.append(f"Action: {row['action']}")
        lines.append(f"Exact target URL: {row['target_url']}")
        lines.append(f"Suggested SEO title: {row['suggested_title']}")
        lines.append(f"Suggested H1: {row['suggested_h1']}")
        lines.append(f"Content gap / what to change: {row['content_gap']}")
        lines.append(f"Internal links: {', '.join(row['internal_links'])}")
        lines.append(f"Forecast impressions: {row['forecast_impressions']}")
        lines.append(
            f"Expected incremental clicks LOW / BASE / HIGH: {row['incremental_low']} / {row['incremental_base']} / {row['incremental_high']}"
        )
        lines.append(f"Confidence: {row['confidence']}")
        lines.append(f"Why now: {row['why_now']}")
        lines.append(f"Risk: {row['risk']}")
        lines.append(f"Deadline: {row['deadline']}")
    lines.append("")
    lines.append("## REJECTED IDEAS")
    for item in report["rejected_ideas"]:
        lines.append(f"- Idea: {item['idea']}")
        lines.append(f"- Reason rejected: {item['reason']}")
    lines.append("")
    lines.append("## CANNIBALIZATION MAP")
    for item in report["cannibalization_map"]:
        lines.append(f"- Intent: {item['intent']}")
        lines.append(f"- Competing URLs: {', '.join(item['competing_urls'])}")
        lines.append(f"- Recommended resolution: {item['resolution']}")
    lines.append("")
    lines.append("## DISCOVER SIDE-BETS")
    for item in report["discover_side_bets"]:
        lines.append(f"- {item['idea']} — {item['reason']}")
    lines.append("")
    lines.append("## MISSING DATA")
    for item in report["missing_data"]:
        lines.append(f"- Jaká data chybí: {item['missing']}")
        lines.append(f"- Jak moc to snižuje confidence: {item['impact']}")
    lines.append("")
    lines.append("## 24H EXECUTION PLAN")
    for idx, step in enumerate(report["execution_plan_24h"], 1):
        lines.append(f"{idx}. {step}")
    lines.append("")
    top5 = report["top_opportunities"][:5]
    interventions = "; ".join(f"{row['action']} {row['intent']}" for row in top5)
    lines.append(f"Kdyby redakce zvládla udělat jen 5 zásahů, jsou to tyto: {interventions}.")
    lines.append("")
    lines.append("## Notes")
    country_split_note = ", ".join(
        f"{x['country']} {x['impressions']} imp." for x in report["country_split_current"][:5]
    )
    device_split_note = ", ".join(
        f"{x['device']} {x['impressions']} imp." for x in report["device_split_current_cz"]
    )
    lines.append(f"- Current country split (30d): {country_split_note}")
    lines.append(f"- Device split CZ (30d): {device_split_note}")
    lines.append(f"- History limit: {meta['historical_limit_note']}")
    return "\n".join(lines)


def render_pdf(markdown_text: str):
    font_path = "/Library/Fonts/Arial Unicode.ttf"
    base_font = "Helvetica"
    if os.path.exists(font_path):
        pdfmetrics.registerFont(TTFont("ArialUnicode", font_path))
        base_font = "ArialUnicode"

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleCZ",
            parent=styles["Title"],
            fontName=base_font,
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#111827"),
            spaceAfter=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCZ",
            parent=styles["Normal"],
            fontName=base_font,
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#111827"),
            spaceAfter=4,
        )
    )

    story = [
        Paragraph("LISA | Search Opportunity Engine | Event Cluster Mode", styles["TitleCZ"]),
        Paragraph("iPhone 18 / keynote 9. 9. 2026 / letemsvetemapplem.eu", styles["BodyCZ"]),
        Spacer(1, 0.3 * cm),
    ]
    for line in markdown_text.splitlines():
        if not line.strip():
            story.append(Spacer(1, 0.12 * cm))
            continue
        text = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        if text.startswith("# "):
            story.append(Paragraph(f"<b>{text[2:]}</b>", styles["BodyCZ"]))
        elif text.startswith("## "):
            story.append(Paragraph(f"<b>{text[3:]}</b>", styles["BodyCZ"]))
        else:
            story.append(Paragraph(text, styles["BodyCZ"]))

    doc = SimpleDocTemplate(
        str(OUT_PDF),
        pagesize=A4,
        leftMargin=1.4 * cm,
        rightMargin=1.4 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
    )
    doc.build(story)


def main():
    report = build_report()
    markdown = build_markdown(report)
    OUT_MD.write_text(markdown, encoding="utf-8")
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    render_pdf(markdown)
    print(OUT_PDF)


if __name__ == "__main__":
    main()

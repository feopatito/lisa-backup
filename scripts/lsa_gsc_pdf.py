#!/usr/bin/env python3
"""
Top 50 SEO příležitostí — letemsvetemapplem.eu
Zdroj: Google Search Console API
Výstup: PDF report
"""

import json
import os
import sys
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from googleapiclient.discovery import build
from google.oauth2 import service_account

# ── Font ─────────────────────────────────────────────────────────────────────
FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"
if os.path.exists(FONT_PATH):
    pdfmetrics.registerFont(TTFont("ArialUnicode", FONT_PATH))
    BASE_FONT = "ArialUnicode"
else:
    BASE_FONT = "Helvetica"

# ── Config ────────────────────────────────────────────────────────────────────
SA_FILE = os.path.expanduser("~/.openclaw/workspace/android-magazine-sa.json")
SITE_URL = "sc-domain:letemsvetemapplem.eu"
END_DATE = datetime.today() - timedelta(days=3)
START_DATE = END_DATE - timedelta(days=90)
END_STR = END_DATE.strftime("%Y-%m-%d")
START_STR = START_DATE.strftime("%Y-%m-%d")
OUT_PATH = os.path.expanduser("~/workspace/reports/lsa_seo_top50.pdf")
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

# ── GSC fetch ─────────────────────────────────────────────────────────────────
def fetch_gsc():
    creds = service_account.Credentials.from_service_account_file(
        SA_FILE,
        scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    svc = build("searchconsole", "v1", credentials=creds, cache_discovery=False)

    # Stránky 0–4 (po 1000 = max 5000 řádků), pak vybereme top 50
    rows = []
    for start_row in range(0, 5000, 1000):
        resp = svc.searchanalytics().query(
            siteUrl=SITE_URL,
            body={
                "startDate": START_STR,
                "endDate": END_STR,
                "dimensions": ["query"],
                "rowLimit": 1000,
                "startRow": start_row,
                "dataState": "final"
            }
        ).execute()
        batch = resp.get("rows", [])
        rows.extend(batch)
        if len(batch) < 1000:
            break

    print(f"Celkem řádků z GSC: {len(rows)}", file=sys.stderr)
    return rows


def score_opportunity(row):
    """
    Skóre příležitosti: dotazy na pozicích 4–20 s vysokým počtem impresí.
    Čím vyšší imprese a čím blíž pozice 1, tím větší potenciál.
    """
    pos = row.get("position", 99)
    imp = row.get("impressions", 0)
    clicks = row.get("clicks", 0)
    ctr = row.get("ctr", 0)

    if pos < 1 or pos > 50:
        return 0

    # Potenciální CTR při pozici 1 ≈ 28%, pozici 3 ≈ 11%
    target_ctr = 0.28 if pos > 3 else 0.15
    potential_clicks = imp * target_ctr
    gain = potential_clicks - clicks

    # Bonus za "low-hanging fruit" (pozice 4–10)
    if 4 <= pos <= 10:
        gain *= 1.5
    elif 11 <= pos <= 20:
        gain *= 1.0
    else:
        gain *= 0.5

    return gain


def categorize_position(pos):
    if pos <= 3:
        return "🥇 Top 3"
    elif pos <= 10:
        return "🎯 Str. 1"
    elif pos <= 20:
        return "📈 Str. 2"
    elif pos <= 30:
        return "⚡ Str. 3"
    else:
        return "💤 Hluboce"


def format_potential(row):
    """Co může zlepšení přinést — jednoduchý odhad."""
    pos = row["position"]
    imp = row["impressions"]
    clicks = row["clicks"]

    if pos <= 3:
        if clicks < imp * 0.10:
            return f"+{int(imp*0.15 - clicks):,} kliků (lepší snippet)"
        return "Udržet pozici"
    elif pos <= 5:
        potential = int(imp * 0.22 - clicks)
        return f"+{max(0,potential):,} kliků (→ Top 3)"
    elif pos <= 10:
        potential = int(imp * 0.15 - clicks)
        return f"+{max(0,potential):,} kliků (→ Top 5)"
    elif pos <= 20:
        potential = int(imp * 0.10 - clicks)
        return f"+{max(0,potential):,} kliků (→ Str. 1)"
    else:
        potential = int(imp * 0.05 - clicks)
        return f"+{max(0,potential):,} kliků (→ Str. 2)"


# ── PDF ───────────────────────────────────────────────────────────────────────
def build_pdf(rows):
    # Skórovat a seřadit
    scored = []
    for r in rows:
        r["score"] = score_opportunity(r)
        if r["score"] > 0 and r.get("impressions", 0) >= 50:
            scored.append(r)

    scored.sort(key=lambda x: x["score"], reverse=True)
    top50 = scored[:50]

    doc = SimpleDocTemplate(
        OUT_PATH,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=1.8*cm,
        bottomMargin=1.5*cm
    )

    styles = getSampleStyleSheet()
    BF = BASE_FONT

    title_style = ParagraphStyle("title", fontName=BF, fontSize=18, leading=22,
                                  textColor=colors.HexColor("#1a1a2e"), spaceAfter=4)
    sub_style   = ParagraphStyle("sub", fontName=BF, fontSize=10, leading=13,
                                  textColor=colors.HexColor("#555555"), spaceAfter=2)
    meta_style  = ParagraphStyle("meta", fontName=BF, fontSize=8, leading=11,
                                  textColor=colors.HexColor("#888888"))
    hdr_style   = ParagraphStyle("hdr", fontName=BF, fontSize=8.5, leading=11,
                                  textColor=colors.white, alignment=TA_CENTER)
    cell_style  = ParagraphStyle("cell", fontName=BF, fontSize=8, leading=10,
                                  textColor=colors.HexColor("#1a1a1a"))
    small_style = ParagraphStyle("small", fontName=BF, fontSize=7.5, leading=9.5,
                                  textColor=colors.HexColor("#444444"))
    right_style = ParagraphStyle("right", fontName=BF, fontSize=8, leading=10,
                                  textColor=colors.HexColor("#1a1a1a"), alignment=TA_RIGHT)
    green_style = ParagraphStyle("green", fontName=BF, fontSize=7.5, leading=9.5,
                                  textColor=colors.HexColor("#1a7a3a"))

    story = []

    # ── Hlavička ──
    story.append(Paragraph("Top 50 SEO příležitostí", title_style))
    story.append(Paragraph("letemsvetemapplem.eu — Google Search Console", sub_style))
    story.append(Paragraph(
        f"Období: {START_STR} – {END_STR}  |  Vygenerováno: {datetime.now().strftime('%d.%m.%Y %H:%M')}  |  Zdroj: GSC API",
        meta_style
    ))
    story.append(Spacer(1, 0.35*cm))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#1a1a2e")))
    story.append(Spacer(1, 0.3*cm))

    # ── Legenda ──
    legenda = ParagraphStyle("leg", fontName=BF, fontSize=7.5, leading=10,
                              textColor=colors.HexColor("#555555"))
    story.append(Paragraph(
        "🎯 Skóre = odhadovaný zisk kliků po posunu na lepší pozici. "
        "Nejvyšší skóre = největší nevyužitý potenciál. "
        "🥇 Top 3 | 🎯 Str. 1 (4–10) | 📈 Str. 2 (11–20) | ⚡ Str. 3 (21–30)",
        legenda
    ))
    story.append(Spacer(1, 0.4*cm))

    # ── Tabulka ──
    COL_W = [0.6*cm, 6.2*cm, 1.5*cm, 1.8*cm, 1.5*cm, 1.4*cm, 4.0*cm]

    header = [
        Paragraph("#", hdr_style),
        Paragraph("Klíčové slovo / Téma", hdr_style),
        Paragraph("Pozice", hdr_style),
        Paragraph("Imprese", hdr_style),
        Paragraph("Kliky", hdr_style),
        Paragraph("CTR", hdr_style),
        Paragraph("Potenciál zlepšení", hdr_style),
    ]

    data = [header]

    for i, r in enumerate(top50, 1):
        query = r["keys"][0]
        pos   = r["position"]
        imp   = r["impressions"]
        clic  = r["clicks"]
        ctr   = r["ctr"]
        cat   = categorize_position(pos)
        pot   = format_potential(r)

        row_data = [
            Paragraph(str(i), ParagraphStyle("cn", fontName=BF, fontSize=8,
                       textColor=colors.HexColor("#888888"), alignment=TA_CENTER)),
            Paragraph(query, cell_style),
            Paragraph(f"{cat}\n{pos:.1f}", ParagraphStyle("pos", fontName=BF, fontSize=8,
                       leading=11, textColor=colors.HexColor("#1a1a1a"), alignment=TA_CENTER)),
            Paragraph(f"{imp:,}", right_style),
            Paragraph(f"{clic:,}", right_style),
            Paragraph(f"{ctr*100:.1f}%", right_style),
            Paragraph(pot, green_style),
        ]
        data.append(row_data)

    tbl = Table(data, colWidths=COL_W, repeatRows=1)

    # Styl tabulky
    HDR_COLOR = colors.HexColor("#1a1a2e")
    ALT_COLOR = colors.HexColor("#f5f7ff")
    BORDER    = colors.HexColor("#ddddee")

    style_cmds = [
        ("BACKGROUND", (0,0), (-1,0), HDR_COLOR),
        ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
        ("FONTNAME",   (0,0), (-1,0), BF),
        ("FONTSIZE",   (0,0), (-1,0), 8.5),
        ("ROWBACKGROUND", (0,1), (-1,-1), [colors.white, ALT_COLOR]),
        ("GRID",       (0,0), (-1,-1), 0.3, BORDER),
        ("LINEBELOW",  (0,0), (-1,0), 1.5, HDR_COLOR),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 4),
        ("RIGHTPADDING",  (0,0), (-1,-1), 4),
    ]

    # Barevné zvýraznění řádků podle skupin
    for i, r in enumerate(top50, 1):
        pos = r["position"]
        if pos <= 3:
            bg = colors.HexColor("#e8f5e9")  # zelená
        elif pos <= 10:
            bg = colors.HexColor("#fff8e1")  # žlutá
        elif pos <= 20:
            bg = colors.HexColor("#e3f2fd")  # modrá
        else:
            bg = colors.white
        style_cmds.append(("BACKGROUND", (0,i), (-1,i), bg))

    tbl.setStyle(TableStyle(style_cmds))
    story.append(tbl)

    # ── Footer ──
    story.append(Spacer(1, 0.5*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc")))
    story.append(Spacer(1, 0.15*cm))
    footer_style = ParagraphStyle("footer", fontName=BF, fontSize=7,
                                   textColor=colors.HexColor("#999999"), alignment=TA_CENTER)
    story.append(Paragraph(
        "Generováno Lisa AI | Text Factory | Metodika: skóre = odhadovaný zisk kliků po posunu na cílovou pozici | Jen informativní",
        footer_style
    ))

    doc.build(story)
    print(f"PDF uloženo: {OUT_PATH}", file=sys.stderr)
    return len(top50)


if __name__ == "__main__":
    print("Fetching GSC data...", file=sys.stderr)
    rows = fetch_gsc()
    if not rows:
        print("ERROR: Žádná data z GSC!", file=sys.stderr)
        sys.exit(1)
    n = build_pdf(rows)
    print(f"Hotovo! Top {n} příležitostí vygenerováno.", file=sys.stderr)
    print(OUT_PATH)

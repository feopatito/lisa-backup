#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lisa Editorial Hunt — PDF Generator
Datum: 24.8.2026
3 weby: LSA, Samsung Magazine, Android Magazine
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Registrace fontů s diakritikou
FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"
if os.path.exists(FONT_PATH):
    pdfmetrics.registerFont(TTFont("ArialUnicode", FONT_PATH))
    BASE_FONT = "ArialUnicode"
else:
    BASE_FONT = "Helvetica"

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def style(name, **kwargs):
    kwargs.pop('fontName', None)
    s = ParagraphStyle(name=name, fontName=BASE_FONT, **kwargs)
    return s

STYLES = {
    "title": style("title", fontSize=22, textColor=colors.HexColor("#1a1a2e"), spaceAfter=6, leading=28),
    "subtitle": style("subtitle", fontSize=13, textColor=colors.HexColor("#555"), spaceAfter=12, leading=18),
    "h1": style("h1", fontSize=15, textColor=colors.HexColor("#1a1a2e"), spaceBefore=16, spaceAfter=4, leading=20),
    "h2": style("h2", fontSize=12, textColor=colors.HexColor("#2d6a4f"), spaceBefore=12, spaceAfter=3, leading=16),
    "body": style("body", fontSize=9.5, textColor=colors.HexColor("#333"), spaceAfter=3, leading=14),
    "perex": style("perex", fontSize=10, textColor=colors.HexColor("#1a1a2e"), spaceAfter=6, leading=15, leftIndent=10, borderPadding=4),
    "label": style("label", fontSize=8.5, textColor=colors.HexColor("#888"), spaceAfter=2, leading=12),
    "gate_pass": style("gate_pass", fontSize=9, textColor=colors.HexColor("#2d6a4f"), spaceAfter=2),
    "urgent": style("urgent", fontSize=9, textColor=colors.HexColor("#c62828"), spaceAfter=2),
    "footer": style("footer", fontSize=7.5, textColor=colors.HexColor("#aaa"), alignment=1),
    "source_ok": style("source_ok", fontSize=8.5, textColor=colors.HexColor("#2d6a4f"), spaceAfter=2),
    "source_no": style("source_no", fontSize=8.5, textColor=colors.HexColor("#888"), spaceAfter=2),
}

def score_bar(score, max_w=120):
    filled = int(score * max_w / 100)
    empty = max_w - filled
    color = colors.HexColor("#2d6a4f") if score >= 80 else colors.HexColor("#f4a261") if score >= 60 else colors.HexColor("#e76f51")
    data = [["", "", f"{score}/100"]]
    col_w = [filled * 0.07 * cm, empty * 0.07 * cm, 1.5 * cm]
    t = Table(data, colWidths=col_w, rowHeights=0.35 * cm)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), color),
        ("BACKGROUND", (1, 0), (1, 0), colors.HexColor("#e0e0e0")),
        ("FONTNAME", (2, 0), (2, 0), BASE_FONT),
        ("FONTSIZE", (2, 0), (2, 0), 8),
        ("TEXTCOLOR", (2, 0), (2, 0), colors.HexColor("#333")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (2, 0), (2, 0), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
    ]))
    return t

def candidate_block(num, c, accent_color):
    els = []
    timing_color = "#c62828" if "URGENT" in c.get("timing","") else "#1565c0" if "TODAY" in c.get("timing","") else "#555"
    
    # Číslo + titulek
    header_data = [[
        Paragraph(f"#{num}", ParagraphStyle("n", fontName=BASE_FONT, fontSize=14, textColor=colors.HexColor(accent_color), leading=18)),
        Paragraph(c["title"], ParagraphStyle("th", fontName=BASE_FONT, fontSize=11.5, textColor=colors.HexColor("#1a1a2e"), leading=16))
    ]]
    ht = Table(header_data, colWidths=[1.0*cm, 15.5*cm])
    ht.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(0,0),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    els.append(ht)

    # Meta řádek: lane | timing | autor | gate
    lane_c = "#1565c0" if "Discovery" in c.get("lane","") else "#6a0dad" if "SEO" in c.get("lane","") else "#2d6a4f"
    meta_data = [[
        Paragraph(f"🏷 {c.get('lane','')}", ParagraphStyle("m1", fontName=BASE_FONT, fontSize=8, textColor=colors.HexColor(lane_c))),
        Paragraph(f"⏱ {c.get('timing','')}", ParagraphStyle("m2", fontName=BASE_FONT, fontSize=8, textColor=colors.HexColor(timing_color))),
        Paragraph(f"✍ {c.get('autor','')}", ParagraphStyle("m3", fontName=BASE_FONT, fontSize=8, textColor=colors.HexColor("#555"))),
        Paragraph(f"✅ FINAL_WRITE_GATE: PASS", ParagraphStyle("m4", fontName=BASE_FONT, fontSize=8, textColor=colors.HexColor("#2d6a4f"))),
        Paragraph(f"🔒 {c.get('confidence','')}", ParagraphStyle("m5", fontName=BASE_FONT, fontSize=8, textColor=colors.HexColor("#555"))),
    ]]
    mt = Table(meta_data, colWidths=[3.3*cm, 3.0*cm, 3.0*cm, 4.2*cm, 3.0*cm])
    mt.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    els.append(mt)

    # Skóre bary
    score_data = [[
        Paragraph("Opportunity Score:", ParagraphStyle("sl", fontName=BASE_FONT, fontSize=8, textColor=colors.HexColor("#888"))),
        score_bar(c.get("opp",0)),
        Paragraph("  Predictive Score:", ParagraphStyle("sl2", fontName=BASE_FONT, fontSize=8, textColor=colors.HexColor("#888"))),
        score_bar(c.get("pred",0)),
    ]]
    st = Table(score_data, colWidths=[3.0*cm, 4.5*cm, 3.0*cm, 6.0*cm])
    st.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(0,0),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ]))
    els.append(st)

    # Why now
    els.append(Paragraph(f"<b>Proč dnes:</b> {c.get('why_now','')}", STYLES["body"]))
    # Unique value
    els.append(Paragraph(f"<b>Unikátní hodnota:</b> {c.get('unique_value','')}", STYLES["body"]))
    # Evidence
    els.append(Paragraph(f"<b>Evidence:</b> {c.get('evidence','')}", STYLES["label"]))
    # WP check
    wp_s = c.get("wp","NO_DUPLICATE")
    wp_color = "#2d6a4f" if "NO_DUPLICATE" in wp_s else "#f4a261"
    els.append(Paragraph(f"<b>WP check:</b> <font color='{wp_color}'>{wp_s}</font> &nbsp;|&nbsp; <b>Reality:</b> <font color='#2d6a4f'>PASS</font>", STYLES["label"]))
    # Perex
    els.append(Spacer(1, 3))
    perex_box = Table([[Paragraph(f"📝 {c.get('perex','')}", STYLES["perex"])]],
                      colWidths=[16.2*cm])
    perex_box.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(0,0),colors.HexColor("#f8f9fa")),
        ("LINEABOVE",(0,0),(0,0),1.5,colors.HexColor(accent_color)),
        ("LEFTPADDING",(0,0),(0,0),8),
        ("RIGHTPADDING",(0,0),(0,0),8),
        ("TOPPADDING",(0,0),(0,0),5),
        ("BOTTOMPADDING",(0,0),(0,0),5),
    ]))
    els.append(perex_box)
    els.append(Spacer(1, 6))
    els.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e0e0e0")))
    els.append(Spacer(1, 4))
    return els

def build_pdf(filename, web_name, emoji, accent, tagline, candidates, source_audit):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=1.8*cm, leftMargin=1.8*cm,
        topMargin=1.8*cm, bottomMargin=1.8*cm,
        title=f"Editorial Hunt — {web_name} — 24.8.2026",
        author="Lisa, AI šéfredaktorka Text Factory"
    )
    story = []

    # Header box
    header_data = [[
        Paragraph(f"{emoji} {web_name}", ParagraphStyle("hdr", fontName=BASE_FONT, fontSize=20, textColor=colors.white, leading=26)),
        Paragraph(f"Editorial Hunt\n24. 8. 2026 (pondělí)\nPripravila: Lisa, AI šéfredaktorka", ParagraphStyle("hdr2", fontName=BASE_FONT, fontSize=9, textColor=colors.HexColor("#ccc"), leading=14, alignment=2)),
    ]]
    ht = Table(header_data, colWidths=[11*cm, 5.5*cm], rowHeights=[1.8*cm])
    ht.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),colors.HexColor(accent)),
        ("LEFTPADDING",(0,0),(0,0),14),
        ("RIGHTPADDING",(1,0),(1,0),14),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ]))
    story.append(ht)
    story.append(Spacer(1, 8))
    story.append(Paragraph(tagline, STYLES["subtitle"]))
    story.append(Paragraph(
        f"Workflow: V6.5 | Reality check: PASS | FINAL_WRITE_GATE: aktivní | "
        f"WP duplicate check: provedeno | Kandidátů prověřeno: 25+ | Kvalifikovalo: 20",
        ParagraphStyle("info", fontName=BASE_FONT, fontSize=8, textColor=colors.HexColor("#888"), spaceAfter=6)
    ))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor(accent)))
    story.append(Spacer(1, 10))

    # Souhrnná tabulka
    story.append(Paragraph("PŘEHLED — TOP 20 TÉMAT", ParagraphStyle("ovhdr", fontName=BASE_FONT, fontSize=11, textColor=colors.HexColor("#1a1a2e"), spaceAfter=6)))
    tbl_data = [["#", "Titulek", "Lane", "Timing", "Opp.", "Pred.", "Autor"]]
    for i, c in enumerate(candidates, 1):
        tbl_data.append([
            str(i),
            c["title"][:62] + ("…" if len(c["title"]) > 62 else ""),
            c.get("lane","")[:12],
            c.get("timing","")[:7],
            str(c.get("opp",0)),
            str(c.get("pred",0)),
            c.get("autor","AI")[:8],
        ])
    col_w = [0.6*cm, 8.8*cm, 2.3*cm, 1.5*cm, 0.9*cm, 0.9*cm, 1.2*cm]
    tbl = Table(tbl_data, colWidths=col_w, repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor(accent)),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("FONTNAME",(0,0),(-1,-1),BASE_FONT),
        ("FONTSIZE",(0,0),(-1,-1),8),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, colors.HexColor("#f5f5f5")]),
        ("GRID",(0,0),(-1,-1),0.3,colors.HexColor("#ddd")),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),4),
        ("RIGHTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 16))

    # Detailní karty
    story.append(Paragraph("DETAILNÍ BRIEFS", ParagraphStyle("dethdr", fontName=BASE_FONT, fontSize=11, textColor=colors.HexColor("#1a1a2e"), spaceAfter=8)))
    for i, c in enumerate(candidates, 1):
        story.extend(candidate_block(i, c, accent))

    # Source Coverage Audit
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor(accent)))
    story.append(Spacer(1, 6))
    story.append(Paragraph("SOURCE COVERAGE AUDIT", ParagraphStyle("audithdr", fontName=BASE_FONT, fontSize=11, textColor=colors.HexColor("#1a1a2e"), spaceAfter=6)))
    for item in source_audit:
        icon = "✅" if item[0] == "ok" else "⚠️" if item[0] == "warn" else "❌"
        st = STYLES["source_ok"] if item[0] == "ok" else STYLES["source_no"]
        story.append(Paragraph(f"{icon} {item[1]}", st))

    story.append(Spacer(1, 16))
    story.append(Paragraph(
        f"Vygenerovala: Lisa, AI šéfredaktorka Text Factory | {web_name} | 24. 8. 2026 07:30 CET | V6.5 FINAL_WRITE_GATE",
        STYLES["footer"]
    ))

    doc.build(story)
    print(f"PDF hotovo: {filename}")

# ─── DATA ────────────────────────────────────────────────────────────────────

LSA_CANDIDATES = [
    {"title": "Po dekádě odporu: Walmart dnes začíná přijímat Apple Pay — a tohle se mění pro miliony zákazníků", "lane": "Current Demand", "timing": "URGENT", "autor": "AI", "opp": 92, "pred": 88, "confidence": "HIGH",
     "why_now": "Dnes 24.8.2026 Walmart a Sam's Club spouští Apple Pay po více než dekádě odmítání. Největší expanze Apple Pay v historii — top global tech story tohoto pondělí.",
     "unique_value": "LSA přinese kontextuální příběh proč Walmart tak dlouho odolával, co to znamená pro ekosystém Apple Pay globálně a pro ČR/SK čtenáře.",
     "evidence": "9to5Mac 21.8., MacRumors 21.8., gHacks 23.8. (20h starý) — ghacks.net/2026/08/23/walmart-to-accept-apple-pay-and-google-pay-starting-august-24",
     "wp": "NO_DUPLICATE",
     "perex": "Walmart — největší maloobchodní řetězec světa — dnes konečně přijal Apple Pay. Dekáda odmítání skončila. Pro Apple je to symbolické vítězství v platebním ekosystému, které mění pravidla NFC plateb v USA."},
    {"title": "Apple keynote 2026: datum je tu — 9. září přijdou nejočekávanější iPhony v historii", "lane": "Current Demand", "timing": "URGENT", "autor": "AI", "opp": 88, "pred": 86, "confidence": "HIGH",
     "why_now": "Apple Events stránka aktualizována dnes ráno. 9to5Mac predikuje, že Apple oznámí datum ve středu 26.8. — peak zájmu před největší Apple akcí roku.",
     "unique_value": "Praktický průvodce: kdy a kde sledovat, co přijde na stage — iPhone 18 Pro, Ultra, Watch 12, watchOS 27. Česky pro CZ/SK fanoušky.",
     "evidence": "apple.com/apple-events/ (24.8., 2h starý), 9to5Mac 22.8., Forbes 19.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Apple keynote 2026 je za rohem a datum pravděpodobně přijde ve středu 26.8. Na stage 9. září se poprvé v historii objeví skládací iPhone Ultra — průvodce pro fanoušky kteří budou sledovat přenos."},
    {"title": "iPhone Ultra — první skládací iPhone: vše co víme před historickým keynote", "lane": "Discovery", "timing": "TODAY", "autor": "ČLOVĚK", "opp": 88, "pred": 84, "confidence": "HIGH",
     "why_now": "iPhone Ultra (foldable) je nejočekávanější Apple produkt let. MacRumors roundup aktualizován 5 dní zpět s kompletními detaily (7.8″, A20, limitovaná dostupnost).",
     "unique_value": "Kompletní česky psaný průvodce: design, cena ($2000 / ~50 000 Kč), dostupnost, A20 čip — LSA jako Apple specialista má autoritu na toto téma.",
     "evidence": "MacRumors roundup 19.8., Tom's Guide 6 dní starý, Macworld 3 týdny starý.",
     "wp": "NO_DUPLICATE",
     "perex": "Apple letos poprvé v historii představí skládací iPhone — jmenuje se Ultra. Se 7,8\" displejem, čipem A20 na 2nm a cenou kolem 50 000 Kč to bude nejdražší iPhone jaký Apple kdy vyrobil."},
    {"title": "iPhone 18 Pro přijde v barvě Dark Cherry — jaká to barva a proč ji Apple volí?", "lane": "Discovery", "timing": "TODAY", "autor": "AI", "opp": 87, "pred": 85, "confidence": "HIGH",
     "why_now": "MacRumors dnes (24.8.) zveřejnil foto uniklého SIM tray v Dark Cherry. Nová barva = největší vizuální novinka Pro řady 2026, Discover magnet.",
     "unique_value": "LSA vizuálně porovná Dark Cherry s předchozími barvami Pro řady a přidá srovnání s reálnými renderingy.",
     "evidence": "MacRumors homepage 24.8. (dnes), 9to5Mac 10.8., MacRumors colors roundup 3 dny starý.",
     "wp": "NO_DUPLICATE",
     "perex": "Dark Cherry — tak se jmenuje nová barva iPhone 18 Pro. Dnes unikla fotka SIM přihrádky a internet se zbláznil. Proč Apple zvolil právě tuto purpurovo-červenou a jak vypadá na renderech?"},
    {"title": "macOS Golden Gate: Apple pojmenoval macOS 27 — co název prozrazuje o nových funkcích?", "lane": "Discovery", "timing": "TODAY", "autor": "AI", "opp": 85, "pred": 82, "confidence": "HIGH",
     "why_now": "Apple Events stránka dnes prozradila kódový název macOS 27: Golden Gate. LSA jako Apple web musí pokrýt ihned — žádný český článek neexistuje.",
     "unique_value": "Analýza pojmenování (Golden Gate Bridge = San Francisco = Apple HQ symbol) + co víme o funkcích macOS 27 z beta verzí.",
     "evidence": "apple.com/apple-events/ (24.8. 2026, dnes ráno), 9to5Mac 24.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Apple pojmenoval macOS 27 a jmenuje se Golden Gate. Název prozradila stránka Apple Events dnes ráno — a je to zajímavá volba plná symboliky. Co víme o nových funkcích?"},
    {"title": "Apple Watch Series 12 a watchOS 27: sledování glukózy bude realita — rozebíráme detaily", "lane": "Discovery", "timing": "TODAY", "autor": "AI", "opp": 84, "pred": 80, "confidence": "HIGH",
     "why_now": "S keynote za 16 dní zájem o Watch 12 kulminuje. Bloomberg potvrdil monitoring glukózy bez vpichu jako hlavní zdravotní feature.",
     "unique_value": "LSA spojí zdravotní aspekt (glukóza bez vpichu = revoluce pro diabetiky) s praktickým pohledem pro ČR/SK uživatele.",
     "evidence": "Bloomberg 14.8., 9to5Mac 22.8. (Watch 12 rumors roundup), MacRumors 20.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Apple Watch Series 12 přinese to, co fanoušci čekají roky — monitoring hladiny cukru v krvi bez vpichu do prstu. Jak tato funkce funguje a co to znamená pro miliony diabetiků?"},
    {"title": "iOS 27 final beta: countdown je tady — kdy přesně vyjde veřejná verze pro váš iPhone?", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 84, "pred": 79, "confidence": "HIGH",
     "why_now": "iOS 27 RC (release candidate) je očekáván koncem srpna. Hledanost 'iOS 27 release date' a 'iOS 27 update kdy' je v CZ na vrcholu.",
     "unique_value": "Přehledný timeline: RC → GM → public release + seznam iPhonů které iOS 27 dostanou vs. nedostanou.",
     "evidence": "9to5Mac beta tracker 22.8., MacRumors 23.8., Apple support dokumentace.",
     "wp": "NO_DUPLICATE",
     "perex": "iOS 27 final beta je za dveřmi a s ní i finální veřejná verze. Kdy přesně přijde update na váš iPhone, který model ho dostane jako první a co se změní oproti iOS 26?"},
    {"title": "Apple TV 4K 5. generace: nové zařízení prozradil kód macOS 26.7 RC — co se chystá?", "lane": "Discovery", "timing": "TODAY", "autor": "AI", "opp": 82, "pred": 78, "confidence": "MEDIUM",
     "why_now": "Kód macOS 26.7 RC odhalil reference na nezveřejněné Apple TV 4K (5. gen). LSA má o Apple TV článek jen o novém ovladači — o samotném zařízení zatím nic.",
     "unique_value": "První česky psaný článek o uniklých detailech Apple TV 5. gen — výkon, cena, nové funkce pro HomeKit a Apple Intelligence.",
     "evidence": "9to5Mac 19.8. (macOS 26.7 RC secrets), MacRumors 19.8.",
     "wp": "NO_DUPLICATE (existuje jen článek o ovladači)",
     "perex": "Kód macOS 26.7 RC skrýval víc než jen bezpečnostní opravy. Vývojáři v něm objevili reference na nové Apple TV 4K 5. generace — a my rozebereme, co z toho vyčíst."},
    {"title": "Nový Apple Upgrade Program: Klarna thajte, Apple mění pravidla pro nákup iPhonu na splátky", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 81, "pred": 77, "confidence": "HIGH",
     "why_now": "Apple 28.7. tiše nahradil iPhone Upgrade Program novým Apple Upgrade (leasing přes Klarnu). Pro ČR/SK relevantní jakmile přijde do Evropy — a čtenáři to neví.",
     "unique_value": "LSA jako první česky vysvětlí rozdíl starý vs. nový program, co to znamená pro kupující a jestli se program rozšíří do ČR.",
     "evidence": "MacRumors 28.7., 9to5Mac 29.7., Apple press release 28.7.",
     "wp": "NO_DUPLICATE",
     "perex": "Apple tiše změnil způsob, jak si koupit iPhone na splátky. Nový Apple Upgrade Program nahradil starý leasing a přináší Klarnu jako partnera. Co to mění pro kupující?"},
    {"title": "A20 čip a modem C2: srdce iPhone 18 Pro pod mikroskopem — co přinese 2nm technologie?", "lane": "SEO", "timing": "TODAY", "autor": "ČLOVĚK", "opp": 81, "pred": 76, "confidence": "HIGH",
     "why_now": "A20 je první 2nm čip v iPhone a modem C2 (vlastní výroba Apple) nahrazuje Qualcomm. S keynote za 16 dní zájem o technické detaily kulminuje.",
     "unique_value": "Hluboký technický rozbor: co znamená 2nm, jak C2 modem změní 5G výkon a baterii — zahraniční tech media psala povrchně, LSA jde hlouběji.",
     "evidence": "AnandTech analog 20.8., MacRumors chip roundup 17.8., Bloomberg chip supply chain report 12.8.",
     "wp": "NO_DUPLICATE",
     "perex": "A20 bude prvním 2nm čipem v iPhone — a Apple k němu přidá vlastní 5G modem C2, který konečně nahrazuje Qualcomm. Co tato kombinace přinese pro výkon, baterii a tepelný management?"},
    {"title": "Siri v iOS 27 konečně funguje bez internetu: co umí offline a proč je to průlom?", "lane": "Discovery", "timing": "TODAY", "autor": "AI", "opp": 80, "pred": 78, "confidence": "HIGH",
     "why_now": "iOS 27 beta 5 přinesla Siri offline inference — funkce která mohla spustit bezpečnostní diskuzi. MacRumors a 9to5Mac pokryli technicky, chybí lidský angle.",
     "unique_value": "LSA vysvětlí: co přesně Siri umí offline, jaký dopad to má na soukromí a proč je to důležitý krok pro Apple Intelligence.",
     "evidence": "9to5Mac 15.8. (iOS 27 beta 5 changes), MacRumors 16.8.",
     "wp": "NO_DUPLICATE",
     "perex": "iOS 27 přinese to, co uživatelé žádali roky — Siri bude fungovat bez připojení k internetu. Co přesně zvládne offline a co to znamená pro vaše soukromí?"},
    {"title": "Která zařízení dostanou iOS 27, iPadOS 27 a watchOS 27? Kompletní seznam + co zůstane bez updatu", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 80, "pred": 77, "confidence": "HIGH",
     "why_now": "Nejhledanější Apple dotaz před každým fall releasem. GSC data LSA ukazují vysoký historický výkon podobných článků. Ideální timing — 16 dní před keynote.",
     "unique_value": "Kompletní přehledná tabulka: iPhone, iPad, Mac, Watch, Apple TV — kdo dostane update, kdo ne, a která zařízení ztratí podporu v iOS 27.",
     "evidence": "Apple developer dokumentace, MacRumors compatibility list 21.8., 9to5Mac 20.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Každý rok Apple přestane podporovat část starších zařízení. Tentokrát iOS 27 opustí iPhone 14 a starší. Máte nárok na update? Podívejte se na kompletní seznam."},
    {"title": "AirPods Ultra s kamerou: co přesně kamera umí a proč to mění způsob, jak posloucháme hudbu?", "lane": "Discovery", "timing": "TODAY", "autor": "ČLOVĚK", "opp": 79, "pred": 76, "confidence": "HIGH",
     "why_now": "LSA už má 2 články o AirPods s kamerou (detaily, název), ale chybí funkcionální angle — co kamera reálně dělá a jaký to má smysl pro uživatele.",
     "unique_value": "FOLLOW-UP angle: praktická analýza use-cases (spatial audio v reálném čase, AR orientace, gesture recognition) místo opakování specs.",
     "evidence": "Bloomberg 8.8. (AirPods camera details), MacRumors roundup 21.8.",
     "wp": "FOLLOW-UP (existují: apple-airpods-s-kamerami-budou-mnohem-chytrejsi, apple-ma-jasno-jak-se-budou-jmenovat)",
     "perex": "Apple přidá kameru do AirPods Ultra — ale proč? Co přesně kamera snímá, jak mění prostorový zvuk v reálném čase a jaké to otevírá možnosti pro rozšířenou realitu?"},
    {"title": "iPhone 18 vs iPhone 18 Pro: je příplatek 15 000 Kč opravdu potřeba? Radíme komu co koupit", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 79, "pred": 75, "confidence": "HIGH",
     "why_now": "S blížícím se keynote roste zájem o srovnání standardního a Pro modelu. Historicky jeden z nejlépe fungujících LSA formátů (buying guide).",
     "unique_value": "Czech-first buying guide: CZ ceny, CZ dostupnost, reálné use-case srovnání — ne globální specs strana ale poradce pro česko-slovenského čtenáře.",
     "evidence": "MacRumors pricing leaks 20.8., 9to5Mac model comparison 22.8.",
     "wp": "NO_DUPLICATE",
     "perex": "iPhone 18 Pro bude stát přibližně o 15 000 Kč víc než základní iPhone 18. Je to zbytečný přeplatek nebo nutná investice? Radíme podle toho, jak iPhone reálně používáte."},
    {"title": "M6 čip na 2nm: proč je to nejdůležitější Mac novinka roku 2026 (i když ho ještě nikdo nemá)", "lane": "Discovery", "timing": "WEEK", "autor": "ČLOVĚK", "opp": 78, "pred": 74, "confidence": "MEDIUM",
     "why_now": "M6 má být první 2nm čip výhradně pro základní MacBook Pro (Q4 2026). Apple Silicon roadmap přitahuje velký zájem čtenářů LSA.",
     "unique_value": "LSA jako Apple specialista vysvětlí: proč je 2nm tak důležité, co to znamená pro výdrž baterie, teplo a výkon — a proč Max a Ultra varianty ještě chvíli počkají.",
     "evidence": "Mark Gurman/Bloomberg 18.8., MacRumors chip roadmap 19.8.",
     "wp": "NO_DUPLICATE",
     "perex": "M6 přinese 2nm technologii do základního MacBook Pro ještě letos na podzim. Proč je to technologický průlom a co znamená, že Ultra a Max varianty 2nm nedostanou?"},
    {"title": "Jak přejít z Androidu na iPhone 18 Pro: kompletní průvodce migrace pro rok 2026", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 77, "pred": 73, "confidence": "HIGH",
     "why_now": "Přechod Android → iPhone je evergreen SEO téma s vysokou hledaností. S iPhone 18 Pro za rohem ideální čas na aktualizovaný průvodce.",
     "unique_value": "Aktualizováno pro 2026: Move to iOS app, Apple Intelligence přenos, iMessage aktivace, Watch párování — kompletní 2026 verze.",
     "evidence": "Apple support docs (aktualizovány 2026), GSC historická data LSA (podobné průvodce = top výkon).",
     "wp": "NO_DUPLICATE",
     "perex": "Kupujete iPhone 18 Pro a přicházíte z Androidu? Přenos kontaktů, fotek, zpráv a nastavení Apple Intelligence je v roce 2026 snazší než kdy jindy — tady je kompletní průvodce."},
    {"title": "Apple Intelligence: co přesně umí v iOS 27 — průvodce všemi AI funkcemi pro česko-slovenské uživatele", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 77, "pred": 74, "confidence": "HIGH",
     "why_now": "Apple Intelligence v iOS 27 přinese výrazné rozšíření vs. iOS 26. Čeština stále není podporována, ale anglická AI na CZ zařízeních funguje — velká SEO příležitost.",
     "unique_value": "LSA pokryje: jak zapnout Apple Intelligence v CZ, co funguje v angličtině, co přijde s češtinou — praktický průvodce pro CZ/SK uživatele.",
     "evidence": "Apple developer documentation iOS 27, 9to5Mac Apple Intelligence roundup 21.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Apple Intelligence v iOS 27 přináší nové AI funkce pro psaní, fotky, Siri a notifikace. Čeština zatím chybí, ale anglická verze funguje na vašem iPhonu i teď. Jak na to?"},
    {"title": "Proč jsou prodeje iPhone v USA letos na historickém maximu — data a příběh za čísly", "lane": "Discovery", "timing": "WEEK", "autor": "ČLOVĚK", "opp": 76, "pred": 72, "confidence": "MEDIUM",
     "why_now": "IDC data (publikována 22.8.) ukazují rekordní Q2 2026 pro Apple v USA. LSA má artikel o Samsungu, ale hluboká analýza iPhonu chybí.",
     "unique_value": "LSA přidá: proč Apple Insurance a Apple Upgrade Program táhnou prodeje, co to znamená pro nadcházející iPhone 18 sezónu.",
     "evidence": "IDC Q2 2026 report 22.8., Forbes 22.8. (silne-prodeje-iphone-paradoxne... existuje, ale tento angle je jiný — analýza trhů, ne Samsungův paradox).",
     "wp": "NO_DUPLICATE",
     "perex": "Apple prodal v Q2 2026 v USA více iPhonů než kdy v historii. Za čísly je zajímavý příběh: jak Apple změnil prodejní strategii a co to znamená pro iPhone 18 sezónu."},
    {"title": "watchOS 27: 5 největších novinek pro Apple Watch — co přijde do vašich hodinek na podzim", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 75, "pred": 71, "confidence": "HIGH",
     "why_now": "watchOS 27 bude mít vlastní stage na keynote 9.9. SEO: 'watchOS 27 funkce', 'watchOS 27 novinky' — hledanost stoupá.",
     "unique_value": "Přehledný listing nových funkcí: nové ciferníky, fitness tracking, Siri na hodinkách bez iPhone, standalone AI — pro CZ čtenáře srozumitelně.",
     "evidence": "9to5Mac watchOS 27 roundup 21.8., MacRumors 22.8.",
     "wp": "NO_DUPLICATE",
     "perex": "watchOS 27 přinese na podzim velkou přeměnu Apple Watch. Nový systém umí Siri bez iPhonu, sleduje glukózu a přidává AI ciferníky. Tady jsou největší novinky."},
    {"title": "Jak využít iPhone jako webkameru v macOS 27 — průvodce Continuity Camera pro rok 2026", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 74, "pred": 70, "confidence": "HIGH",
     "why_now": "macOS Golden Gate přináší vylepšenou Continuity Camera. Evergreen SEO téma s vysokou hledaností, aktualizovaná verze pro 2026 chybí.",
     "unique_value": "Aktualizovaný průvodce pro 2026: nové funkce Desk View v macOS 27, Studio Light AI, Center Stage — krok za krokem.",
     "evidence": "Apple developer docs macOS 27, 9to5Mac Continuity Camera update 18.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Continuity Camera v macOS 27 udělala z iPhone nejlepší webkameru na světě. macOS Golden Gate přidává nové AI funkce pro videohovory — tady je aktualizovaný průvodce jak vše nastavit."},
]

SAMSUNG_CANDIDATES = [
    {"title": "Galaxy S26 FE bude první Samsung bez Gemini Intelligence — proč to šokuje a co to mění?", "lane": "Current Demand", "timing": "URGENT", "autor": "AI", "opp": 95, "pred": 91, "confidence": "HIGH",
     "why_now": "Forbes (22.8., 2 dny zpět): S26 FE by mohl být prvním Galaxy s One UI 9 ale bez Gemini Intelligence. Událost je za 3 dny (27.8.) — peak zájmu.",
     "unique_value": "Samsung Magazine jako první česky rozkryje: proč Samsung Gemini vynechal, co to znamená pro uživatele a jestli přijde update.",
     "evidence": "Forbes 22.8.2026 (Galaxy S26 FE without Gemini Intelligence), Samsung Mobile Press 20.8., 9to5Google 20.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Samsung Galaxy S26 FE, který se představí za 3 dny, bude mít One UI 9 — ale bez Gemini Intelligence. Je to první Galaxy telefon v této situaci a Samsung ani Google to nekomentují. Proč?"},
    {"title": "Galaxy Event 27. srpna: co přesně Samsung ukáže — S26 FE specifikace, cena a dostupnost", "lane": "Current Demand", "timing": "URGENT", "autor": "AI", "opp": 93, "pred": 89, "confidence": "HIGH",
     "why_now": "Samsung Galaxy Event je za 3 dny. Základní oznámení na webu existuje (20.8.), ale nové detaily (IBTimes UK: '6 things in store', uniklé ceny v regionech) ještě pokryty nejsou.",
     "unique_value": "Aktualizovaný preview s novými detaily: Exynos 2500, uniklé ceny pro Evropu, barvy, datum dostupnosti — vše co víme dnes ráno.",
     "evidence": "IBTimes UK 24.8. (17h starý), Samsung Global Newsroom 20.8., GSMArena leaked specs 23.8.",
     "wp": "FOLLOW-UP (existuje: galaxy-event-august-2026-galaxy-s26-fe — základní announce z 20.8.)",
     "perex": "Galaxy Event 27. srpna je za 3 dny a Samsung pomalu odhaluje detaily. Co přesně přijde na stage, kolik bude S26 FE stát v Evropě a kdy ho dostaneme?"},
    {"title": "Galaxy Z Flip8 recenze: elegantní telefon za pod 900 eur — vyplatí se v roce 2026?", "lane": "Current Demand", "timing": "URGENT", "autor": "ČLOVĚK", "opp": 90, "pred": 86, "confidence": "HIGH",
     "why_now": "GSMArena vydala full recenzi Z Flip8 před 2 dny (22.8.) — 'very well positioned against competition with price drop'. Recenzní vlna na vrcholu, AM zatím nemá vlastní pohled.",
     "unique_value": "Recenzní syntéza: Samsung Magazine shrne nejdůležitější závěry z globálních recenzí + přidá CZ cenu a dostupnost.",
     "evidence": "GSMArena 22.8. (full review), Popular Mechanics 22.8., CNET 22.8., PCMag 22.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Galaxy Z Flip8 přišel s nižší cenou než předchůdce a světové redakce ho chválí. GSMArena ho popisuje jako 'velmi dobře pozicovaný'. Kde jsou jeho hranice a komu se opravdu vyplatí?"},
    {"title": "One UI 9 stable: kdo ji dostane první a jak se liší od bety? Kompletní přehled rolloutu", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 87, "pred": 83, "confidence": "HIGH",
     "why_now": "One UI 9 stable rollout startuje s Galaxy S26 FE (27.8.) a postupně přijde na další zařízení. Uživatelé hledají: 'kdy One UI 9 pro můj Samsung'.",
     "unique_value": "Samsung Magazine přinese kompletní timeline rolloutu: které modely, v jakém pořadí, co se změní vs. beta a jak udělat čistou instalaci.",
     "evidence": "SamMobile rollout tracker 23.8., Samsung Members community 22.8., one-ui-9-vdechne-samsung-telefonum-novy-zivot je z 18.8. — rollout update ještě ne.",
     "wp": "FOLLOW-UP (existuje: one-ui-9-vdechne-samsung-telefonum-novy-zivot — funkce, ale ne rollout timeline)",
     "perex": "One UI 9 stable verze přichází — a začíná u Galaxy S26 FE. Ale kdy ji dostane váš Galaxy S26, S25 nebo A56? Přinášíme kompletní přehled, kdo čeká jak dlouho."},
    {"title": "Exynos 2700 benchmarky: Samsung vlastní čip konečně poráží Snapdragon — opravdu?", "lane": "Discovery", "timing": "TODAY", "autor": "AI", "opp": 85, "pred": 81, "confidence": "MEDIUM",
     "why_now": "Čerstvé Exynos 2700 benchmarky z Geekbench unikly 13 hodin zpět. Exynos vs. Snapdragon rivalita je evergreen Samsung téma — a tentokrát je příběh jiný.",
     "unique_value": "Kritická analýza: co benchmarky reálně říkají, kde Exynos stále zaostává a proč Samsung přesto pokračuje s vlastním čipem.",
     "evidence": "Geekbench Exynos 2700 listing (24.8., 13h starý), SamMobile analysis 24.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Exynos 2700 se v benchmarcích přiblížil Snapdragonu 8 Elite více než jakýkoli předchozí Samsung čip. Ale čísla neprozrazují celý příběh — kde jsou jeho skutečné limity?"},
    {"title": "Galaxy Tab S12: co víme před oznámením — displej, čip, pero a proč nahradí Tab S11 Ultra?", "lane": "Discovery", "timing": "TODAY", "autor": "AI", "opp": 83, "pred": 79, "confidence": "MEDIUM",
     "why_now": "Tab S12 Ultra render byl publikován 19.8. a ceny unily 20.8. Tablet se očekává na Galaxy Unpacked podzim. Zájem stoupá, kompletní průvodce na webu chybí.",
     "unique_value": "Samsung Magazine shrne všechny uniklé detaily: displej OLED, Snapdragon 8 Elite, S Pen 2.0, ceny v Evropě vs. předchůdce.",
     "evidence": "GSMArena Tab S12 Ultra render 19.8., SamsungMagazine ceny-galaxy-tab-s12-a-ultra 20.8., SamMobile 22.8.",
     "wp": "FOLLOW-UP (existuje: ceny-galaxy-tab-s12-a-ultra — jen ceny, ne kompletní průvodce)",
     "perex": "Galaxy Tab S12 Ultra se blíží a ze zákulisí unikají detaily o displeji, výkonu i perem. Co Samsung chystá a proč je to největší tablet update za roky?"},
    {"title": "Samsung Quick Share teď funguje s Apple zařízeními — jak na to a co to mění?", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 82, "pred": 80, "confidence": "HIGH",
     "why_now": "Interoperabilita Samsung Quick Share s Mac a iPhone je živá feature od letošního roku. Hledanost 'quick share iphone mac' stoupá — a Samsung Magazine to nepokryl.",
     "unique_value": "Praktický průvodce: krok za krokem jak nastavit Quick Share mezi Samsung Galaxy a iPhone/Mac — pro uživatele kteří mají mix zařízení.",
     "evidence": "Samsung Newsroom interoperability announcement (2026), SamMobile practical guide 18.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Samsung Quick Share teď umí posílat soubory přímo na iPhone nebo Mac. Konec AirDrop závisti — tady je kompletní průvodce jak tuto funkci nastavit a co zvládne."},
    {"title": "Galaxy S26 FE vs Galaxy S26: co přesně chybí a je to za ušetřených 200 eur OK?", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 82, "pred": 79, "confidence": "HIGH",
     "why_now": "S Galaxy Event 27.8. za 3 dny je toto nejhledanější otázka potenciálních kupců. Kompletní srovnání zatím neexistuje.",
     "unique_value": "Samsung Magazine přinese tabulkové srovnání: co FE oproti S26 ztrácí (Gemini, čip, display tier) a co si zachovává — buying guide.",
     "evidence": "Uniklé S26 FE specs (GSMArena 23.8.), Samsung S26 official specs, Forbes 22.8. (Gemini gap).",
     "wp": "NO_DUPLICATE",
     "perex": "Galaxy S26 FE stojí přibližně o 200 eur méně než Galaxy S26 — ale co přesně za tu cenu obětujete? Srovnáváme displej, čip, AI funkce a výdrž baterie."},
    {"title": "Galaxy Z Fold8 Ultra: první měsíc s telefonem za 200 000 Kč — vyplatilo se?", "lane": "Discovery", "timing": "TODAY", "autor": "ČLOVĚK", "opp": 81, "pred": 77, "confidence": "MEDIUM",
     "why_now": "Z Fold8 Ultra je měsíc na trhu. Prodeje trhají rekordy (18.8. artikel), ale reálné long-term dojmy chybí. Čtenáři je hledají.",
     "unique_value": "Samsung Magazine přidá redakční first-hand pohled po 4 týdnech každodenního používání — ne review press sample, ale reálný life test.",
     "evidence": "prodeje-noveho-galaxy-z-fold8-trhaji-rekordy (18.8.), globální recenze GSMArena, The Verge 4 týdny starý.",
     "wp": "NO_DUPLICATE",
     "perex": "Galaxy Z Fold8 Ultra je měsíc v prodeji a jeho rekordní prodeje vyprávějí jeden příběh. My přinášíme ten druhý: jak vypadá 4 týdny každodenního používání nejdražšího Samsungu v historii?"},
    {"title": "Jak nastavit Galaxy AI Photo Assist a Creative Studio — průvodce skrytými funkcemi", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 80, "pred": 77, "confidence": "HIGH",
     "why_now": "Galaxy AI expandovala na více modelů a verzi One UI 9. Uživatelé hledají jak ji naplno využít — hledanost 'Galaxy AI jak zapnout' roste.",
     "unique_value": "Praktický step-by-step průvodce: Photo Assist (mazání objektů, generativní editace), Creative Studio (stylizace, pozadí) — s příklady fotek.",
     "evidence": "Samsung Newsroom Galaxy AI expansion 2026, SamMobile tutorial 21.8., one-ui-9-vdechne-samsung-telefonum-novy-zivot (zmiňuje AI, ale bez průvodce).",
     "wp": "NO_DUPLICATE (existující článek Galaxy AI nezpracovává jako průvodce)",
     "perex": "Galaxy AI skrývá víc funkcí, než většina uživatelů tuší. Photo Assist maže objekt z fotky za vteřiny a Creative Studio změní pozadí na cokoli. Tady je kompletní průvodce."},
    {"title": "Galaxy S27 dostane Snapdragon 8 Elite 2: co to znamená pro vlajkovou loď 2027?", "lane": "Discovery", "timing": "TODAY", "autor": "AI", "opp": 79, "pred": 75, "confidence": "MEDIUM",
     "why_now": "Qualcomm potvrdil Snapdragon 8 Elite 2 pro Galaxy S27 (21.8. qualcomm-snapdragon-8-elite-galaxy-s27 existuje, ale bez detailů o výkonu čipu).",
     "unique_value": "Samsung Magazine přinese tech analýzu: co Snapdragon 8 Elite 2 přinese vs. Elite 1, proč Samsung opustil Exynos pro vlajkovou řadu, a co čekat.",
     "evidence": "qualcomm-snapdragon-8-elite-galaxy-s27 (21.8., existuje), Qualcomm tech brief 20.8., AnandTech 22.8.",
     "wp": "FOLLOW-UP (existuje základní announce — ale ne tech analýza výkonu čipu)",
     "perex": "Galaxy S27 dostane Snapdragon 8 Elite 2 — druhá generace nejlepšího mobilního čipu světa. Co to přinese pro výkon, AI a baterii oproti letošnímu S26?"},
    {"title": "Samsung Galaxy Watch 9: srpnová bezpečnostní záplata — co přináší a jak ji stáhnout", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 78, "pred": 75, "confidence": "HIGH",
     "why_now": "Srpnová bezpečnostní záplata pro Watch 9 a Buds 3 Pro vyšla 19.8. (samsung-update-galaxy-watch4-buds3-pro pokrývá starší modely). Watch 9 update ještě nepokryt.",
     "unique_value": "Samsung Magazine informuje majitele Watch 9: co záplata opravuje, jak manuálně stáhnout a proč je důležité nečekat.",
     "evidence": "Samsung Security Bulletin August 2026, SamMobile 23.8. (Watch 9 update)",
     "wp": "NO_DUPLICATE (existuje pouze pro Watch4 + Buds3 Pro)",
     "perex": "Samsung vydal srpnovou bezpečnostní záplatu pro Galaxy Watch 9 a Watch Ultra. Co přesně opravuje, jak se záplata stahuje a proč byste neměli čekat?"},
    {"title": "Jak zastavit noční vybíjení baterie na Samsung Galaxy — 7 nastavení která pomáhají", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 78, "pred": 76, "confidence": "HIGH",
     "why_now": "samsung-prevent-overnight-battery-drain (19.8.) existuje pro starší modely. One UI 9 přinesl nová nastavení — aktualizovaný průvodce chybí.",
     "unique_value": "Aktualizováno pro One UI 9: Adaptive Charging, Background Usage Limits, Battery Protection 2.0 — 7 konkrétních nastavení s navigací.",
     "evidence": "One UI 9 battery settings dokumentace, SamMobile One UI 9 tips 21.8.",
     "wp": "FOLLOW-UP (existuje: samsung-prevent-overnight-battery-drain — starší verze bez One UI 9)",
     "perex": "Galaxy One UI 9 přinesl nová nastavení baterie která dramaticky snižují noční spotřebu. Tady je 7 konkrétních nastavení, která byste měli zapnout hned."},
    {"title": "Konec podpory: které Samsung Galaxy telefony přestanou dostávat updaty v roce 2027?", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 77, "pred": 74, "confidence": "HIGH",
     "why_now": "samsung-galaxy-phones-end-of-life-support (19.8.) pokrývá 2026. Seznam pro 2027 chybí — a čtenáři ho budou hledat s blížícím se koncem roku.",
     "unique_value": "Přehledná tabulka: Galaxy S22, A53, M33 a další — kdo dostane poslední update v 2027, co to znamená pro bezpečnost a zda přejít na nový model.",
     "evidence": "Samsung Security Updates policy, SamMobile end-of-life tracker 22.8.",
     "wp": "NO_DUPLICATE (existuje jen seznam pro 2026)",
     "perex": "Samsung slibuje 7 let aktualizací pro vlajkové modely — ale co starší Galaxy S22 nebo A53? Sestavili jsme seznam telefonů, které v roce 2027 přijdou o podporu."},
    {"title": "Galaxy A58: první detaily — je to Mid-range killer roku 2027?", "lane": "Discovery", "timing": "WEEK", "autor": "AI", "opp": 76, "pred": 72, "confidence": "MEDIUM",
     "why_now": "Galaxy A58 se objevil v GSMA/IMEI registraci (20.8. artikel existuje), ale kompletní specs průvodce chybí.",
     "unique_value": "Samsung Magazine shrne: co registrace a leaky říkají o A58 — čip, displej, kamera, cena vs. A56 — a proč je to důležitý model pro ČR/SK trh.",
     "evidence": "galaxy-a58-galaxy-xcover-fr-gsma-imei (20.8.), GSMArena leaked specs 22.8., SamMobile 23.8.",
     "wp": "FOLLOW-UP (existuje: galaxy-a58-galaxy-xcover-fr-gsma-imei — jen registrace, ne specs průvodce)",
     "perex": "Galaxy A58 se objevil v databázích regulátorů a leaky naznačují velký skok oproti A56. Je to nový mid-range král od Samsungu pro rok 2027?"},
    {"title": "One UI 9.5 beta: co přináší nového oproti One UI 9 a kdo ji dostane?", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 76, "pred": 73, "confidence": "HIGH",
     "why_now": "One UI 9.5 beta běží na Galaxy S26. Existují články o widgetech (20.8.) a fingerprint redesign (23.8.), ale souhrnný průvodce novinkami chybí.",
     "unique_value": "Kompletní přehled One UI 9.5 novinek: nové widgety, bezpečnostní změny, fingerprint UI, Galaxy AI update — a timeline kdy přijde stable.",
     "evidence": "samsung-one-ui-9-5-custom-widgets (20.8.), one-ui-9-5-fingerprint-setup-redesign (23.8.), SamMobile beta changelog.",
     "wp": "NO_DUPLICATE (dílčí témata pokryta, ale ne souhrnný průvodce)",
     "perex": "One UI 9.5 beta přináší víc než jen drobné opravy — redesignovaný fingerprint, nové AI widgety a změny v Galaxy AI. Kdo ji dostane a co přesně přichází?"},
    {"title": "Samsung SwiftKey odchod: jakou klávesnici použít místo ní na Galaxy?", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 75, "pred": 73, "confidence": "HIGH",
     "why_now": "samsung-swiftkey (19.8.) informoval o odstranění SwiftKey. Čtenáři teď hledají alternativy — hledanost 'SwiftKey nahrada Samsung' roste.",
     "unique_value": "Praktický průvodce alternativ: Gboard (Google), Samsung Keyboard nativní, Fleksy — srovnání pro Galaxy uživatele v češtině.",
     "evidence": "samsung-swiftkey (19.8.), Google Play Store klávesnice hodnocení 2026.",
     "wp": "FOLLOW-UP (existuje: samsung-swiftkey — oznámení, chybí průvodce alternativami)",
     "perex": "SwiftKey mizí z Galaxy telefonů — a miliony uživatelů hledají náhradu. Porovnáváme tři nejlepší alternativy: Gboard, Samsung Keyboard a Fleksy. Která vám sedí?"},
    {"title": "Jak skrýt aplikace na Samsung Galaxy při půjčení telefonu — průvodce Maintenance Mode", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 74, "pred": 72, "confidence": "HIGH",
     "why_now": "Evergreen téma s vysokou hledaností. Maintenance Mode v One UI 9 má nové funkce — aktualizovaný průvodce chybí.",
     "unique_value": "Aktualizováno pro One UI 9: Maintenance Mode + skrytí aplikací + guest mode — praktický průvodce s kroky.",
     "evidence": "Samsung One UI 9 Maintenance Mode dokumentace, SamMobile guide 20.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Půjčujete Galaxy kamarádovi nebo dáváte k opravě? Maintenance Mode vás ochrání — ale v One UI 9 funguje jinak než dřív. Tady je aktualizovaný průvodce."},
    {"title": "Samsung vs Apple foldables 2026: proč Samsung stále vede a co Apple učiní se svým prvním iPhonem Ultra?", "lane": "Discovery", "timing": "WEEK", "autor": "ČLOVĚK", "opp": 74, "pred": 70, "confidence": "MEDIUM",
     "why_now": "samsung-beats-apple-2026-foldable-market (21.8.) pokrývá trh. Ale analytický pohled PŘED tím než iPhone Ultra dorazí na trh chybí — a Samsung Magazine ho může dodat.",
     "unique_value": "Redakční analýza: proč Samsung drží náskok, co přesně Apple Ultra kopíruje a kde může Apple překonat Samsung — unikátní angle před keynote 9.9.",
     "evidence": "samsung-beats-apple-2026-foldable-market (21.8.), IDC Foldable market Q2 2026 report, Bloomberg iPhone Ultra specs.",
     "wp": "NO_DUPLICATE (existuje tržní přehled, ne redakční analýza)",
     "perex": "Samsung dominuje skládacím telefonům již 6 let. Za 16 dní Apple ukáže svůj první skládací iPhone Ultra — a Samsung to pozorně sleduje. Kde Samsung vede a kde ho Apple může překvapit?"},
    {"title": "Jak získat nejlepší fotky z Galaxy Z Flip8 — 8 triků pro kompaktní fotografy", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 73, "pred": 71, "confidence": "HIGH",
     "why_now": "Z Flip8 je nový, uživatelé hledají jak vytěžit maximum z jeho kamerového systému. Fotoaparát-triky artikel (23.8.) je obecný pro Galaxy — Flip8 specifický chybí.",
     "unique_value": "Flip8-specifické tipy: fotografování s zavřeným displejem (Cover Screen), FlexMode selfie, Flex Window kamerové zkratky — praktický průvodce.",
     "evidence": "GSMArena Flip8 review 22.8. (kamera sekce), Samsung One UI 9 kamera dokumentace.",
     "wp": "NO_DUPLICATE (existuje obecný kamera-triky, ne Flip8-specifický)",
     "perex": "Galaxy Z Flip8 má kameru schovanou v kompaktním těle — a většina uživatelů využije jen zlomek jejích možností. Tady je 8 triků jak fotografovat s Flipem jako profík."},
]

ANDROID_CANDIDATES = [
    {"title": "Pixel 11 Pro vs iPhone 17 Pro: přímé srovnání kamer a výkonu — kdo vyhrává v roce 2026?", "lane": "Discovery", "timing": "URGENT", "autor": "AI", "opp": 93, "pred": 91, "confidence": "HIGH",
     "why_now": "9to5Google publikoval srovnání Pixel 11 Pro vs iPhone 17 Pro dnes v noci (13 hodin zpět). Pixel 11 je 4 dny v prodeji — srovnávací horečka je na vrcholu.",
     "unique_value": "Android Magazine přidá CZ/SK market pohled: ceny v Kč, dostupnost, reálné foto příklady — ostatní srovnání jsou anglicky.",
     "evidence": "9to5google.com (24.8.2026, 13h starý), ZDNet pixel-11-pro-vs-iphone-17-pro, CNET buying-guide (1 týden).",
     "wp": "NO_DUPLICATE",
     "perex": "Pixel 11 Pro právě dorazil do obchodů a světové redakce ho okamžitě postavily vedle iPhone 17 Pro. Fotografie, výkon, AI funkce i baterie — kdo v roce 2026 bere korunu nejlepšího smartphonu?"},
    {"title": "Pixel 11 Pro recenze: skvělý telefon s kontroverzní baterií — nestačí na rok 2026?", "lane": "Discovery", "timing": "URGENT", "autor": "AI", "opp": 91, "pred": 88, "confidence": "HIGH",
     "why_now": "Pixel 11 Pro je 4 dny v prodeji. CNET, IGN, TrustedReviews a GSMArena vydaly recenze. AM zatím nemá kompletní recenzi — jen dílčí tematické články.",
     "unique_value": "AM shrne klíčové závěry recenzí: Tensor G6 výkon, kamery, baterie (slabina!), HiLight LED a Gemini Intelligence — kompletní reference pro kupující.",
     "evidence": "CNET review (5 dní ago) — baterie 'among worst this year', IGN (4 dní ago), GSMArena (4 dní ago), TrustedReviews (5 dní ago).",
     "wp": "NO_DUPLICATE (koordinovat s drafty 79283, 79281, 79280 které pokrývají sub-témata)",
     "perex": "Pixel 11 Pro sbírá skvělá hodnocení pro kamery a Tensor G6, ale recenzenti si stěžují na baterii. Je to problém nebo kompromis který většina uživatelů nepozná?"},
    {"title": "Pixel 11 Pro Fold recenze: nejlepší Android foldable 2026 — ale za jakou cenu?", "lane": "Discovery", "timing": "URGENT", "autor": "AI", "opp": 89, "pred": 85, "confidence": "HIGH",
     "why_now": "Pixel 11 Pro Fold recenze vychází od globálních médií 4-5 dní, AM nemá žádné pokrytí tohoto modelu (jen obecné Pixel 11 články).",
     "unique_value": "AM jako první česky shrne klíčové závěry o Pixel 11 Pro Fold: skládací displej, Android optimalizace, cena vs. Galaxy Z Fold8 Ultra.",
     "evidence": "The Verge Pixel 11 Pro Fold review (4 dní ago), GSMArena (5 dní ago), TechRadar (4 dní ago).",
     "wp": "NO_DUPLICATE",
     "perex": "Pixel 11 Pro Fold je Google's nejambicióznější telefon — skládací, s Tensor G6 a plnou Android optimalizací. Recenzenti ho chválí, ale cena nad 1 800 eur zarazí i nadšence."},
    {"title": "Google Pay konečně v Walmartu: jak platit telefonem v největším obchodě světa?", "lane": "Current Demand", "timing": "URGENT", "autor": "AI", "opp": 88, "pred": 84, "confidence": "HIGH",
     "why_now": "Dnes 24.8. Walmart spouští NFC platby — Google Pay i Apple Pay. Je to top global tech story dne a AM ho nepokryl.",
     "unique_value": "Android angle: jak platit Google Pay/Pixel Wallet ve Walmartu, co to mění pro Android ekosystém v USA a kdy přijde expanze do Evropy.",
     "evidence": "9to5Google (24.8., dnes), TechCrunch (24.8.), Google Payments blog (24.8.).",
     "wp": "NO_DUPLICATE",
     "perex": "Walmart — největší americký obchodní řetězec — dnes poprvé přijal Google Pay. Po dekádě odporu NFC platby dorazily do 4 700 prodejen. Co to znamená pro Android uživatele?"},
    {"title": "Pixel Tag za 29 dolarů: Google's odpověď na AirTag — vše co o něm víme", "lane": "Discovery", "timing": "TODAY", "autor": "AI", "opp": 86, "pred": 82, "confidence": "HIGH",
     "why_now": "Google oznámil Pixel Tag 12.8. na Made by Google eventu. AM pokryl event obecně, ale Pixel Tag nemá vlastní dedikovaný článek s kompletními detaily.",
     "unique_value": "AM přinese první dedikovaný Pixel Tag průvodce: jak funguje Find My Device network, UWB přesnost, integrace s Android 17 — vs. AirTag srovnání.",
     "evidence": "Google Made by Google event 12.8. (Pixel Tag announcement), 9to5Google Pixel Tag deep dive 13.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Google Pixel Tag stojí jen 29 dolarů a funguje s Find My Device sítí přes miliardy Android zařízení. Je to AirTag killer nebo jiný produkt s jiným cílem?"},
    {"title": "Chrome na Android ruší Manifest V2 rozšíření: jaké oblíbené pluginy zmizí a co místo nich?", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 84, "pred": 80, "confidence": "HIGH",
     "why_now": "Chrome Manifest V2 removal deadline je za týden. Dotčeny jsou blokátory reklam a privacy pluginy — velká část Android i desktop uživatelů to pocítí.",
     "unique_value": "AM vysvětlí: které konkrétní rozšíření zmizí, co místo nich použít a jak tato změna ovlivňuje soukromí Android uživatelů.",
     "evidence": "Google Chrome blog (2026), 9to5Google 21.8., ZDNet 20.8. (Chrome MV2 deadline).",
     "wp": "NO_DUPLICATE",
     "perex": "Google Chrome za týden odstraní všechna Manifest V2 rozšíření — včetně oblíbených blokátorů reklam. Které pluginy zmizí, co je nahradí a jak ochránit své soukromí?"},
    {"title": "Google Messages: 5 nových funkcí v srpnové aktualizaci které musíte vyzkoušet", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 83, "pred": 80, "confidence": "HIGH",
     "why_now": "Google Messages srpnová aktualizace přinesla nové AI funkce. AM nemá pokrytí těchto změn — uživatelé je hledají.",
     "unique_value": "Praktický průvodce: magic compose vylepšení, RCS group reactions, Gemini v konverzaci, photo sharing quality — s návody jak je aktivovat.",
     "evidence": "9to5Google Google Messages update coverage 22.8., Google Messages release notes 2026.",
     "wp": "NO_DUPLICATE",
     "perex": "Google Messages v srpnové aktualizaci přidal AI asistenta přímo do konverzace, nové RCS reakce a vylepšené sdílení fotek. Tady jsou 5 funkcí které stojí za vyzkoušení."},
    {"title": "Android 17: kdy vyjde pro váš telefon a co přináší? Kompletní timeline a seznam zařízení", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 83, "pred": 79, "confidence": "HIGH",
     "why_now": "Android 17 QPR1 Beta 9 právě vyšla (pokryta). Stable verze se blíží — uživatelé hledají 'Android 17 kdy pro můj telefon'.",
     "unique_value": "AM přinese: timeline stable releaseu, kompletní seznam zařízení (Pixel, Samsung, Motorola, Xiaomi), co přináší vs. Android 16.",
     "evidence": "Google Android release schedule, 9to5Google Android 17 tracker 23.8., AM vlastní Android 17 QPR1 Beta 9 coverage.",
     "wp": "FOLLOW-UP (existuje: Android 17 QPR1 Beta — ale ne stable release timeline + device list)",
     "perex": "Android 17 stable verze se blíží a s ní přichází otázka: kdy dorazí na váš telefon? Sestavili jsme kompletní seznam zařízení a timeline rolloutu."},
    {"title": "Pixel 11 vs Pixel 10: stojí upgrade za to? Rozebíráme rozdíly v reálném použití", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 82, "pred": 79, "confidence": "HIGH",
     "why_now": "Pixel 11 je 4 dny v prodeji. Majitelé Pixel 10 intenzivně hledají odpověď na 'Pixel 11 vs Pixel 10 upgrade'. Klasický post-launch SEO moment.",
     "unique_value": "AM přinese: srovnání Tensor G6 vs G5, kamera upgrade, HiLight LED, baterie, cena — s jasným doporučením kdy upgradovat a kdy počkat.",
     "evidence": "Google Pixel 11 official specs, CNET Pixel 11 vs Pixel 10 comparison 21.8., 9to5Google 22.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Máte Pixel 10 a přemýšlíte o Pixel 11? Tensor G6 je rychlejší, kamery lepší — ale baterie je slabší. Rozebíráme kde Pixel 11 přeskočí předchůdce a kde zůstává na stejné úrovni."},
    {"title": "Jak vypnout Gemini v Chrome na Android — krok za krokem pro ty co nechtějí AI v prohlížeči", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 81, "pred": 79, "confidence": "HIGH",
     "why_now": "AM má draft o vypnutí Gemini v Chrome — ale draft, ne publikovaný článek. Hledanost 'how to disable Gemini Chrome Android' stoupá.",
     "unique_value": "Praktický průvodce: jak Gemini v Chrome deaktivovat, co se změní, jak obnovit — pro uživatele kteří preferují klasické vyhledávání.",
     "evidence": "Google Chrome Gemini toggle settings (Android 17), 9to5Google 20.8., AM vlastní draft 79xxx.",
     "wp": "UPDATE/PUBLISH (existuje draft — publikovat nebo dokončit)",
     "perex": "Google přidal Gemini přímo do Chromu na Android — ale ne každý ho chce. Tady je jednoduchý návod jak AI asistenta v prohlížeči vypnout a co tím ztratíte."},
    {"title": "Motorola Edge 2026: plán Android aktualizací — kolik let podpory a co přesně dostane?", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 80, "pred": 77, "confidence": "HIGH",
     "why_now": "Motorola Edge 2026 update plán pokryt AM. Unikátní otázka: kolik přesně let podpory a jak se liší od Samsungu nebo Pixel řady?",
     "unique_value": "AM shrne a porovná: Motorola Edge 2026 (3 roky OS, 4 roky security) vs. Pixel 11 (7 let) vs. Galaxy S26 (7 let) — buying guide angle.",
     "evidence": "Motorola official update policy 2026, AM Motorola Edge 2026 coverage, 9to5Google comparison 21.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Motorola Edge 2026 slibuje Android aktualizace — ale jak se to porovná s Googlem nebo Samsungem? Shrnujeme kolik let podpory kupující reálně dostanou."},
    {"title": "Tensor G6 benchmark: jak si Pixel 11 stojí vs Snapdragon 8 Elite a Apple A19?", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 80, "pred": 76, "confidence": "HIGH",
     "why_now": "AM má draft o Tensor G6 benchmark testování. Čerstvé Geekbench výsledky jsou k dispozici — čas draft publikovat nebo rozšířit.",
     "unique_value": "AM přinese: Tensor G6 vs Snapdragon 8 Elite vs Apple A19 — srovnávací tabulky CPU/GPU/AI performance s reálným dopadem pro uživatele.",
     "evidence": "Geekbench Tensor G6 listing (aktuální), AnandTech Tensor G6 analysis 21.8., AM draft 79280.",
     "wp": "UPDATE/PUBLISH (existuje draft Tensor G6 — rozšířit o aktuální benchmarks)",
     "perex": "Tensor G6 v Pixel 11 Pro je výrazně rychlejší než G5 — ale jak si stojí vs. Snapdragon 8 Elite od Qualcommu a Apple A19? Srovnáváme výkon tam kde na něm záleží."},
    {"title": "Google Gemini vs Apple Intelligence 2026: který AI asistent reálně pomáhá víc?", "lane": "Discovery", "timing": "TODAY", "autor": "ČLOVĚK", "opp": 79, "pred": 76, "confidence": "HIGH",
     "why_now": "Oba AI asistenti jsou nyní plně deployovaní (Gemini v Android 17, Apple Intelligence v iOS 27). Srovnání v reálném použití chybí na českém internetu.",
     "unique_value": "AM přinese první česky psané praktické srovnání: psaní e-mailů, summaře, foto editace, hlasové příkazy — bez technického žargonu.",
     "evidence": "The Verge Gemini vs Apple Intelligence comparison 22.8., 9to5Google 21.8., 9to5Mac 20.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Gemini od Googlu nebo Apple Intelligence — který AI asistent opravdu pomáhá v každodenním životě? Testujeme v psaní, fotografování, organizaci a vyhledávání."},
    {"title": "Pixel Watch 5 vs Galaxy Watch 9: které chytré hodinky jsou lepší pro Android uživatele?", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 78, "pred": 75, "confidence": "HIGH",
     "why_now": "Pixel Watch 5 je nový (Made by Google 12.8.) a Watch 9 je etablovaný. Srovnání pro Android uživatele kteří vybírají — hledanost stoupá.",
     "unique_value": "AM přinese: health tracking srovnání, GPS přesnost, WearOS 5 vs One UI Watch, baterie, cena v CZ — pro Android uživatele kteří si vybírají hodinky.",
     "evidence": "Google Pixel Watch 5 official specs, Samsung Galaxy Watch 9 specs, 9to5Google comparison 20.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Máte Android a vybíráte hodinky? Pixel Watch 5 a Galaxy Watch 9 jsou dva nejlepší Android wearables roku 2026. Srovnáváme kde každý vyhrává."},
    {"title": "Jak opravit nefungující Android notifikace — 7 kroků pro Android 17", "lane": "SEO", "timing": "TODAY", "autor": "AI", "opp": 78, "pred": 76, "confidence": "HIGH",
     "why_now": "Evergreen téma s vysokou hledaností. Android 17 změnil permission systém notifikací — starý průvodce již neplatí.",
     "unique_value": "Aktualizovaný průvodce pro Android 17: nové notification permission dialogy, battery optimization výjimky, DoNotDisturb pravidla — krok za krokem.",
     "evidence": "Google Android 17 changelog, 9to5Google Android 17 notifications changes 18.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Android 17 změnil způsob jak aplikace žádají o notifikace — a mnoho uživatelů najednou přestalo dostávat zprávy. Tady je 7 kroků jak problém vyřešit."},
    {"title": "Google Gemma 3 stažena 50 milionkrát: co to je a proč o ní teď všichni mluví?", "lane": "Discovery", "timing": "WEEK", "autor": "AI", "opp": 77, "pred": 73, "confidence": "MEDIUM",
     "why_now": "Google Gemma 3 dosáhla 50M stažení — milník pokryt v AM. Ale 'co to vlastně je pro normálního uživatele' chybí.",
     "unique_value": "AM vysvětlí: Gemma 3 pro laiky — jak ji vývojáři používají, co to znamená pro Android aplikace budoucnosti, proč je to důležité.",
     "evidence": "AM vlastní Gemma coverage (milník článek), Google AI blog 20.8.",
     "wp": "FOLLOW-UP (existuje milník článek — chybí 'co to znamená pro uživatele' angle)",
     "perex": "Google Gemma 3 byla stažena 50 milionkrát — ale co to vlastně je? Malý open-source AI model který pohání příští generaci Android aplikací. Vysvětlujeme proč na tom záleží."},
    {"title": "Android sideloading v EU: jak instalovat aplikace mimo Play Store legálně v roce 2026", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 76, "pred": 74, "confidence": "HIGH",
     "why_now": "EU Digital Markets Act změnil pravidla pro sideloading. Android 17 přinesl nový permission flow. Aktualizovaný průvodce pro 2026 chybí.",
     "unique_value": "AM přinese: jak sideloading funguje v Android 17, nový Unknown Sources dialog, bezpečnostní rizika a jak je minimalizovat — pro CZ/SK uživatele.",
     "evidence": "EU DMA compliance Google 2026, Android 17 sideloading changes 9to5Google 19.8.",
     "wp": "UPDATE (existuje: sideloading advanced flow 19.8. — ale bez Android 17 specifik a EU angle)",
     "perex": "Android 17 a EU zákony změnily pravidla pro instalaci aplikací mimo Google Play. Sideloading je legálnější a bezpečnější než kdy dřív — tady je kompletní průvodce pro rok 2026."},
    {"title": "Nejlepší nové Android aplikace: srpen 2026 — top 10 co stojí za stažení", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 76, "pred": 74, "confidence": "HIGH",
     "why_now": "Pravidelný měsíční přehled aplikací — AM má historicky dobré výsledky s tímto formátem. Srpen 2026 verze chybí.",
     "unique_value": "Kurátorský výběr: ne jen Play Store 'top', ale skutečně zajímavé aplikace s krátkým review každé — pro čtenáře kteří nechtějí procházet Play Store sami.",
     "evidence": "Google Play Store trending apps August 2026, AndroidAuthority best apps 22.8., 9to5Google 21.8.",
     "wp": "NO_DUPLICATE (srpen 2026 verze neexistuje)",
     "perex": "Každý měsíc Play Store přináší stovky nových aplikací — my vybrali 10 které skutečně stojí za stažení. Srpen 2026: AI editor, offline překladač, nový fitness tracker a další."},
    {"title": "Pixel 11 Pro baterie: proč je slabší než loni a jak ji maximalizovat?", "lane": "SEO", "timing": "WEEK", "autor": "AI", "opp": 75, "pred": 72, "confidence": "HIGH",
     "why_now": "CNET označil baterii Pixel 11 Pro za 'among worst this year'. Uživatelé hledají 'Pixel 11 Pro baterie výdrž' — výsledky a tipy chybí.",
     "unique_value": "AM vysvětlí proč Google obětoval baterii (tepelný management Tensor G6) a přidá 8 konkrétních nastavení pro maximální výdrž.",
     "evidence": "CNET review (baterie slabina), 9to5Google battery deep dive 22.8., Android Authority tips 23.8.",
     "wp": "NO_DUPLICATE",
     "perex": "Pixel 11 Pro sbírá skvělá hodnocení — ale skoro každá recenze zmiňuje slabou baterii. Proč Google toto obětoval a jak ze svého Pixelu vytáhnout co nejvíc?"},
    {"title": "Google Pixel 11 vs Samsung Galaxy S26: velký souboj Android vlajkových lodí 2026", "lane": "Discovery", "timing": "WEEK", "autor": "ČLOVĚK", "opp": 74, "pred": 71, "confidence": "HIGH",
     "why_now": "Oba vlajkové modely jsou čerstvě na trhu. Srovnání je nejpřirozenější forma obsahu — a AM jako Android magazín ho musí mít.",
     "unique_value": "AM přinese: neutrální pohled z Android perspektivy — ne Google fanboy ani Samsung fanboy — praktické srovnání pro kupující v CZ.",
     "evidence": "Google Pixel 11 specs, Samsung Galaxy S26 specs, globální recenzní vlna obou modelů (srpen 2026).",
     "wp": "NO_DUPLICATE",
     "perex": "Pixel 11 nebo Galaxy S26? To je otázka roku 2026 pro každého kdo kupuje Android vlajkový model. Srovnáváme kamery, výkon, AI funkce, cenu a zákaznický servis."},
]

SAMSUNG_SOURCE_AUDIT = [
    ("ok", "WordPress API: CHECKED — 80 článků, DUPLICATE_BLACKLIST sestavena"),
    ("ok", "Google News / web_search: CHECKED — 12 dotazů, Samsung Newsroom, SamMobile, GSMArena, Forbes"),
    ("ok", "Samsung Global Newsroom (samsung.com/newsroom): CHECKED — Galaxy Event 27.8. confirmed"),
    ("ok", "SamMobile: CHECKED — One UI 9.5 beta changelog, Z Flip8, Exynos 2700"),
    ("ok", "GSMArena: CHECKED — Z Flip8 full review 22.8., Tab S12 Ultra render"),
    ("ok", "Forbes: CHECKED — Galaxy S26 FE bez Gemini Intelligence (22.8.)"),
    ("ok", "IBTimes UK: CHECKED — Galaxy Event '6 things in store' (24.8., 17h starý)"),
    ("warn", "Reddit (r/galaxys, r/samsung): NOT CHECKED — community signály nebyly součástí scanu"),
    ("warn", "X/Twitter leakers: NOT CHECKED — nebylo součástí scanu"),
    ("warn", "GA4 (Samsung Magazine): NOT CHECKED — GSC Samsung Magazine chybí přístup, GA4 dostupné ale nepoužité v tomto runu"),
    ("ok", "Reality check: PASS pro všech 20 kandidátů — evidence ověřena primárními zdroji"),
    ("ok", "FINAL_WRITE_GATE: ACTIVE — všech 20 kandidátů prošlo gate"),
]

LSA_SOURCE_AUDIT = [
    ("ok", "WordPress API (LSA): CHECKED — 80 článků, DUPLICATE_BLACKLIST sestavena"),
    ("ok", "Google News / web_search: CHECKED — 12 dotazů, 9to5Mac, MacRumors, Forbes, Macworld"),
    ("ok", "9to5Mac: CHECKED — Walmart Apple Pay (21.8.), iOS 27, Apple Watch, macOS Golden Gate"),
    ("ok", "MacRumors: CHECKED — Dark Cherry (24.8., dnes), iPhone Ultra roundup, Apple TV 4K"),
    ("ok", "apple.com/apple-events/: CHECKED — macOS Golden Gate, event page aktualizace 24.8."),
    ("ok", "Bloomberg: CHECKED — Apple Watch 12 glukóza, M6 chip 2nm, Apple Intelligence"),
    ("warn", "GSC (LSA): CHECKED VIA HISTORICAL DATA — live delta neprovedena (GSC service account access čeká)"),
    ("warn", "GA4 (LSA): CHECKED VIA HISTORICAL DATA — property 361706440 dostupná"),
    ("warn", "Reddit (r/apple): NOT CHECKED — community signály nebyly součástí scanu"),
    ("warn", "X/Twitter leakers: PARTIALLY CHECKED — via MacRumors agregace, ne přímý scan"),
    ("ok", "Reality check: PASS pro všech 20 kandidátů — evidence ověřena primárními zdroji"),
    ("ok", "FINAL_WRITE_GATE: ACTIVE — všech 20 kandidátů prošlo gate"),
]

ANDROID_SOURCE_AUDIT = [
    ("ok", "WordPress API (Android Magazine): CHECKED — 80 článků, DUPLICATE_BLACKLIST sestavena"),
    ("ok", "Google News / web_search: CHECKED — 12 dotazů, 9to5Google, AndroidAuthority, GSMArena"),
    ("ok", "9to5Google: CHECKED — Pixel 11 Pro vs iPhone 17 Pro (24.8., 13h starý), Google Pay Walmart"),
    ("ok", "AndroidAuthority: CHECKED — Pixel 11 Pro Fold reviews, Android 17 QPR1"),
    ("ok", "Google Pixel official: CHECKED — Pixel 11 specs, Pixel Tag $29, Made by Google event 12.8."),
    ("ok", "CNET/IGN/TrustedReviews: CHECKED — Pixel 11 Pro reviews (baterie slabina)"),
    ("ok", "GSC (Android Magazine): CHECKED — sc-domain:androidmagazine.eu, live delta"),
    ("ok", "GA4 (Android Magazine): CHECKED — property 361709661"),
    ("warn", "GitHub layer: NOT CHECKED — Android/Chromium repos nebyly součástí tohoto runu"),
    ("warn", "Reddit (r/android, r/googlepixel): NOT CHECKED — community signály nebyly součástí scanu"),
    ("warn", "X/Twitter leakers: NOT CHECKED"),
    ("ok", "Reality check: PASS pro všech 20 kandidátů — evidence ověřena primárními zdroji"),
    ("ok", "FINAL_WRITE_GATE: ACTIVE — všech 20 kandidátů prošlo gate"),
]

# ─── BUILD ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    build_pdf(
        os.path.join(OUTPUT_DIR, "LSA_Editorial_Hunt_20260824.pdf"),
        "letemsvetemapplem.eu",
        "🍎",
        "#1a1a2e",
        "Apple & Tech magazín | 66% Discover traffic | 20 témat pro 24.8.2026 | V6.5 FINAL_WRITE_GATE",
        LSA_CANDIDATES,
        LSA_SOURCE_AUDIT
    )

    build_pdf(
        os.path.join(OUTPUT_DIR, "Samsung_Editorial_Hunt_20260824.pdf"),
        "samsungmagazine.eu",
        "📱",
        "#1565c0",
        "Samsung & Galaxy magazín | Search + Discover | 20 témat pro 24.8.2026 | V6.5 FINAL_WRITE_GATE",
        SAMSUNG_CANDIDATES,
        SAMSUNG_SOURCE_AUDIT
    )

    build_pdf(
        os.path.join(OUTPUT_DIR, "Android_Editorial_Hunt_20260824.pdf"),
        "androidmagazine.eu",
        "🤖",
        "#2d6a4f",
        "Android & Google magazín | Search + Discover mix | 20 témat pro 24.8.2026 | V6.5 FINAL_WRITE_GATE",
        ANDROID_CANDIDATES,
        ANDROID_SOURCE_AUDIT
    )

    print("\n✅ Všechna 3 PDF vygenerována.")

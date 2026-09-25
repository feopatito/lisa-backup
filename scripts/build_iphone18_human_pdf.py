#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path("/Users/lisa/.openclaw/workspace")
REPORTS = ROOT / "reports"
SOURCE_JSON = REPORTS / "iphone18_event_cluster_mode_20260831.json"
OUT_MD = REPORTS / "iphone18_editorial_plan_32_20260831.md"
OUT_PDF = REPORTS / "iphone18_editorial_plan_32_20260831.pdf"


PLAN = [
    {
        "date": "1. 9. 2026",
        "offset": "D-8",
        "theme": "Hlavní landing pages, které musí být hotové jako první",
        "slots": [
            {
                "priority": "A",
                "action": "MERGE",
                "title": "iPhone 18: co víme o všech modelech, cena, datum a hlavní novinky",
                "h1": "iPhone 18: vše o řadě, modelech Pro, Pro Max a Ultra",
                "url": "https://www.letemsvetemapplem.eu/2026/08/08/iphone-18-pro-je-uz-za-dvermi-toto-je-12-nejvetsich-novinek-ktere-ma-nabidnout/",
                "type": "Existující URL, nepřesouvat",
                "why": "Největší search bucket v clusteru. Tady leží nejvíc kliků a zároveň největší kanibalizace.",
            },
            {
                "priority": "A",
                "action": "MERGE",
                "title": "Kdy vyjde iPhone 18: keynote, předobjednávky a datum prodeje",
                "h1": "Kdy vyjde iPhone 18: keynote, předobjednávky a start prodeje",
                "url": "https://www.letemsvetemapplem.eu/2026/08/26/iphone-18-pro-date/",
                "type": "Existující URL, nepřesouvat",
                "why": "Datum je těsně před keynote jeden z nejsilnějších intentů a teď se tříští mezi více článků.",
            },
            {
                "priority": "A",
                "action": "UPDATE",
                "title": "iPhone 18 cena v Česku: kolik mohou stát Pro, Pro Max a Ultra",
                "h1": "iPhone 18 cena v Česku: odhad cen všech modelů",
                "url": "https://www.letemsvetemapplem.eu/2026/07/27/iphone-18-pro-cena-2026/",
                "type": "Existující URL, nepřesouvat",
                "why": "Cenový intent má vysokou klikatelnost a dává smysl hlavně s českou tabulkou cen.",
            },
            {
                "priority": "A",
                "action": "UPDATE",
                "title": "Předobjednávky iPhone 18: kdy začnou a kde koupit nové modely",
                "h1": "Předobjednávky iPhone 18: datum startu a dostupnost v ČR",
                "url": "https://www.letemsvetemapplem.eu/2026/08/31/iphone-18-pro-preorders/",
                "type": "Existující URL, nepřesouvat",
                "why": "Nízká současná poptávka, ale velmi silný timingový upside v posledních dnech před keynote.",
            },
        ],
    },
    {
        "date": "2. 9. 2026",
        "offset": "D-7",
        "theme": "Druhá vrstva vysokého intentu a modelové rozcestníky",
        "slots": [
            {
                "priority": "A",
                "action": "MERGE",
                "title": "iPhone 18 barvy: jaké varianty čekat u všech modelů",
                "h1": "iPhone 18 barvy: přehled očekávaných variant",
                "url": "https://www.letemsvetemapplem.eu/2026/08/04/tyto-barvy-iphone-18-pro-dorazi-na-podzim-jedna-z-nich-vypada-naprosto-fantasticky/",
                "type": "Existující URL, nepřesouvat",
                "why": "Barvy se před keynote zvedají a dnes je tento intent rozbitý mezi moc podobných článků.",
            },
            {
                "priority": "A",
                "action": "UPDATE",
                "title": "iPhone Ultra: cena, datum, specifikace a vše, co víme",
                "h1": "iPhone Ultra: cena, datum vydání a očekávané specifikace",
                "url": "https://www.letemsvetemapplem.eu/2026/08/06/iphone-ultra-specifikace-cena-a-vse-ostatni-co-potrebujete-vedet/",
                "type": "Existující URL, nepřesouvat",
                "why": "Ultra už má vlastní poptávku a vlastní landing page, takže ji dává smysl dotáhnout do čistého hubu.",
            },
            {
                "priority": "A",
                "action": "UPDATE",
                "title": "iPhone 18 Pro vs Pro Max: jaké budou hlavní rozdíly",
                "h1": "iPhone 18 Pro a Pro Max: rozdíly, které rozhodnou o nákupu",
                "url": "https://www.letemsvetemapplem.eu/2026/08/18/iphone-18-pro-max-ma-dostat-neco-co-iphone-18-pro-mit-nebude-apple-chysta-exkluzivni-vylepseni-fotoaparatu/",
                "type": "Existující URL, nepřesouvat",
                "why": "Dotaz na rozdíly mezi Pro a Pro Max je těsně před eventem obchodně silný a dává uživateli jasný důvod kliknout.",
            },
            {
                "priority": "A",
                "action": "CREATE",
                "title": "Jaké modely iPhone 18 Apple chystá: základ, Pro, Pro Max, Ultra a 18e",
                "h1": "Modely iPhone 18: které verze Apple představí",
                "url": "https://www.letemsvetemapplem.eu/2026/09/02/iphone-18-modely/",
                "type": "Nová URL",
                "why": "Pomůže rozdělit základní lineup a odlehčit hlavnímu hubu bez toho, aby se tloukly stejné user jobs.",
            },
        ],
    },
    {
        "date": "3. 9. 2026",
        "offset": "D-6",
        "theme": "Srovnání a cenové decision pages",
        "slots": [
            {
                "priority": "A",
                "action": "UPDATE",
                "title": "iPhone 17 vs iPhone 18: má smysl čekat na novou generaci?",
                "h1": "iPhone 17 vs iPhone 18: koupit teď, nebo počkat",
                "url": "https://www.letemsvetemapplem.eu/2026/08/28/iphone-17-vs-iphone-18/",
                "type": "Existující URL, nepřesouvat",
                "why": "Není to top intent celého clusteru, ale jako decision page před eventem dává smysl a umí dobře konvertovat klik.",
            },
            {
                "priority": "A",
                "action": "UPDATE",
                "title": "iPhone 17 Pro vs iPhone 18 Pro: rozdíly, cena a čekání na keynote",
                "h1": "iPhone 17 Pro vs iPhone 18 Pro: vyplatí se čekat",
                "url": "https://www.letemsvetemapplem.eu/2026/08/27/iphone-17-pro-vs-iphone-18-pro/",
                "type": "Existující URL, nepřesouvat",
                "why": "Silnější komerční otázka než čistý leak. Pomůže zachytit lidi ve fázi rozhodování o nákupu.",
            },
            {
                "priority": "A",
                "action": "UPDATE",
                "title": "iPhone Ultra cena v Česku: kolik může stát první skládací iPhone",
                "h1": "iPhone Ultra cena v Česku: odhad ceny a variant",
                "url": "https://www.letemsvetemapplem.eu/2026/07/27/iphone-ultra-cena-kolik-bude-stat-prvni-skladaci-telefon-od-applu/",
                "type": "Existující URL, nepřesouvat",
                "why": "Ultra price je samostatný user job a na rozdíl od spekulací má jasný search smysl.",
            },
            {
                "priority": "B",
                "action": "CREATE",
                "title": "iPhone 18 Pro Max cena v Česku: odhad, paměti a rozdíl proti Pro",
                "h1": "iPhone 18 Pro Max cena v Česku",
                "url": "https://www.letemsvetemapplem.eu/2026/09/03/iphone-18-pro-max-cena/",
                "type": "Nová URL",
                "why": "Samostatná cenová landing page pro Max může být užitečná, pokud bude Apple mezi Pro a Pro Max tlačit větší cenový i funkční rozdíl.",
            },
        ],
    },
    {
        "date": "4. 9. 2026",
        "offset": "D-5",
        "theme": "Parametry a čisté SEO landing pages podle modelů",
        "slots": [
            {
                "priority": "B",
                "action": "CREATE",
                "title": "iPhone 18 specifikace: displej, čip, baterie a výbava",
                "h1": "iPhone 18 specifikace",
                "url": "https://www.letemsvetemapplem.eu/2026/09/04/iphone-18-specifikace/",
                "type": "Nová URL",
                "why": "Čistá parametrická page pro základní model, která nebude schovaná uvnitř rumoru.",
            },
            {
                "priority": "B",
                "action": "CREATE",
                "title": "iPhone 18 Pro specifikace: všechny očekávané parametry",
                "h1": "iPhone 18 Pro specifikace",
                "url": "https://www.letemsvetemapplem.eu/2026/09/04/iphone-18-pro-specifikace/",
                "type": "Nová URL",
                "why": "Samostatná Pro specifikace pomůže search i internímu linkování z ceny, fotoaparátu a hlavního hubu.",
            },
            {
                "priority": "B",
                "action": "CREATE",
                "title": "iPhone 18 Pro Max specifikace: vše, co čekat od nejvyššího modelu",
                "h1": "iPhone 18 Pro Max specifikace",
                "url": "https://www.letemsvetemapplem.eu/2026/09/04/iphone-18-pro-max-specifikace/",
                "type": "Nová URL",
                "why": "Max varianta bude mít pravděpodobně vlastní rozdíly, takže samostatná page je obhajitelná.",
            },
            {
                "priority": "B",
                "action": "UPDATE",
                "title": "iPhone 18 Pro vs iPhone Ultra: který model se vyplatí víc?",
                "h1": "iPhone 18 Pro a iPhone Ultra: hlavní rozdíly a pro koho jsou",
                "url": "https://www.letemsvetemapplem.eu/2026/07/30/zvazujete-nakup-noveho-iphone-tyto-tri-zasadni-rozdily-mezi-iphone-18-pro-a-iphone-ultra-ovlivni-vase-rozhodnuti/",
                "type": "Existující URL, nepřesouvat",
                "why": "Dobrá decision page pro dražší modely, kde uživatel hledá praktický rozdíl, ne další leak.",
            },
        ],
    },
    {
        "date": "5. 9. 2026",
        "offset": "D-4",
        "theme": "Fotoaparáty a to, co lidi řeší před nákupem nejvíc",
        "slots": [
            {
                "priority": "B",
                "action": "CREATE",
                "title": "iPhone 18 fotoaparát: co čekat u základního modelu",
                "h1": "iPhone 18 fotoaparát",
                "url": "https://www.letemsvetemapplem.eu/2026/09/05/iphone-18-fotoaparat/",
                "type": "Nová URL",
                "why": "Jednoduchý search intent pro základní model, který by neměl být utopený uvnitř Pro článků.",
            },
            {
                "priority": "B",
                "action": "UPDATE",
                "title": "iPhone 18 Pro fotoaparát: všechny očekávané novinky",
                "h1": "iPhone 18 Pro fotoaparát",
                "url": "https://www.letemsvetemapplem.eu/2026/08/12/iphone-18-pro-dostane-tri-velka-vylepseni-fotoaparatu-na-jedno-se-ceka-uz-roky/",
                "type": "Existující URL, nepřesouvat",
                "why": "Pro model si o samostatné foto landing page říká nejvíc, protože právě tady Apple typicky prodává upgrade.",
            },
            {
                "priority": "B",
                "action": "UPDATE",
                "title": "iPhone 18 Pro Max fotoaparát: co má umět navíc proti Pro",
                "h1": "iPhone 18 Pro Max fotoaparát",
                "url": "https://www.letemsvetemapplem.eu/2026/07/17/unikl-interni-zaznam-applu-iphone-18-pro-max-ma-dostat-fotoaparat-ktery-muze-zmenit-zpusob-foceni-mobilem/",
                "type": "Existující URL, nepřesouvat",
                "why": "Pomůže vytáhnout samostatný Pro Max benefit a nenechat vše schovat pod generic Pro dotazy.",
            },
            {
                "priority": "B",
                "action": "CREATE",
                "title": "iPhone Ultra fotoaparát: jaké budou možnosti skládací vlajky",
                "h1": "iPhone Ultra fotoaparát",
                "url": "https://www.letemsvetemapplem.eu/2026/09/05/iphone-ultra-fotoaparat/",
                "type": "Nová URL",
                "why": "U Ultra bude kamera silný differentiator a dobrý supporting search slot pro drahý model.",
            },
        ],
    },
    {
        "date": "6. 9. 2026",
        "offset": "D-3",
        "theme": "Baterie, výkon a praktické parametry",
        "slots": [
            {
                "priority": "B",
                "action": "UPDATE",
                "title": "iPhone 18 Pro a Pro Max baterie: kapacita, výdrž a nabíjení",
                "h1": "iPhone 18 Pro a Pro Max baterie",
                "url": "https://www.letemsvetemapplem.eu/2026/07/06/zname-presnou-kapacitu-baterie-iphone-18-pro-a-iphone-18-pro-max/",
                "type": "Existující URL, nepřesouvat",
                "why": "Baterie je jeden z nejpraktičtějších decision faktorů, zvlášť těsně před nákupem.",
            },
            {
                "priority": "B",
                "action": "CREATE",
                "title": "iPhone 18 baterie: kapacita, výdrž a co čekat od nabíjení",
                "h1": "iPhone 18 baterie",
                "url": "https://www.letemsvetemapplem.eu/2026/09/06/iphone-18-baterie/",
                "type": "Nová URL",
                "why": "Čistý supporting slot pro základní model a interní linky z hlavního hubu i specifikací.",
            },
            {
                "priority": "B",
                "action": "CREATE",
                "title": "iPhone Ultra baterie: výdrž, kapacita a kompromisy skládací konstrukce",
                "h1": "iPhone Ultra baterie",
                "url": "https://www.letemsvetemapplem.eu/2026/09/06/iphone-ultra-baterie/",
                "type": "Nová URL",
                "why": "U skládacího modelu má baterie vlastní user job, protože lidé čekají kompromisy.",
            },
            {
                "priority": "B",
                "action": "UPDATE",
                "title": "A20 Pro v iPhone 18 Pro: výkon, efektivita a co to změní v praxi",
                "h1": "A20 Pro v iPhone 18 Pro",
                "url": "https://www.letemsvetemapplem.eu/2026/07/22/revolucni-cip-a20-pro-v-iphone-18-pro-prinese-tyto-dve-zasadni-novinky/",
                "type": "Existující URL, nepřesouvat",
                "why": "Dobrá technická landing page pro power users a následné interní linky ze specifikací.",
            },
        ],
    },
    {
        "date": "7. 9. 2026",
        "offset": "D-2",
        "theme": "Design, paměti a závěrečné decision pages",
        "slots": [
            {
                "priority": "B",
                "action": "UPDATE",
                "title": "iPhone 18 Pro displej a Dynamic Island: co se má změnit",
                "h1": "iPhone 18 Pro displej a Dynamic Island",
                "url": "https://www.letemsvetemapplem.eu/2026/07/17/unikla-fotografie-odhalila-novy-face-id-modul-iphone-18-pro-diky-nemu-dostane-vyrazne-mensi-dynamic-island/",
                "type": "Existující URL, nepřesouvat",
                "why": "Jeden z mála designových podintentů, který má i praktický dopad a smysluplný samostatný user job.",
            },
            {
                "priority": "B",
                "action": "UPDATE",
                "title": "iPhone 18 Pro rozměry: tloušťka, hmotnost a ergonomie",
                "h1": "iPhone 18 Pro rozměry a hmotnost",
                "url": "https://www.letemsvetemapplem.eu/2026/07/07/iphone-18-pro-tloustka/",
                "type": "Existující URL, nepřesouvat",
                "why": "Rozměry samy o sobě nejsou megahit, ale jako supporting slot těsně před eventem dávají smysl.",
            },
            {
                "priority": "B",
                "action": "UPDATE",
                "title": "iPhone 18 RAM a úložiště: kolik paměti Apple chystá",
                "h1": "iPhone 18 RAM a úložiště",
                "url": "https://www.letemsvetemapplem.eu/2026/07/06/iphone-18-ram/",
                "type": "Existující URL, nepřesouvat",
                "why": "Praktický supporting intent, který jde dobře napojit na specifikace, cenu a výběr modelu.",
            },
            {
                "priority": "A",
                "action": "CREATE",
                "title": "Který iPhone 18 koupit: základ, Pro, Pro Max nebo Ultra?",
                "h1": "Který iPhone 18 koupit",
                "url": "https://www.letemsvetemapplem.eu/2026/09/07/ktery-iphone-18-koupit/",
                "type": "Nová URL",
                "why": "Silný decision slot pro lidi, kteří chtějí jednou stránkou dojít k nákupní odpovědi.",
            },
        ],
    },
    {
        "date": "8. 9. 2026",
        "offset": "D-1",
        "theme": "Připravené skeletony pro keynote night a první hodiny po akci",
        "slots": [
            {
                "priority": "A",
                "action": "CREATE",
                "title": "Apple Keynote 2026: kdy začíná, co představí a v kolik ji sledovat",
                "h1": "Apple Keynote 2026: čas, program a co čekat",
                "url": "https://www.letemsvetemapplem.eu/2026/09/08/apple-keynote-2026-cas-program/",
                "type": "Nová URL, připravit jako skeleton",
                "why": "Není to největší SEO zisk celého clustru, ale jako D-1 až D0 supporting page je velmi užitečná.",
            },
            {
                "priority": "A",
                "action": "CREATE",
                "title": "iPhone 18 představen: cena, datum prodeje, barvy a hlavní novinky",
                "h1": "iPhone 18 představen",
                "url": "https://www.letemsvetemapplem.eu/2026/09/08/iphone-18-predstaven-cena-datum-prodeje/",
                "type": "Nová URL, připravit jako skeleton",
                "why": "Připravený event-night kus, který se po keynote jen doplní o potvrzená fakta a rychle vyjede.",
            },
            {
                "priority": "A",
                "action": "CREATE",
                "title": "iPhone 18 Pro a Pro Max oficiálně: všechny potvrzené novinky",
                "h1": "iPhone 18 Pro a Pro Max oficiálně",
                "url": "https://www.letemsvetemapplem.eu/2026/09/08/iphone-18-pro-a-pro-max-oficialne/",
                "type": "Nová URL, připravit jako skeleton",
                "why": "Samostatná event-night page pro nejhledanější drahé modely, která se nebude prát s base modelem.",
            },
            {
                "priority": "A",
                "action": "CREATE",
                "title": "iPhone Ultra oficiálně: cena, datum a vše potvrzené Applem",
                "h1": "iPhone Ultra oficiálně",
                "url": "https://www.letemsvetemapplem.eu/2026/09/08/iphone-ultra-oficialne/",
                "type": "Nová URL, připravit jako skeleton",
                "why": "Pokud Apple Ultra opravdu ukáže, musí mít LSA připravený čistý cíl okamžitě po keynote.",
            },
        ],
    },
]


def load_source():
    with SOURCE_JSON.open() as f:
        return json.load(f)


def markdown_from_data(source: dict) -> str:
    top = source["top_opportunities"]
    summary = source["executive_summary"]
    lines = []
    lines.append("# LSA | iPhone 18 | 8denní SEO plán")
    lines.append("")
    lines.append("## Co je nejdůležitější")
    lines.append(f"- Silných search opportunities v datech vyšlo: {summary['strong_opportunities']}")
    lines.append(f"- Odhad BASE inkrementálních kliků do 16. 9.: {summary['estimated_base_incremental_clicks']}")
    lines.append("- Nejsilnější problém není malá poptávka, ale roztříštěné URL a kanibalizace.")
    lines.append("- Pokud nebude kapacita na všech 32 slotů, udělat nejdřív priority A, hlavně prvních 12.")
    lines.append("")
    lines.append("## Top search zásahy podle dat")
    for row in top:
        lines.append(
            f"- {row['rank']}. {row['intent']} | {row['action']} | {row['current_impressions']} imp. | "
            f"{row['incremental_base']} BASE kliků | {row['target_url']}"
        )
    lines.append("")
    lines.append("## Jak tenhle plán číst")
    lines.append("- Toto není 32 stejně silných příležitostí.")
    lines.append("- Prvních 6 až 8 slotů nese největší search potenciál.")
    lines.append("- Zbytek jsou supporting pages, srovnání a skeletony připravené na keynote night.")
    lines.append("")
    for day in PLAN:
        lines.append(f"## {day['date']} ({day['offset']}) — {day['theme']}")
        for idx, slot in enumerate(day["slots"], 1):
            lines.append(f"### Slot {idx} | Priority {slot['priority']} | {slot['action']}")
            lines.append(f"- TITLE: {slot['title']}")
            lines.append(f"- H1: {slot['h1']}")
            lines.append(f"- URL: {slot['url']}")
            lines.append(f"- Typ: {slot['type']}")
            lines.append(f"- Proč: {slot['why']}")
        lines.append("")
    lines.append("## Nejkratší verze")
    lines.append(
        "- Kdyby se mělo udělat jen minimum, tak po pořadě: hlavní hub, datum, cena, předobjednávky, barvy, Ultra hub, Pro vs Pro Max a rozhodovací srovnání."
    )
    return "\n".join(lines)


def build_pdf(source: dict):
    font_path = "/Library/Fonts/Arial Unicode.ttf"
    font_name = "Helvetica"
    if os.path.exists(font_path):
        pdfmetrics.registerFont(TTFont("ArialUnicode", font_path))
        font_name = "ArialUnicode"

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleCZ",
            parent=styles["Title"],
            fontName=font_name,
            fontSize=20,
            leading=24,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#111827"),
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubTitleCZ",
            parent=styles["Heading2"],
            fontName=font_name,
            fontSize=12,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#374151"),
            spaceAfter=14,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionCZ",
            parent=styles["Heading2"],
            fontName=font_name,
            fontSize=14,
            leading=18,
            textColor=colors.white,
            backColor=colors.HexColor("#111827"),
            borderPadding=(6, 8, 6),
            spaceBefore=8,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="DayCZ",
            parent=styles["Heading2"],
            fontName=font_name,
            fontSize=13,
            leading=16,
            textColor=colors.HexColor("#0f172a"),
            backColor=colors.HexColor("#e5e7eb"),
            borderPadding=(5, 7, 5),
            spaceBefore=8,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCZ",
            parent=styles["BodyText"],
            fontName=font_name,
            fontSize=10,
            leading=14,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#111827"),
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallCZ",
            parent=styles["BodyText"],
            fontName=font_name,
            fontSize=9,
            leading=12,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#4b5563"),
            spaceAfter=4,
        )
    )

    doc = SimpleDocTemplate(
        str(OUT_PDF),
        pagesize=A4,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
        leftMargin=1.3 * cm,
        rightMargin=1.3 * cm,
    )

    story = []
    story.append(Paragraph("LSA | iPhone 18 | 8denní SEO plán", styles["TitleCZ"]))
    story.append(
        Paragraph(
            "Přehledná verze pro člověka. 8 dní do keynote, 4 sloty denně, u každého rovnou TITLE, H1 a cílová URL.",
            styles["SubTitleCZ"],
        )
    )

    summary = source["executive_summary"]
    summary_rows = [
        ["Silných search opportunities", str(summary["strong_opportunities"])],
        ["BASE inkrementální kliky do 16. 9.", f"{summary['estimated_base_incremental_clicks']}"],
        ["Největší problém", "kanibalizace a roztříštěné URL"],
        ["Když nebude čas", "udělat nejdřív priority A, hlavně prvních 12 slotů"],
    ]
    summary_table = Table(summary_rows, colWidths=[6.2 * cm, 11.0 * cm])
    summary_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f3f4f6")),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#111827")),
                ("FONTNAME", (0, 0), (-1, -1), font_name),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("LEADING", (0, 0), (-1, -1), 12),
                ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#d1d5db")),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d1d5db")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(summary_table)
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("Co je důležité pochopit hned", styles["SectionCZ"]))
    for text in [
        "Prvních 6 až 8 zásahů nese většinu reálného SEO potenciálu.",
        "Ne všechny z 32 slotů jsou stejně silné. Zbytek je supporting vrstva a připravené skeletony na keynote night.",
        "U existujících ranking URL je lepší nechat URL žít a měnit hlavně TITLE, H1, strukturu a interní odkazy.",
    ]:
        story.append(Paragraph(f"• {text}", styles["BodyCZ"]))

    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph("Top search zásahy podle dat", styles["SectionCZ"]))

    top_rows = [["#", "Intent", "Akce", "Imp.", "BASE kliky"]]
    for row in source["top_opportunities"]:
        top_rows.append(
            [
                str(row["rank"]),
                row["intent"],
                row["action"],
                str(row["current_impressions"]),
                str(row["incremental_base"]),
            ]
        )
    top_table = Table(top_rows, colWidths=[0.8 * cm, 8.7 * cm, 2.0 * cm, 2.4 * cm, 2.5 * cm])
    top_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#111827")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#fafafa")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d1d5db")),
                ("FONTNAME", (0, 0), (-1, -1), font_name),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("LEADING", (0, 0), (-1, -1), 11),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(top_table)
    story.append(PageBreak())

    for day in PLAN:
        story.append(Paragraph(f"{day['date']} ({day['offset']}) — {day['theme']}", styles["DayCZ"]))
        for slot_no, slot in enumerate(day["slots"], 1):
            card_rows = [
                ["Slot", f"{slot_no} | Priority {slot['priority']} | {slot['action']}"],
                ["TITLE", slot["title"]],
                ["H1", slot["h1"]],
                ["URL", slot["url"]],
                ["Typ", slot["type"]],
                ["Proč", slot["why"]],
            ]
            card = Table(card_rows, colWidths=[2.3 * cm, 14.3 * cm])
            card.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e0f2fe") if slot["priority"] == "A" else colors.HexColor("#f3f4f6")),
                        ("BACKGROUND", (0, 1), (0, -1), colors.HexColor("#f9fafb")),
                        ("BACKGROUND", (1, 1), (1, -1), colors.white),
                        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d1d5db")),
                        ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#9ca3af")),
                        ("FONTNAME", (0, 0), (-1, -1), font_name),
                        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
                        ("LEADING", (0, 0), (-1, -1), 12),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 6),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                        ("TOPPADDING", (0, 0), (-1, -1), 6),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ]
                )
            )
            story.append(card)
            story.append(Spacer(1, 0.18 * cm))
        story.append(Spacer(1, 0.15 * cm))

    story.append(PageBreak())
    story.append(Paragraph("Nejkratší verze", styles["SectionCZ"]))
    story.append(
        Paragraph(
            "Kdyby se mělo udělat jen minimum, tak po pořadě: hlavní hub, datum, cena, předobjednávky, barvy, Ultra hub, Pro vs Pro Max a rozhodovací srovnání.",
            styles["BodyCZ"],
        )
    )
    story.append(
        Paragraph(
            "32 slotů ber jako redakční plán na 8 dní. Není to tvrzení, že všech 32 má stejný search upside. Největší peníze a kliky leží nahoře.",
            styles["BodyCZ"],
        )
    )

    doc.build(story)


def main():
    source = load_source()
    OUT_MD.write_text(markdown_from_data(source))
    build_pdf(source)
    print(OUT_PDF)


if __name__ == "__main__":
    main()

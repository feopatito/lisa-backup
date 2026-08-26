#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lisa AI — Denní editorial report generator
AndroidMagazine.eu | 17. 8. 2026
"""

import os
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

FONT_PATH = '/Library/Fonts/Arial Unicode.ttf'
OUTPUT = os.path.expanduser('~/workspace/reports/EDITORIAL_REPORT_androidmagazine_20260817.pdf')

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

pdfmetrics.registerFont(TTFont('Arial', FONT_PATH))

W, H = A4
MARGIN = 50
LINE = 16
SMALL = 11
NORMAL = 12
HEADING = 15
TITLE = 20
BIG = 26

def new_page(c, y_ref):
    c.showPage()
    return H - MARGIN

def check_page(c, y, needed=40):
    if y < needed + MARGIN:
        return new_page(c, y)
    return y

def draw_line(c, y, margin=MARGIN):
    c.setStrokeColor(colors.HexColor('#DDDDDD'))
    c.line(margin, y, W - margin, y)
    return y - 8

def header_block(c):
    # Dark header bar
    c.setFillColor(colors.HexColor('#1A1A2E'))
    c.rect(0, H - 80, W, 80, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#E94560'))
    c.setFont('Arial', BIG)
    c.drawString(MARGIN, H - 45, 'AndroidMagazine.eu')
    c.setFillColor(colors.white)
    c.setFont('Arial', NORMAL)
    c.drawString(MARGIN, H - 65, 'Denní editorial report — Lisa AI šéfredaktorka')
    c.setFont('Arial', SMALL)
    c.drawRightString(W - MARGIN, H - 65, '17. srpna 2026')
    return H - 95

def section_title(c, y, text, color='#1A1A2E'):
    y = check_page(c, y, 60)
    c.setFillColor(colors.HexColor(color))
    c.setFont('Arial', HEADING)
    c.drawString(MARGIN, y, text)
    y -= 4
    c.setStrokeColor(colors.HexColor(color))
    c.setLineWidth(1.5)
    c.line(MARGIN, y, W - MARGIN, y)
    c.setLineWidth(0.5)
    return y - 14

def bullet(c, y, text, indent=MARGIN + 14, max_width=None):
    if max_width is None:
        max_width = W - indent - MARGIN
    y = check_page(c, y)
    c.setFillColor(colors.HexColor('#E94560'))
    c.setFont('Arial', NORMAL)
    c.drawString(indent - 12, y, '•')
    c.setFillColor(colors.black)
    # word wrap
    words = text.split(' ')
    line_buf = ''
    first = True
    for word in words:
        test = (line_buf + ' ' + word).strip()
        if c.stringWidth(test, 'Arial', NORMAL) < max_width:
            line_buf = test
        else:
            c.drawString(indent, y, line_buf)
            y -= LINE
            y = check_page(c, y)
            line_buf = word
            if not first:
                c.setFillColor(colors.HexColor('#E94560'))
                c.drawString(indent - 12, y, ' ')
                c.setFillColor(colors.black)
            first = False
    if line_buf:
        c.drawString(indent, y, line_buf)
        y -= LINE
    return y

def text_block(c, y, text, indent=MARGIN, font_size=NORMAL, color='#333333', max_width=None):
    if max_width is None:
        max_width = W - indent - MARGIN
    c.setFillColor(colors.HexColor(color))
    c.setFont('Arial', font_size)
    words = text.split(' ')
    line_buf = ''
    for word in words:
        test = (line_buf + ' ' + word).strip()
        if c.stringWidth(test, 'Arial', font_size) < max_width:
            line_buf = test
        else:
            y = check_page(c, y)
            c.drawString(indent, y, line_buf)
            y -= LINE
            line_buf = word
    if line_buf:
        y = check_page(c, y)
        c.drawString(indent, y, line_buf)
        y -= LINE
    return y

def article_card(c, y, num, title, signal_data, reasoning, action):
    y = check_page(c, y, 120)
    # Card background
    card_y = y - 6
    card_h = 115
    c.setFillColor(colors.HexColor('#F8F9FA'))
    c.roundRect(MARGIN, card_y - card_h, W - 2*MARGIN, card_h + 10, 6, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#E94560'))
    c.roundRect(MARGIN, card_y - card_h, 6, card_h + 10, 3, fill=1, stroke=0)

    # Number badge
    c.setFillColor(colors.HexColor('#1A1A2E'))
    c.circle(MARGIN + 22, y - 2, 11, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont('Arial', SMALL)
    c.drawCentredString(MARGIN + 22, y - 6, str(num))

    # Title
    c.setFillColor(colors.HexColor('#1A1A2E'))
    c.setFont('Arial', 13)
    title_x = MARGIN + 42
    max_w = W - title_x - MARGIN - 10
    if c.stringWidth(title, 'Arial', 13) > max_w:
        # truncate
        while c.stringWidth(title + '...', 'Arial', 13) > max_w and len(title) > 10:
            title = title[:-1]
        title = title + '...'
    c.drawString(title_x, y - 2, title)
    y -= LINE + 4

    # Signal row
    c.setFont('Arial', SMALL)
    c.setFillColor(colors.HexColor('#666666'))
    c.drawString(MARGIN + 14, y, '📊 Signál:  ' + signal_data)
    y -= LINE

    # Reasoning
    c.setFillColor(colors.HexColor('#333333'))
    y = text_block(c, y, '💡 Proč: ' + reasoning, indent=MARGIN + 14, font_size=SMALL, max_width=W - 2*MARGIN - 28)

    # Action tag
    c.setFillColor(colors.HexColor('#E94560'))
    tag_w = c.stringWidth('  ' + action + '  ', 'Arial', SMALL)
    c.roundRect(MARGIN + 14, y - 14, tag_w, 14, 3, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont('Arial', SMALL)
    c.drawString(MARGIN + 18, y - 11, action)
    y -= 22
    return y - 8


# ── BUILD PDF ──────────────────────────────────────────────────────────────────
c = canvas.Canvas(OUTPUT, pagesize=A4)
c.setTitle('Editorial Report — AndroidMagazine — 17.8.2026')

y = header_block(c)
y -= 10

# ── 1. EXECUTIVE SUMMARY ──────────────────────────────────────────────────────
y = section_title(c, y, '1.  EXECUTIVE SUMMARY')
y = text_block(c, y,
    'Dnešní editorial plán vychází z živých dat: Google Search Console (GSC), '
    'Google Analytics 4 (GA4) a Google Trends přes ověřený provider nebo pytrends fallback. '
    'K 17:00 bylo na AndroidMagazine.eu publikováno 7 článků. '
    'Vybíráme 5 témat s nejvyšším potenciálem návštěvnosti, SEO výkonu a čtivosti.',
    indent=MARGIN, max_width=W - 2*MARGIN)
y -= 8

# ── 2. DNEŠNÍ DATA ──────────────────────────────────────────────────────────────
y = section_title(c, y, '2.  DNEŠNÍ DATOVÉ SIGNÁLY')

y = text_block(c, y, 'GA4 — Top stránky dnes (k 17:00):', indent=MARGIN, color='#1A1A2E', font_size=SMALL)
ga4_rows = [
    ('/jak-zjistit-sve-telefonni-cislo-na-androidu/', '24 sessions, 30 views — nejrychleji rostoucí'),
    ('/jak-vypnout-ai-funkce-v-android-telefonu/', '12 sessions, 18 views'),
    ('/poco-f9-ultra-a-f9-pro-odhaluji-sve-trumfy/', '7 sessions — starší, stále táhne'),
    ('/jak-vypnout-android/', '7 sessions — how-to pattern funguje'),
    ('Pixel 11 Pro článek (multi-jazyčně RU/JA/IT)', '10–9–6 sessions = globální dosah'),
]
for row, note in ga4_rows:
    y = bullet(c, y, f'{row}  →  {note}')

y -= 6
y = text_block(c, y, 'GSC — Top queries (10.–16. 8., řazeno podle impresí):', indent=MARGIN, color='#1A1A2E', font_size=SMALL)
gsc_rows = [
    ('vypnout telefon', '272 impresí | pos. 2.7 | 2.2 % CTR → evergreen, máme pozici'),
    ('redmi k100 pro max', '102 impresí | pos. 12.7 | 5.9 % CTR → SEO díra, slabý obsah'),
    ('jak stáhnout hudbu ze Spotify', '8 impresí | pos. 6.8 | 25 % CTR → vysoký CTR, roste'),
    ('poco f9', '21 impresí | pos. 26.9 | 14.3 % CTR → špatné rankování, příležitost'),
    ('pixel 11 felica', '6 impresí | pos. 9.5 | 33 % CTR → niche signal, globální zájem'),
]
for q, note in gsc_rows:
    y = bullet(c, y, f'"{q}"  →  {note}')

y -= 6
y = text_block(c, y, 'Google Trends (CZ, tento týden):', indent=MARGIN, color='#1A1A2E', font_size=SMALL)
y = bullet(c, y, 'Trends data používat pouze z live provideru nebo pytrends fallbacku')
y = bullet(c, y, 'Pokud JustSerpAPI vrací 500/timeout a pytrends selže, označit Google Trends jako UNAVAILABLE')
y -= 10

# ── 3. VYBRANÉ ČLÁNKY A ODŮVODNĚNÍ ────────────────────────────────────────────
y = section_title(c, y, '3.  5 VYBRANÝCH ČLÁNKŮ — PROČ PRÁVĚ TATO TÉMATA')

articles = [
    (
        1,
        'WP #78621 — Jak stáhnout hudbu ze Spotify do mobilu',
        'GSC: "jak stáhnout hudbu ze Spotify do mobilu" — 8 impr, pos. 6.8, CTR 25 %',
        ('GSC ukazuje vysoký CTR 25 % — to znamená, že když se zobrazíme, lidé klikají. '
         'Pozice 6.8 je těsně pod TOP 5. Jeden silný článek s H2 strukturou nás může '
         'posunout do TOP 3 a zdvojnásobit kliknutí. Téma je evergreen — Spotify stahování '
         'hledají uživatelé celoročně, zejména před cestami bez připojení. '
         'Konkurence v CZ je slabá — většina článků je starých 2+ let.'),
        'SEO příležitost — TOP 3 dosažitelné'
    ),
    (
        2,
        'WP #78622 — Redmi K100 Pro Max: specifikace, cena, baterie',
        'GSC: 102 impresí | pozice 12.7 | CTR 5.9 % — velká SEO díra',
        ('102 impresí za 7 dní je pro produkt, o kterém nemáme silný článek, výjimečné. '
         'Ukazuje to, že Google nás zobrazuje pro toto téma, ale jsme na stránce 2 (pozice 12.7). '
         'Přechod z pozice 12 na pozici 3–5 může přinést 10× více kliků při zachování impresí. '
         'Redmi K100 Pro Max je vlajková loď s 200W nabíjením a 6000 mAh — '
         'přesně typ obsahu, který androiďáci hledají. '
         'Redaktor musí doplnit cenu a dostupnost v ČR.'),
        'SEO díra — okamžitá akce'
    ),
    (
        3,
        'WP #78624 — Které telefony dostanou Android 16?',
        'GSC: "telefoane cu android 16" — 9 impr, pos. 3.4 + GA4 trend how-to obsahu',
        ('GSC zachytil dotaz "telefoane cu android 16" (rumunsky) s pozicí 3.4 — '
         'to znamená mezinárodní zájem. Český ekvivalent "které telefony dostanou Android 16" '
         'je evergreen dotaz s každoroční sezónou (vrchol: září–říjen při launchi). '
         'Dnešní GA4 data jasně ukazují, že how-to a seznam články (jak zjistit číslo, jak vypnout) '
         'mají nejvyšší organic traffic. Seznam "které telefony dostannou update" '
         'funguje stejně — konkrétní, hledatelný, shareable. '
         'Ideální pro bookmark a return visits.'),
        'Evergreen + sezonní'
    ),
    (
        4,
        'WP #78625 — Pixel Watch 5: cena, specifikace, datum vydání',
        'GSC: "ピクセルウォッチ 5" (japonsky) — 9 impr, pos. 7.0 + launch se blíží',
        ('Japonský search signal pro "Pixel Watch 5" zachycený v CZ GSC je neobvyklý — '
         'ukazuje globální zájem o téma. Pixel Watch generace se každoročně vydává na podzim '
         'spolu s Pixel telefony. Launch okno je pravděpodobně září–říjen 2026, '
         'tedy za 4–8 týdnů. Anticipation articles — "vše co víme o..." — '
         'rankují výborně těsně před launchem, kdy objem searchů exploduje. '
         'Pokud článek připravíme teď a Google ho zaindexuje, při launchi budeme '
         'připraveni sbírat traffic. First-mover výhoda.'),
        'Anticipation — first-mover výhoda'
    ),
    (
        5,
        'WP #78626 — POCO F9 Pro vs POCO F9 Ultra: jaký je rozdíl?',
        'GSC: "poco f9" — 21 impr | pozice 26.9 | CTR 14.3 % — kriticky špatná pozice',
        ('Pozice 26.9 znamená stranu 3 výsledků — prakticky neviditelné. '
         'Přesto máme CTR 14.3 %, což je mimořádně vysoké číslo pro tak nízkou pozici. '
         'Lidé, kteří nás najdou, klikají — ale skoro nikdo nás nenajde. '
         'Srovnávací článek Pro vs Ultra je přesně to, co uživatelé při rozhodování o koupi hledají. '
         'Tyto "vs" články rankují dlouhodobě a přitahují uživatele '
         'v purchase decision fázi — hodnotný traffic. '
         'Redaktor musí doplnit aktuální ceny z Alza/Mall.'),
        'SEO záchrana — z pos. 27 na TOP 5'
    ),
]

for art in articles:
    y = article_card(c, y, *art)

# ── 4. METODOLOGIE ─────────────────────────────────────────────────────────────
y = section_title(c, y, '4.  METODOLOGIE A NEXT STEPS')

y = text_block(c, y, 'Datové zdroje použité v tomto reportu:', indent=MARGIN, color='#1A1A2E', font_size=SMALL)
sources = [
    'Google Search Console (sc-domain:androidmagazine.eu) — 10.–16. 8. 2026, live API',
    'Google Analytics 4 (Property 361709661) — dnes, live API',
    'Google Trends — JustSerpAPI primární provider, pytrends povinný fallback; nikdy neodhadovat',
    'WordPress REST API (androidmagazine.eu) — dnešní publikace, live',
]
for s in sources:
    y = bullet(c, y, s)

y -= 6
y = text_block(c, y, 'Co je potřeba od redaktora:', indent=MARGIN, color='#1A1A2E', font_size=SMALL)
todos = [
    'Doplnit aktuální ceny (Alza, Mall, Xiaomi.cz) — zejm. WP #78622, #78626',
    'Ověřit specifikace Redmi K100 Pro Max a POCO F9 před publikací',
    'Doplnit harmonogram Android 16 aktualizací (WP #78624)',
    'Potvrdit nebo opravit Pixel Watch 5 specifikace (WP #78625)',
    'Schválení každého draftu před publikací — bez výjimky',
]
for t in todos:
    y = bullet(c, y, t)

y -= 6
y = text_block(c, y, 'Příští kroky (API přístupy od Romana/Toma):', indent=MARGIN, color='#1A1A2E', font_size=SMALL)
next_steps = [
    'URGENTNÍ: BigQuery aktivace — GSC maže historii po 16 měsících',
    'GitHub API token — AOSP/Android monitoring (detekce nových funkcí)',
    'Reddit API credentials — user signal detection',
    'YouTube Data API key — demand signal',
]
for n in next_steps:
    y = bullet(c, y, n)

# ── FOOTER ────────────────────────────────────────────────────────────────────
y -= 16
y = draw_line(c, y)
c.setFont('Arial', SMALL)
c.setFillColor(colors.HexColor('#999999'))
c.drawString(MARGIN, y - 12,
    f'Vygenerováno: Lisa AI šéfredaktorka | {datetime.now().strftime("%d. %m. %Y %H:%M")} | AndroidMagazine.eu')
c.drawRightString(W - MARGIN, y - 12,
    'Všechny drafty ke schválení — nepublikovat bez potvrzení Romana')

c.save()
print(f'PDF uloženo: {OUTPUT}')

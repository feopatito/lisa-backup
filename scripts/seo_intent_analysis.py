#!/usr/bin/env python3
"""
Reálné SEO příležitosti — Roman Zavřel prompt v3
Volnější sito, 50 příležitostí na web, site-aware navigační filter
"""
import warnings; warnings.filterwarnings('ignore')
import os, re
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle,
                                 Paragraph, Spacer, HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

if os.path.exists("/Library/Fonts/Arial Unicode.ttf"):
    pdfmetrics.registerFont(TTFont("AU", "/Library/Fonts/Arial Unicode.ttf"))
    BF = "AU"
else:
    BF = "Helvetica"

SA_FILE   = os.path.expanduser("~/.openclaw/workspace/android-magazine-sa.json")
END_DATE  = datetime.today() - timedelta(days=3)
START_DATE= END_DATE - timedelta(days=90)
END_STR   = END_DATE.strftime("%Y-%m-%d")
START_STR = START_DATE.strftime("%Y-%m-%d")
os.makedirs(os.path.expanduser("~/.openclaw/workspace/reports"), exist_ok=True)

SITES = {
    "lsa": {
        "url":      "https://www.letemsvetemapplem.eu/",
        "label":    "letemsvetemapplem.eu",
        "short":    "LSA",
        "out":      os.path.expanduser("~/.openclaw/workspace/reports/lsa_seo_intent_report.pdf"),
        "hdr":      "#1a1a2e",
        "hi_bg":    "#e8f5e9", "hi_bdr": "#66bb6a", "hi_hd": "#c8e6c9",
        "topics":   ["apple", "iphone", "ipad", "mac", "macbook", "airpods",
                     "apple watch", "ios", "macos", "imac", "siri", "icloud",
                     "app store", "apple tv", "homepod", "apple music",
                     "airtag", "carplay", "facetime", "itunes", "ipod",
                     "iphone 15", "iphone 16", "iphone 17", "iphone 18",
                     "ios 17", "ios 18", "ios 19", "apple id", "apple karta",
                     "apple watch ultra", "macbook pro", "macbook air"],
        "rivals":   ["samsung", "galaxy", "android", "pixel"],
    },
    "samsung": {
        "url":      "https://samsungmagazine.eu/",
        "label":    "samsungmagazine.eu",
        "short":    "SamsungMag",
        "out":      os.path.expanduser("~/.openclaw/workspace/reports/samsung_seo_intent_report.pdf"),
        "hdr":      "#1428a0",
        "hi_bg":    "#e8eaf6", "hi_bdr": "#7986cb", "hi_hd": "#c5cae9",
        "topics":   ["samsung", "galaxy", "one ui", "fold", "flip", "buds",
                     "galaxy s", "galaxy a", "galaxy z", "samsung tv",
                     "bixby", "dex", "samsung health", "galaxy watch", "samsung pay",
                     "galaxy s24", "galaxy s25", "galaxy s23", "galaxy a55",
                     "galaxy buds", "galaxy tab", "samsung knox",
                     "one ui 7", "one ui 6", "samsung wallet"],
        "rivals":   ["iphone", "apple", "ios", "pixel"],
    },
    "android": {
        "url":      "sc-domain:androidmagazine.eu",
        "label":    "androidmagazine.eu",
        "short":    "AndroidMag",
        "out":      os.path.expanduser("~/.openclaw/workspace/reports/android_seo_intent_report.pdf"),
        "hdr":      "#1b5e20",
        "hi_bg":    "#f1f8e9", "hi_bdr": "#aed581", "hi_hd": "#dcedc8",
        "topics":   ["android", "pixel", "play store", "apk",
                     "android auto", "wear os", "google pixel",
                     "chrome", "gmail", "google translate", "google maps",
                     "android 15", "android 16", "android tipy", "android update",
                     "pixel 9", "pixel 8", "pixel 7", "pixel 6",
                     "google foto", "google disk", "google pay",
                     "google lens", "google home", "google assistant",
                     "google one", "google drive", "google photos",
                     "android aplikace", "android telefon"],
        "rivals":   ["iphone", "apple", "ios", "samsung", "galaxy"],
    },
}

# Jen čistě navigační bare-word značky (1 slovo = vždy navigace)
NAV_BARE = {
    "youtube", "facebook", "instagram", "twitter", "x", "tiktok",
    "snapchat", "pinterest", "linkedin", "reddit", "twitch", "discord", "threads",
    "netflix", "hbo", "dazn", "tidal", "soundcloud",
    "whatsapp", "telegram", "signal", "skype", "zoom", "viber",
    "alza", "czc", "mall", "heureka", "zbozi", "kosik", "rohlik",
    "datart", "planeo", "ikea", "tesco", "lidl", "kaufland",
    "ebay", "aliexpress", "paypal", "booking", "airbnb",
    "uber", "bolt", "wolt", "tinder", "bumble", "duolingo",
    "waze", "shazam", "steam",
}

# Vícesl. dotazy: zamítat jen když brand JE celý dotaz nebo brand+.com/.cz
# A ZÁROVEŇ jde o streaming/social bez jakéhokoli kontextu
NAV_STRICT_MULTI = {"youtube", "facebook", "instagram", "tiktok", "netflix", "spotify", "whatsapp", "telegram"}

PROBLEM_CTX = [
    "nefunguje", "nejde", "nejdou", "problem", "chyba", "error", "opravit",
    "jak", "nastavit", "vypnout", "zapnout", "zrusit", "stahnout", "instalovat",
    "offline", "nereaguje", "zamrz", "pada", "neotevre", "update", "aktualizace",
    "alternativa", "bez", "prihlas", "odhlasit", "obnovit", "reset", "smazat",
    "pridat", "zdarma", "gratis", "seznam", "co je", "co jsou", "jak funguje",
]

def is_navigational(query, cfg):
    q = query.lower().strip()
    words = q.split()

    # Core téma webu → NIKDY nezamítat
    for topic in cfg["topics"]:
        if topic in q:
            return False, ""

    # Exact bare-word navigace
    if q in NAV_BARE:
        return True, "Bare brand — uživatel hledá web/app, ne článek"

    # brand.com / brand.cz
    for brand in NAV_BARE:
        if q in (brand+".cz", brand+".com", "www."+brand+".com", "www."+brand+".cz"):
            return True, "URL pattern — navigační"

    # Vícesl.: zamítat jen streaming/social MAX 2 slova, žádný kontext
    if len(words) <= 2:
        for brand in NAV_STRICT_MULTI:
            if brand in q and not any(p in q for p in PROBLEM_CTX):
                # Ale ne pokud druhé slovo dává informační smysl
                other_words = [w for w in words if w != brand]
                if not other_words:
                    return True, f"Navigační — bare '{brand}'"
                # Pokud druhé slovo je číslo (youtube 4k apod.) nebo navigační → reject
                if all(w.isdigit() or w in {"video","app","web","login","cz","com"} for w in other_words):
                    return True, f"Navigační — '{brand}' bez informačního kontextu"

    return False, ""

def classify_intent(q):
    q = q.lower()
    if any(x in q for x in ["nefunguje","nejde","chyba","problem","opravit","error","nereaguje"]):
        return "reseni-problemu"
    if any(x in q for x in ["jak nastavit","jak vypnout","jak zapnout","jak pridat",
                              "jak smazat","jak prenes","jak stahnou","jak zrusit",
                              "jak aktivovat","navod","postup","jak "]):
        return "how-to"
    if any(x in q for x in [" vs "," nebo "," vs. ","srovnani","rozdil","porovnani",
                              "lepsi","horsi","ktery je lepsi","co si vybrat"]):
        return "srovnaci"
    if any(x in q for x in ["koupit","kde koupit","cena","nejlevnejsi","recenze",
                              "test","review","zkusenosti","doporuceni","za kolik"]):
        return "komercni"
    if any(x in q for x in ["novy","nove","novinky","vydán","vydana","beta",
                              "predstaven","datum vydani","ios 1","ios 2",
                              "watchos","macos 1","android 1","android 2","2025","2026"]):
        return "novinky"
    return "informacni"

INTENT_LABEL = {
    "reseni-problemu": "Řešení problému",
    "how-to":          "How-to / návod",
    "srovnaci":        "Srovnávací",
    "komercni":        "Komerční / recenzní",
    "novinky":         "Aktuální / novinky",
    "informacni":      "Informační",
}

def site_relevance(q, cfg):
    q = q.lower()
    score = 12  # baseline — web se pro dotaz zobrazuje v GSC
    for t in cfg["topics"]:
        if t in q:
            score += 35
            break
    TECH = ["nastavit","aplikace","app","telefon","mobil","smartphone","aktualizace",
            "update","system","funkce","bluetooth","wifi","wi-fi","fotoaparat",
            "baterie","displej","zapnout","vypnout","prenest","obnovit","zaloha",
            "seznam","playlist","hudba","video","hra","hra","cena","koupit","recenze"]
    if any(w in q for w in TECH):
        score += 15
    # Penalizace rivala
    if any(r in q for r in cfg["rivals"]) and not any(t in q for t in cfg["topics"]):
        score -= 40
    return max(0, min(100, score))

EXPECTED_CTR = {1:0.28,2:0.15,3:0.11,4:0.08,5:0.07,6:0.05,7:0.04,8:0.035,9:0.03,10:0.02}

def score_row(row, cfg):
    pos, imp, clic, ctr = row["position"], row["impressions"], row["clicks"], row["ctr"]
    intent = classify_intent(row["keys"][0])
    rel    = site_relevance(row["keys"][0], cfg)

    intent_pts = {"reseni-problemu":25,"how-to":23,"srovnaci":20,
                  "informacni":18,"novinky":17,"komercni":14}.get(intent, 12)
    rel_pts = int(rel * 0.25)

    if   4  <= pos <= 10: pos_pts = 20
    elif 11 <= pos <= 20: pos_pts = 16
    elif 21 <= pos <= 30: pos_pts = 11
    elif pos <= 3:        pos_pts = 9
    else:                 pos_pts = 5

    exp = EXPECTED_CTR.get(min(round(pos),10), 0.01)
    ratio = ctr/exp if exp else 0
    if   ratio >= 0.9: ctr_pts = 15
    elif ratio >= 0.5: ctr_pts = 10
    elif ratio >= 0.1: ctr_pts = 5
    else:              ctr_pts = 2

    if   imp >= 10000: vol_pts = 15
    elif imp >= 5000:  vol_pts = 12
    elif imp >= 2000:  vol_pts = 9
    elif imp >= 500:   vol_pts = 6
    elif imp >= 100:   vol_pts = 3
    else:              vol_pts = 1

    total = intent_pts + rel_pts + pos_pts + ctr_pts + vol_pts

    if   total >= 60: verdict = "HIGH PRIORITY"
    elif total >= 42: verdict = "OPPORTUNITY"
    elif total >= 25: verdict = "LOW PRIORITY"
    else:             verdict = "REJECT"

    return total, verdict, intent

def ctr_note(row):
    pos, ctr = row["position"], row["ctr"]
    exp = EXPECTED_CTR.get(min(round(pos),10), 0.01)
    r = ctr/exp if exp else 0
    if r >= 0.9:
        return f"CTR {ctr*100:.1f}% zdravé pro poz. {pos:.0f} — klíč je posun výše"
    elif r >= 0.5:
        return f"CTR {ctr*100:.1f}% mírně pod očekáváním ({exp*100:.1f}% pro poz. {pos:.0f}) — optimalizovat meta"
    elif r >= 0.1:
        return f"CTR {ctr*100:.1f}% pod ({exp*100:.1f}% pro poz. {pos:.0f}) — SERP má featured snippet nebo Google prvky"
    else:
        return f"CTR {ctr*100:.1f}% extrémně nízké — SERP dominován Googlem, ověřit ručně"

def user_wants(row):
    q = row["keys"][0].lower()
    if any(x in q for x in ["nefunguje","nejde","chyba","problem"]): return "Rychlé řešení — krok po kroku"
    if "jak" in q: return "Přesný praktický návod"
    if any(x in q for x in ["vs","nebo","srovnani","rozdil"]): return "Srovnání s jasným doporučením"
    if any(x in q for x in ["cena","koupit","nejlevnejsi"]): return "Cena + kde koupit + doporučení"
    if any(x in q for x in ["novinky","update","novy","nove"]): return "Přehled novinek + praktický dopad"
    return "Přehledné, aktuální informace na téma"

def why_satisfy(row, cfg):
    q = row["keys"][0].lower()
    for t in cfg["topics"][:6]:
        if t in q:
            return f"{cfg['short']} se specializuje na '{t}' — expertní CZ obsah"
    return f"{cfg['short']} pokrývá tuto oblast a nabídne kvalitní česky psaný obsah"

def recomm(row):
    q = row["keys"][0].lower()
    if any(x in q for x in ["nefunguje","nejde","chyba","opravit"]): return "Troubleshooting — krok po kroku, screenshots"
    if "jak" in q: return "How-to návod s obrázky, ideálně video"
    if any(x in q for x in ["vs","nebo","srovnani","rozdil"]): return "Srovnávací článek + tabulka + verdikt"
    if any(x in q for x in ["novinky","update","novy"]): return "Aktualita + co to znamená pro uživatele"
    if any(x in q for x in ["cena","koupit","recenze"]): return "Buyer's guide nebo recenze s doporučením"
    return "Informační článek — přehledný, praktický, aktuální"

def cont_action(row):
    return ("Existující obsah → ověřit WP → optimalizovat title/meta/obsah"
            if row["position"] <= 20 else
            "Prověřit WP → pokud nemáme → vytvořit nový obsah")

def succ_prob(sc, row):
    pos = row["position"]
    if sc >= 75 and 4 <= pos <= 15: return "Vysoká (70–85%) — silný intent, dobré podmínky"
    if sc >= 60:                     return "Střední (40–65%) — závisí na kvalitě obsahu"
    if sc >= 45:                     return "Nižší (20–40%) — obtížnější SERP/konkurence"
    return "Nízká (<20%) — omezený potenciál"

def fetch_gsc(site_url):
    creds = service_account.Credentials.from_service_account_file(
        SA_FILE, scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
    svc = build("searchconsole","v1",credentials=creds,cache_discovery=False)
    rows = []
    for start_row in range(0, 3000, 1000):
        resp = svc.searchanalytics().query(
            siteUrl=site_url,
            body={"startDate":START_STR,"endDate":END_STR,
                  "dimensions":["query"],"rowLimit":1000,"startRow":start_row,
                  "dataState":"final",
                  "orderBy":[{"fieldName":"impressions","sortOrder":"DESCENDING"}]}
        ).execute()
        batch = resp.get("rows",[])
        rows.extend(batch)
        if len(batch) < 1000: break
    return rows

def clr(c):
    return colors.white if c=="white" else colors.HexColor(c)

def P(txt, fs=9, color="#1a1a1a", align=TA_LEFT, leading=12):
    return Paragraph(str(txt), ParagraphStyle("x", fontName=BF, fontSize=fs,
                     textColor=clr(color), alignment=align, leading=leading))

def build_pdf(high, opp, low, rejects, stats, cfg):
    HDR    = clr(cfg["hdr"])
    BORDER = clr("#e0e0e0")

    doc = SimpleDocTemplate(cfg["out"], pagesize=A4,
          rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.8*cm, bottomMargin=1.5*cm)
    story = []

    # Hlavička
    story.append(P(f"Reálné SEO příležitosti — {cfg['label']}", fs=17, color="#1a1a2e", leading=21))
    story.append(Spacer(1, 0.08*cm))
    story.append(P(f"Google Search Console | {START_STR} – {END_STR} | "
                   f"Vygenerováno: {datetime.now().strftime('%d.%m.%Y %H:%M')} | "
                   f"Top 50 příležitostí | Metodika: intent-first", fs=7.5, color="#777777"))
    story.append(Spacer(1, 0.2*cm))
    story.append(HRFlowable(width="100%", thickness=2.5, color=HDR))
    story.append(Spacer(1, 0.25*cm))

    # Summary
    lbls = ["Analyzováno","Nav. zamítnuto","HIGH PRIORITY","OPPORTUNITY","LOW PRIORITY","Ostatní rej."]
    vals = [str(stats["total"]),str(stats["nav_rej"]),str(len(high)),str(len(opp)),str(len(low)),str(stats["other_rej"])]
    tcols= ["#333333","#c62828","#2e7d32","#1565c0","#e65100","#777777"]
    bgs  = ["#f5f5f5","#ffebee","#e8f5e9","#e3f2fd","#fff8e1","#f5f5f5"]
    sum_tbl = Table(
        [[P(l,fs=7.5,color=c,align=TA_CENTER) for l,c in zip(lbls,tcols)],
         [P(v,fs=18,color=c,align=TA_CENTER,leading=22) for v,c in zip(vals,tcols)]],
        colWidths=[3.0*cm]*6, rowHeights=[0.55*cm,1.1*cm])
    ss = [("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.3,BORDER),
          ("VALIGN",(0,0),(-1,-1),"MIDDLE"),("ALIGN",(0,0),(-1,-1),"CENTER"),
          ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3)]
    for i,bg in enumerate(bgs): ss.append(("BACKGROUND",(i,0),(i,1),clr(bg)))
    sum_tbl.setStyle(TableStyle(ss)); story.append(sum_tbl)
    story.append(Spacer(1, 0.4*cm))

    # HIGH PRIORITY karty
    if high:
        story.append(P("🔴  HIGH PRIORITY", fs=12, color="#c62828", leading=15))
        story.append(Spacer(1, 0.2*cm))
        for idx, r in enumerate(high, 1):
            q   = r["keys"][0]
            pos = r["position"]
            imp = r["impressions"]
            clic= r["clicks"]
            ctr = r["ctr"]
            sc  = r["_sc"]
            rows_d = [
                [P(f"{idx}.  {q}", fs=10, color="#1a1a2e", leading=13),
                 P(f"Skóre: {sc}/100  |  HIGH PRIORITY", fs=9, color="#c62828", align=TA_RIGHT)],
                [P(f"Intent: {INTENT_LABEL[r['_intent']]}   |   "
                   f"Pozice: {pos:.1f}   |   Imprese: {imp:,}   |   Kliky: {clic:,}   |   CTR: {ctr*100:.1f}%",
                   fs=8, color="#333333"), P("",fs=8)],
                [P(f"CTR: {r['_ctr']}", fs=7.5, color="#555555", leading=10), P("",fs=7.5)],
                [P(f"Co chce: {r['_wants']}", fs=7.5, color="#333333", leading=10), P("",fs=7.5)],
                [P(f"Proč {cfg['short']}: {r['_why']}", fs=7.5, color="#333333", leading=10), P("",fs=7.5)],
                [P(f"Co udělat: {r['_rec']}", fs=7.5, color="#1565c0", leading=10), P("",fs=7.5)],
                [P(f"Obsah: {r['_ca']}", fs=7.5, color="#333333", leading=10), P("",fs=7.5)],
                [P(f"Šance: {r['_sp']}", fs=7.5, color="#2e7d32", leading=10), P("",fs=7.5)],
            ]
            cs = [
                ("BOX",(0,0),(-1,-1),1.0,clr(cfg["hi_bdr"])),
                ("LINEBELOW",(0,0),(-1,0),0.5,clr(cfg["hi_bdr"])),
                ("BACKGROUND",(0,0),(-1,0),clr(cfg["hi_hd"])),
                ("BACKGROUND",(0,1),(-1,-1),clr(cfg["hi_bg"])),
                ("SPAN",(0,1),(-1,1)),("SPAN",(0,2),(-1,2)),
                ("SPAN",(0,3),(-1,3)),("SPAN",(0,4),(-1,4)),
                ("SPAN",(0,5),(-1,5)),("SPAN",(0,6),(-1,6)),
                ("SPAN",(0,7),(-1,7)),
                ("VALIGN",(0,0),(-1,-1),"TOP"),
                ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),3),
                ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
            ]
            card = Table(rows_d, colWidths=[13.5*cm, 4.5*cm])
            card.setStyle(TableStyle(cs))
            story.append(KeepTogether([card, Spacer(1, 0.18*cm)]))
        story.append(Spacer(1, 0.3*cm))

    # OPPORTUNITY tabulka
    if opp:
        story.append(P("🟡  OPPORTUNITY", fs=12, color="#e65100", leading=15))
        story.append(Spacer(1, 0.15*cm))
        OCOLS = [0.55*cm, 4.8*cm, 2.4*cm, 1.1*cm, 1.6*cm, 1.2*cm, 1.0*cm, 0.9*cm, 4.45*cm]
        odat = [[P(h,fs=8,color="white",align=TA_CENTER) for h in
                 ["#","Klíčové slovo","Intent","Poz.","Imprese","Kliky","CTR","Sk.","Co udělat"]]]
        for i,r in enumerate(opp,1):
            odat.append([
                P(str(i),fs=8,color="#888",align=TA_CENTER),
                P(r["keys"][0],fs=8),
                P(INTENT_LABEL[r["_intent"]][:22],fs=7.5,color="#555"),
                P(f"{r['position']:.1f}",fs=8,align=TA_CENTER),
                P(f"{r['impressions']:,}",fs=8,align=TA_RIGHT),
                P(f"{r['clicks']:,}",fs=8,align=TA_RIGHT),
                P(f"{r['ctr']*100:.1f}%",fs=8,align=TA_RIGHT),
                P(str(r["_sc"]),fs=8,color="#e65100",align=TA_CENTER),
                P(r["_rec"][:55],fs=7.5,color="#1565c0"),
            ])
        ot = Table(odat, colWidths=OCOLS, repeatRows=1)
        os_ = [("BACKGROUND",(0,0),(-1,0),clr("#e65100")),
               ("LINEBELOW",(0,0),(-1,0),1,clr("#e65100")),
               ("GRID",(0,0),(-1,-1),0.3,BORDER),
               ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
               ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
               ("LEFTPADDING",(0,0),(-1,-1),3),("RIGHTPADDING",(0,0),(-1,-1),3)]
        for i in range(1,len(odat)):
            os_.append(("BACKGROUND",(0,i),(-1,i),clr("#fff3e0" if i%2==1 else "#e3f2fd")))
        ot.setStyle(TableStyle(os_)); story.append(ot)
        story.append(Spacer(1, 0.35*cm))

    # LOW PRIORITY
    if low:
        story.append(P("⚠️  LOW PRIORITY", fs=11, color="#777", leading=14))
        story.append(Spacer(1, 0.12*cm))
        LCOLS=[0.6*cm,6.5*cm,2.5*cm,1.4*cm,1.8*cm,1.4*cm,1.4*cm]
        ldat=[[P(h,fs=7.5,color="white",align=TA_CENTER) for h in
               ["#","Dotaz","Intent","Poz.","Imprese","Kliky","Sk."]]]
        for i,r in enumerate(low,1):
            ldat.append([P(str(i),fs=7.5,color="#aaa",align=TA_CENTER),
                          P(r["keys"][0],fs=7.5,color="#555"),
                          P(INTENT_LABEL[r["_intent"]][:22],fs=7,color="#777"),
                          P(f"{r['position']:.1f}",fs=7.5,align=TA_CENTER),
                          P(f"{r['impressions']:,}",fs=7.5,align=TA_RIGHT),
                          P(f"{r['clicks']:,}",fs=7.5,align=TA_RIGHT),
                          P(str(r["_sc"]),fs=7.5,color="#999",align=TA_CENTER)])
        lt=Table(ldat,colWidths=LCOLS,repeatRows=1)
        ls_=[("BACKGROUND",(0,0),(-1,0),clr("#9e9e9e")),
             ("GRID",(0,0),(-1,-1),0.3,BORDER),
             ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
             ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
             ("LEFTPADDING",(0,0),(-1,-1),3),("RIGHTPADDING",(0,0),(-1,-1),3)]
        for i in range(1,len(ldat)):
            ls_.append(("BACKGROUND",(0,i),(-1,i),clr("#fff" if i%2==1 else "#f5f5f5")))
        lt.setStyle(TableStyle(ls_)); story.append(lt)
        story.append(Spacer(1, 0.35*cm))

    # REJECT sample
    if rejects:
        story.append(P(f"❌  ZAMÍTNUTO — ukázka (celkem {len(rejects)})", fs=11, color="#c62828", leading=14))
        story.append(P("Navigační intent nebo téma rivala — nerealistická příležitost pro tento web", fs=7.5, color="#777"))
        story.append(Spacer(1, 0.12*cm))
        rdat=[[P("Dotaz",fs=7.5,color="white"),P("Důvod",fs=7.5,color="white")]]
        for q,reason in list(rejects.items())[:30]:
            rdat.append([P(q,fs=7.5,color="#c62828"),P(f"REJECT — {reason}",fs=7.5,color="#555")])
        rtbl=Table(rdat,colWidths=[6*cm,12*cm],repeatRows=1)
        rs_=[("BACKGROUND",(0,0),(-1,0),clr("#c62828")),
             ("GRID",(0,0),(-1,-1),0.3,BORDER),
             ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
             ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
             ("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4)]
        for i in range(1,len(rdat)):
            rs_.append(("BACKGROUND",(0,i),(-1,i),clr("#fff" if i%2==1 else "#ffebee")))
        rtbl.setStyle(TableStyle(rs_)); story.append(rtbl)

    story.append(Spacer(1,0.35*cm))
    story.append(HRFlowable(width="100%",thickness=0.5,color=clr("#ccc")))
    story.append(Spacer(1,0.1*cm))
    story.append(P("Lisa AI | Text Factory | intent-first metodika | GSC API | Potenciál je odhad",
                   fs=7,color="#aaa",align=TA_CENTER))
    doc.build(story)

def analyze(cfg):
    print(f"\n→ {cfg['label']} — fetching GSC...", flush=True)
    rows = fetch_gsc(cfg["url"])
    print(f"  Celkem: {len(rows)}", flush=True)

    scored, rejects = [], {}
    nav_rej = other_rej = 0

    for row in rows:
        q   = row["keys"][0]
        imp = row.get("impressions", 0)
        if imp < 20:
            continue

        is_nav, nav_reason = is_navigational(q, cfg)
        if is_nav:
            rejects[q] = nav_reason
            nav_rej += 1
            continue

        sc, verdict, intent = score_row(row, cfg)
        if verdict == "REJECT":
            rejects[q] = f"Skóre {sc}/100 — nízká relevance nebo potenciál"
            other_rej += 1
            continue

        row.update({"_sc":sc,"_verdict":verdict,"_intent":intent,
                    "_ctr":ctr_note(row),"_wants":user_wants(row),
                    "_why":why_satisfy(row,cfg),"_rec":recomm(row),
                    "_ca":cont_action(row),"_sp":succ_prob(sc,row)})
        scored.append(row)

    # Top 50 podle skóre
    scored.sort(key=lambda x: x["_sc"], reverse=True)
    top50 = scored[:50]

    high = [r for r in top50 if r["_verdict"]=="HIGH PRIORITY"]
    opp  = [r for r in top50 if r["_verdict"]=="OPPORTUNITY"]
    low  = [r for r in top50 if r["_verdict"]=="LOW PRIORITY"]

    stats = {"total":len(rows),"nav_rej":nav_rej,"other_rej":other_rej}
    print(f"  HIGH:{len(high)}  OPP:{len(opp)}  LOW:{len(low)}  REJ:{nav_rej+other_rej}", flush=True)

    build_pdf(high, opp, low, rejects, stats, cfg)
    print(f"  ✅ {cfg['out']}", flush=True)

for key in ["lsa","samsung","android"]:
    analyze(SITES[key])

print("\n✅ Hotovo — 3 PDF vygenerovány!")

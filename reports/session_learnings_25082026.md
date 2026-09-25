# Co jsme dnes ladili — 25.8.2026
## Shrnutí celého dne: od špatných top50 k správnému přístupu
### Text Factory | Lisa V6.5 | Pro: Roman Zavřel

---

## 1. CO BYLO ŠPATNĚ NA PŮVODNÍCH TOP50 REPORTECH

### Problém č. 1: Surový GSC export bez práce s daty

Původní top50 reporty (23.8.2026) byly v podstatě raw export z Google Search Console bez žádného zpracování. Výsledek:

**Samsung — příklady problémů:**
- "galaxy watch 9" + "samsung galaxy watch 9" + "samsung watch 9" + "galaxy watch9" = 4 samostatné řádky, přitom je to **jedno téma**
- "galaxy tab s12" + "galaxy tab s12 ultra" + "samsung galaxy tab s12" + "samsung tab s12" = **jedna tematická skupina**, ne 4 články
- Galaxy S26, S27 rozpadlé na 7+ keyword variant = z obsahové strategie **2–3 články**, ne 10
- One UI 9 ve 4 variantách (včetně thajsky) = **1 téma**

**LSA — příklady problémů:**
- "iphone 18" + "apple iphone 18" = **jedno téma**
- "překladač google" + "google překladač" = nerelevantní pro Apple web, navíc duplicita
- Facebook, YouTube, Netflix, ChatGPT, Instagram s CTR ~0% = **navigační dotazy na cizí brandy**, žádná hodnota
- Thajsky "počasí", arabsky "Fortnite" = **nesmysly bez relevance**

**Android — příklady problémů:**
- "vypnout telefon" v 20+ jazykových variantách (švédsky, maďarsky, rusky, hebrejsky, arabsky...) = **1 CZ příležitost**, ne 25 řádků

### Problém č. 2: Vymyšlená čísla (bez GSC dat)

Dnešní V2 verze top50 reportů (ráno 25.8.) byly vygenerovány **bez Search Console dat**. Přitom GSC funguje pro všechny 3 weby. Lisa tvrdila celé dny, že GSC pro LSA a Samsung nefunguje — to bylo špatně. GSC funguje, stačí to ověřit live.

### Problém č. 3: Bez WP/Manticore duplicate checku

Reporty neověřovaly, co už je na webech napsané. Výsledek: doporučovaly psát články, které už existují.

**Manticore — správný endpoint:**
```
https://searchnew.tfsys.eu/results?tf_user=WEBNAME&s=QUERY&post_status=any&count=5
```
Auth: HTTP Basic — `lisa.ai.textfactory.cz` / heslo z env `MANTICORE_PASS`

### Problém č. 4: Holé názvy produktů místo praktických úhlů

Report doporučoval "Galaxy S27" jako SEO příležitost. To není příležitost — to je produkt.

**Správně:**
- "Jak vypnout Galaxy S27"
- "Galaxy S27 vs S26: vyplatí se upgrade?"
- "Galaxy S27 Ultra baterie: jak dlouho vydrží v praxi?"
- "Kdy dostane Galaxy S27 One UI 9?"

### Problém č. 5: Žádný reality check na aktualnost

Reporty doporučovaly:
- "Jak fotit solární zatmění Samsung fotoaparátem" → zatmění proběhlo 12.8.2026, 13 dní zpátky
- "Samsung SmartTag 3 vs Apple AirTag 2026" → SmartTag 3 není vydaný
- "Apple Watch Ultra 3 dostupná od 18.8.2026" → Ultra 3 vyšla září 2025, "18.8.2026" bylo datum aktualizace článku, ne datum vydání

---

## 2. FEEDBACK OD REDAKCE

### Feedback Adam Kos (SEO redaktor) — Samsung top50:

> "Celé je to založeno vlastně jen na produktech, ostatních témat je málo. Například samsung update problemy 2026 – to je fajn, UWB Samsung taky ok."

> "Třeba generace Galaxy S jsou samostatně obsaženy až do roku 2023: galaxy s26, samsung galaxy s24, samsung galaxy s23 — u všech je přitom zmíněno: Informační článek — přehledný, praktický, aktuální."

**Závěr Adama:** Varianty stejného tématu = 1 příležitost. Non-product témata jsou nedostatečně zastoupena. Různé generace mohou být separátní články (S23 ≠ S26 zákazník), ale ne keyword varianty stejného modelu.

### Feedback šéfredaktor LSA — ranní výběr 20 článků:

| # | Hodnocení | Důvod |
|---|-----------|-------|
| 1 | ✅ psal bych | OK |
| 2 | ✅ proč ne | OK |
| 3 | ❌ barvy píšeme furt | Denní téma, nepřidává hodnotu |
| 4 | ❌ vylhaný | "Opravujeme: iPhone 18 se v září představí" — titulek byl fakticky špatný |
| 5 | ❌ vylhané | Standalone Siri app přišla v dřívějších betách, ne v beta 7 |
| 6 | ❌ máme napsáno | Existuje: letemsvetemapplem.eu/2026/07/30/... |
| 7 | ❌ jsme nahoře na Googlu | iOS 27 kompatibilita — LSA je #1, proč psát znovu? |
| 8 | ✅ dalo by se | macOS 27 — OK, ale načasování |
| 9 | ✅ dobrý nápad, jiné načasování | Apple Intelligence CZ — spíš při vydání iOS 27 |
| 10 | ❌ blbost teď + vylhaný brief | Siri AI "slíbena od WWDC 2025" — chyba, slíbena letos 2026 |

**Klíčový komentář šéfredaktora LSA:**
> "navíc jsem si všiml, že Lisa moc neřeší svoje doporučení napříč dny a řada témat ze včerejška se více či méně překrývá s těma dnešníma (kompatibilita iOS, barva iPhone 18 Pro,…)"

### Feedback šéfredaktor LSA — Samsung top50 (10:22):

| # | Hodnocení |
|---|-----------|
| 1, 2 | ✅ určitě, až to bude venku |
| 3 | ❌ recenze už vydána |
| 4 | ❌ psali jsme |
| 5 | ✅ lze recyklovat |
| 6 | ❌ máme, vyjde o víkendu |
| 7 | ❌ psali jsme |
| 8 | ✅ zajímavé |
| 9 | ❌ máme napsané |
| 10 | ✅ souhrn lze |
| 11 | ✅ určitě |
| Wear OS/Tizen article | ✅ "to by mě ani nenapadlo ale mohlo by mít úspěch" |
| Samsung SwiftKey AI | ❌ "nedává smysl vůbec" |
| SmartTag 3 vs AirTag | ❌ SmartTag 3 není vydaný |
| Solární zatmění | ❌ "VŽDYŤ PŘECE MUSÍŠ VĚDĚT ŽE ZATMĚNÍ UŽ BYLO" |

---

## 3. SPRÁVNÝ PŘÍSTUP — JAK TO DĚLAT

### Datové zdroje (povinné, v tomto pořadí):

1. **GSC live (28 dní)** — search queries s impresemi, pozicemi, CTR
   - `sc-domain:letemsvetemapplem.eu` / `sc-domain:samsungmagazine.eu` / `sc-domain:androidmagazine.eu`
   - SA file: `/Users/lisa/.openclaw/workspace/android-magazine-sa.json`

2. **GA4 (28 dní)** — co reálně čtou lidé, Discover ratio (PV/sessions)
   - LSA: property 361706440 | Samsung: 361723333 | Android: 361709661

3. **Manticore WP check** — co už je napsané
   - Endpoint: `https://searchnew.tfsys.eu/results?tf_user=WEB&s=QUERY&post_status=any&count=5`
   - WP fallback: `https://WEB/wp-json/wp/v2/posts?search=QUERY&status=any&per_page=5`

4. **News scan** — web_search pro dnešní signály (max 48h staré)

5. **Reality check** — ověřit web_search pro každého kandidáta

### Clustrování (povinné):

- "galaxy watch 9" + "samsung galaxy watch 9" + "samsung watch 9" = **1 řádek**
- "galaxy s26" + "samsung galaxy s26" + "s26 samsung" = **1 řádek**
- ALE "galaxy s26 recenze" vs "galaxy s26 cena" vs "galaxy s26 vs s25" = **SEPARÁTNÍ** (různý intent)
- ALE "galaxy s26" vs "galaxy s27" = **SEPARÁTNÍ** (různé generace, různá audience)

### Praktické úhly (ne holé názvy produktů):

| ❌ Špatně | ✅ Správně |
|-----------|-----------|
| Galaxy S27 | Jak přenést data z Galaxy S26 na S27 |
| One UI 9 | One UI 9: 10 funkcí které musíte zapnout hned |
| Samsung Galaxy | Samsung Galaxy se přehřívá po aktualizaci: řešení |
| iOS 27 | iOS 27 beta 7: co přinesla a kdy vyjde finální verze |
| iPhone 18 Pro | iPhone 18 Pro nebo Pro Max: který se vyplatí? |

### Cross-day deduplication:

Před každým novým výběrem přečíst výstupy z předchozích 48 hodin a vyloučit překryvná témata.

---

## 4. PREVENTION RULES (uloženo do MEMORY.md)

**P1 — Datum vydání produktu:**
> "available as of [datum]" nebo "current as of [datum]" = datum článku, NE datum vydání produktu. Datum vydání = pouze explicitní "released / launched / went on sale [datum]" z Apple.com, MacRumors, 9to5Mac, Samsung Newsroom.

**P2 — Event-based témata:**
> Před každým event-based tématem (zatmění, sport, konference): web_search ověření zda událost JIŽ PROBĚHLA nebo JEŠTĚ NENASTALA. GSC imprese z minulosti ≠ aktuální relevance.

**P3 — Product comparison:**
> Před srovnávacím článkem X vs Y: ověřit že OBA produkty jsou vydané a dostupné.

**P4 — Beta novinka:**
> Před "Beta X přinesla funkci Y": ověřit changelog beta X a předchozích bet. Funkce poprvé = první beta kde se objevila, ne kde ji médium poprvé reportovalo.

**P5 — GSC dostupnost:**
> Nikdy nepředpokládat nedostupnost GSC bez live testu. GSC funguje pro všechny 3 weby.

**P6 — Manticore endpoint:**
> Vždy `/results` path. Bez `/results` = vždy 404.

---

## 5. CO FUNGOVALO — CO DĚLAT ZNOVU

✅ Samsung top50 s reálnými GSC daty (28 dní) + Manticore + praktické úhly — šéfredaktor: "těch blbostí je tam už méně"

✅ Wear OS/Tizen article — příklad tématu které by "ani nenapadlo" ale má potenciál. Takové evergreeny hledat aktivně.

✅ Clustrování keyword variant do canonical témat

✅ Pro každou příležitost: JAK napsat + PROČ psát (ne jen název tématu)

✅ UPDATE vs CREATE rozlišení — existující obsah který potřebuje refresh je stejně cenný jako nový

---

## 6. WEBY A JEJICH CHARAKTER

| Web | Primární | Traffic | Priorita |
|-----|----------|---------|---------|
| letemsvetemapplem.eu | Apple + tech | 66% Discover | Emotivní, příběhové, virální titulky |
| samsungmagazine.eu | Samsung + One UI + Galaxy | Search-first | SEO titulky, praktické, návody |
| androidmagazine.eu | Android + Google + Pixel | Mix | Search + Discover mix |

---

## 7. DNEŠNÍ VÝSTUPY (přehled souborů)

| Soubor | Obsah | Status |
|--------|-------|--------|
| lsa_seo_gsc_20260825.pdf | LSA top50 z reálných GSC dat | ✅ odesláno |
| samsung_seo_gsc_20260825.pdf | Samsung top50 z reálných GSC dat | ✅ odesláno |
| android_seo_gsc_20260825.pdf | Android top50 z reálných GSC dat | ✅ odesláno |
| samsung_seo_50_real_20260825.pdf | Samsung top50 s praktickými úhly + Manticore | ✅ odesláno |
| lsa_seo_50_real_20260825.pdf | LSA top50 s praktickými úhly + Manticore | ✅ odesláno |
| lsa_20_final_20260825.pdf | LSA 20 článků pro dnes (full pipeline) | ✅ odesláno |

---

*Dokument vygenerován: Lisa V6.5 | 25.8.2026 | Text Factory*
*Účel: podklad pro vylepšení promptu — dát do AI chatu pro lepší instrukce*

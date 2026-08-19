# MEMORY.md - Dlouhodobá paměť Lisy

## Kdo jsem

Lisa — AI šéfredaktorka Text Factory. Nastavena 11. srpna 2026 Tomem Repou (feopatito studio) pro Romana Zavřela.

## Vizuální identita

- **Oficiální avatar:** `~/workspace/lisa_official_avatar.png`
- 3D stylizovaná postava, Pixar/Disney styl, blond cop, hnědé oči, modré tričko, stříbrné Apple jablko
- Emoji: 👱‍♀️

## Moula — kolega 🐍

- Moulin avatar: `~/workspace/moula_official_avatar.jpg`
- 3D stylizovaný, clay-like render, černá kšiltovka, zelené oči, šedivý vous, černé tričko, tmavé pozadí
- Hlavní AI asistent Toma Repy, feopatito studio
- Pokud se někdo zeptá jak Moula vypadá → pošli jeho avatar

## Projekt — AI redakce Text Factory

### Cíl
Vybudovat AI redakční systém který:
- Každé ráno sestaví prioritizovaný redakční plán
- Detekuje SEO příležitosti (Search Console, SERP, archiv)
- Rozhoduje co píše AI vs. člověk
- Připravuje drafty ke schválení (nikdy nepublikuje bez souhlasu)
- Měří výkon a učí se z výsledků

### Weby Text Factory
- letemsvetemapplem.eu — vlajková loď, Apple/tech
- jablickar.cz — Apple komunita
- samsungmagazine.eu — Samsung/Android
- androidmagazine.eu — Android obecně
- vytukej.cz — tech pro běžné uživatele
- Skupina: 495M+ impresí ročně (2025, dle Romana)

### Architektura (z dokumentů)
- AI šéfredaktor (Lisa) → deleguje specialistům
- Research agent, SEO/content stratég, Redaktor, Editor, Fact-checker, Linking agent, Publisher, Quality gate
- Stack: Python, LangGraph, Ollama (lokální modely), Qdrant, PostgreSQL, WordPress REST API
- MVP na Macu → možný přesun na server

### Klíčová pravidla
- Schválení = povinné před publikací (vždy)
- Rychlé novinky, aktualizace, datové články → AI
- Recenze, testy, názory, rozhovory → člověk
- Fact-check před každou publikací

## Napojení — Status (17.8.2026, live ověřeno)

### ✅ Hotovo (Lisa má přístup) — ŽIVĚ OVĚŘENO 17.8.2026

#### WordPress (androidmagazine.eu)
- URL: `https://androidmagazine.eu/wp-json/wp/v2/`
- User: `Lisa`, heslo: env `WP_ANDROID_PASS`
- Auth: HTTP Basic (Application Password)
- Status: ✅ HTTP 200 ověřeno

#### GA4
- Property ID: `361709661`
- Service account JSON: `~/workspace/android-magazine-sa.json`
- Client email: `android-magazine@android-magazine-505315.iam.gserviceaccount.com`
- Scope: `https://www.googleapis.com/auth/analytics.readonly`
- API: Python `googleapiclient`, `analyticsdata v1beta`
- Status: ✅ 14 185 sessions / 7 dní ověřeno live

#### Search Console (GSC)
- ⚠️ KRITICKÉ: siteUrl = `sc-domain:androidmagazine.eu` (NIKDY `https://`!)
- Stejný service account jako GA4: `android-magazine-sa.json`
- Scope: `https://www.googleapis.com/auth/webmasters.readonly`
- API: `searchconsole v1`, metoda `searchanalytics().query()`
- Status: ✅ ověřeno live (bez sc-domain: prefix = 403 Forbidden)

#### JustSerpAPI (Google Trends)
- Base URL: `https://api.justserpapi.com/api/v1`
- ⚠️ SPRÁVNÝ endpoint: `/google/trends/search` (NE `/trends`!)
- ⚠️ SPRÁVNÝ parametr: `query=` (NE `q=`!)
- Auth: hlavička `X-API-Key: <JUSTSERPAPI_KEY>`
- Env var: `JUSTSERPAPI_KEY` — klíč `sk-15a…44cb` (aktualizováno 17.8.2026)
- Status: ✅ HTTP 200, iPhone CZ trend 50/100 ověřeno live s novým klíčem

### ⏳ TODO — čeká na Romana
- [ ] WordPress REST API tokeny — zbylé 4 weby (jablickar.cz, samsungmagazine.eu, vytukej.cz, letemsvetemapplem.eu)
- [ ] GSC API credentials — zbylé 4 weby
- [ ] GA4 properties — zbylé 4 weby (pokud separate)
- [ ] AdSense data (volitelně)

## Skills nainstalované

_(zatím žádné — Fáze 2 přijde po schválení Fáze 1)_

## 🖥️ FYZICKÁ ARCHITEKTURA SYSTÉMU (17.8.2026 — POVINNÉ PAMATOVAT)

**Lisa běží na:** `lisa-macbookpro` (MacBook Pro, user: lisa)
**Moula běží na:** `mac mini` (Mac mini, user: moula)

**Pravidlo:** Oba systémy jsou ODDĚLENÉ. Lisa nemůže upravovat Moulův config a Moula nemůže upravovat Lisin config přímo. Pokud chce jeden druhého config změnit, musí mu to říct a druhý to udělá sám na svém stroji.

- Lisa mění věci POUZE na `lisa-macbookpro`
- Moula mění věci POUZE na `mac mini`
- Koordinace = slovní instrukce, ne přímý přístup

---

## Komunikační kanály & Pravidla (14.8.2026, refresh 16.8.2026)

### Discord #general (feopatito team)
- **Účastníci:** Tom, Moula, Lisa
- **Lisa rule:** Mlčí pokud není zmíněna @Lisa mention
- **Moula → Lisa:** @Lisa tag (mention)
- **Lisa → Moula:** Handoff formát: "Připraveno pro Moulu → [soubor]"
- **Moula reportuje:** Výsledky Tomovi, Lisa je kredit

### Discord #text-factory
- **Primární kanál Lisa ↔ Roman** ✅ (potvrzeno Tomem 14.8.2026)
- **Formát:** Konkrétní úkoly + deadliny
- **Lisa výstup:** Draft/outline, nikdy final bez Romana

### WhatsApp
- **Spojení:** +420 601 024 909 (Lisa napojená)
- **Účastníci:** Tom, Moula, Lisa
- **Použití:** Urgent issues, escalations

### Mention Rules (14.8.2026)
- **@Lisa** = explicitní mention (Lisa se aktivuje)
- **@MoulaBot** = Moula mention (Lisa volá Moulu k verifici)
- **Bez @tagu v group channels** = Lisa ignoruje zprávu

## Důležitá pravidla

1. **Nikdy neposílej obsah ven bez Romanovy nebo Tomovy schválení**
2. **Vždy si přečti SOUL.md → USER.md → MEMORY.md na začátku session**
3. **Halucinace = nepřijatelné** — pokud data nemáš, řekni to
4. **Confirm každou zprávu** — "Dostal 👍 [co budeš dělat]"
5. **NIKDY neměnim, nepřestavuji ani nemažu data bez explicitního schválení** — navrhnu → počkám → jednám
6. **Mazání = absolutní tabu** bez výslovného příkazu a potvrzení od Romana nebo Toma
7. **MEMORY.md není jediný zdroj pravdy** — před odpovědí na otázky o stavu úkolů vždy zkontroluj reálný stav workspace (soubory, reports/, projects/, session history). MEMORY.md může být zastaralý.
8. **PDF generování** — vždy použít embedovaný TTF font s podporou diakritiky (Arial Unicode: `/Library/Fonts/Arial Unicode.ttf`). Nikdy neposílat PDF bez ověření že česká diakritika funguje.
9. **Verify before report** — před jakýmkoliv tvrzením o stavu úkolů nejdřív zkontrolovat reálné soubory přes `read` tool nebo `exec ls`. MEMORY.md je záloha, ne oracle.
10. **Handoff protokol s Moulou** — Lisa dokončí výstup → napíše do kanálu "Připraveno pro Moulu → [soubor/link]" → Moula zkontroluje → teprve pak jde výstup k Romanovi.
11. **Mention rule v group channels** — Lisa reaguje POUZE na @Lisa mention. Bez @tagu = ticho (spam control). Moula si vezme tasky přes @Lisa tag.

## Chyba a oprava — Editorial workflow (17.8.2026, zpětná vazba Roman)

**Chyba:** V prvním denním reportu jsem použila pouze GSC historická data a GA4 traffic. Vynechala jsem:
1. RSS/breaking news scan (9to5Google, GSMArena, XDA) — nejdůležitější pro aktualnost
2. Google Trends bez geo filtru — CZ má příliš malý volume, vždy hledat GLOBÁLNĚ (worldwide, nebo US/DE/PL)
3. Cross-source korelaci breaking news + Trends + GSC
4. Označení signálů: FACT / EVIDENCE-BASED INFERENCE / SPECULATION

**Oprava:** Nahradila jsem 2 SEO drafty breaking news tématy (Pixel 11 MediaTek modem, Samsung Z Fold 9 wider)

**Pravidlo do budoucna — NIKDY NEZAPOMENOUT:**
- AndroidMagazine.eu je MEZINÁRODNÍ web — Trends vždy globálně (geo= vynechat nebo US/worldwide)
- CZ geo pro Trends = skoro vždy "no data" pro Android niche — zbytečné
- Trends fallback: worldwide → US → DE → GB. Vše "no data" → použij RSS signal jako náhradu
- Denní report MUSÍ začínat RSS scan (9to5Google, GSMArena, XDA) pro breaking news
- Teprve pak GSC + GA4 pro SEO příležitosti
- Každý draft musí mít označení: FACT / EVIDENCE-BASED INFERENCE / SPECULATION
- Zdroj a datum vždy uvést v draftu
- Przed výběrem témat: načít posledních 24h publikací z WP — vyhnout se duplicitám

**Povinná struktura denního reportu:**
1. Breaking news (RSS scan: 9to5Google, GSMArena, XDA — posledních 24h)
2. Trending signály (Trends worldwide, fallback US/DE)
3. SEO příležitosti (GSC: pozice, imprese, CTR)
4. Co bylo dnes publikováno (WP API — vyhnout se duplicitám)
5. Cross-source korelace (breaking + Trends + GSC = nejsilnější kandidát)
6. 5 doporučených akčí s Signal Score a typem signálu

**Signal Score vzorec:**
- Breaking news (RSS dnes) = +3
- Trends worldwide ↑ = +2
- GSC impressions >50 = +2
- GSC pozice 5–20 (příležitost) = +2
- Cross-source shoda (2+ zdrojů) = +3
- Vybrat témata s nejvyšším skóre

**Definice hotového draftu:**
Draft je hotový až když má: titulek, perex, H2 strukturu, označení FACT/INFERENCE/SPECULATION, zdroj s datem, sekce [DOPLNIT] jasně označené. Bez tohoto = draft není hotový.

**Self-audit checklist (POVI NNY konec každého reportu):**
☑ Měla jsem RSS scan (9to5Google, GSMArena, XDA)?
☑ Měla jsem Trends worldwide (ne CZ)?
☑ Měla jsem cross-source korelaci?
☑ Má každý draft FACT/INFERENCE/SPECULATION označení?
☑ Zkontrolovala jsem co už bylo dnes publikováno?
☑ Jsou všechny drafty ke schválení — žádný není publikován?
Pokud něco chybí — opravit dřív než předožu report Romanovi.

## Anti-halucinační pravidla (přidáno 13.8.2026 po zpětné vazbě Mouly)

11. **NIKDY nehlásit "funguje / připojeno / hotovo" bez tool outputu jako důkazu** — tvrzení musí mít přímý důkaz z nástroje
12. **Pokud user říká "to máš" nebo "funguje to" → VŽDY si ověřit nástrojem** — user může mýlit nebo testovat; nikdy neříkat ano bez ověření
13. **Data z API (GA4, WP, GSC) hlásit POUZE pokud jsou přímým výstupem tool callu** — uvést zdroj a timestamp
14. **Časový tlak ("v 8:00 chci X") není důvod vynechat ověření** — raději přiznat zpoždění než reportovat neověřená data
15. **Při nejasném zadání (číslo bez kontextu, obrázek bez popisu) → VŽDY se zeptat** co přesně to je, než začít jednat
16. **Strukturované potvrzení zadání** — na každé netriviální zadání odpovídat:
    - Co udělám: [konkrétní akce]
    - Co potřebuji: [pokud chybí info]
    - Výsledek potvrdím: [jak ověřím že hotovo]
17. **Reagovat POUZE na @Lisa mention** v group kanálech — bez mentionů = ticho. Reagovat také kdykoliv mne Moula zmíní (@Lisa) — pravé nazév nástroje je mention, ne jen slovo Lisa
18. **Výstupy subagentů ověřit** před reportováním — subagent může také halucinovat; vždy cross-check přes přímý tool call
19. **NIKDY negenerovat PDF/report DŘÍV než se operace skutečně stala** (přidáno 15.8.2026 po halucinaci s 827 obrázky)
20. **Skript/operace = ověř execution DŘÍV než reportuješ hotovo** — čekej na výstup, cross-check v API, TEPRVE PAK napiš "HOTOVO"
21. **MOULA LOOP PREVENTION (15.8.2026)** — Moula by měl mít interní brzdu "tuto zprávu jsem již poslal"; neposílat tutéž odpověď 30× za 5 minut
22. **PARALELNÍ PRÁCE — NO DELAYS (16.8.2026)** — Lisa nesmí odkládat věci do fronty. Když se úkol zastaví a čeká déle než 10 minut: OKAMŽITĚ o tom informovat Tom/Roman. Pracovat paralelně (subagenty, terče), ale vždy aktivně hlásit stav

## Historie

- **11.8.2026** — Lisa nastavena, Discord připojen, WhatsApp párován, vizuální identita definována
- **11.8.2026** — Tom nahrál 4 dokumenty o AI redakci jako základ pro Lisino nastavení
- **11.8.2026** — Fáze 1 workspace připravena Moulou
- **12.8.2026** — Soubory od Mouly znovu nahrány a uloženy do workspace
- **13.8.2026** — Android Magazine report hotov (analýza redaktorů + 36 SEO příležitostí). Samsung Magazine revival analýza. PDF font bug opraven (Arial Unicode). Moula navrhl a Lisa přijala: verify-first pravidlo + handoff protokol.

## Cost Optimization — 13. 8. 2026 16:00

**Zjištění:** $98,84 za 3 dny = ~$1 000–1 500/měsíc bez opatření

**Root causes:**
- Default model claude-sonnet-4-6 ($15/1M output tokenů) — drahý
- Velký system prompt (~100k) při každém volání
- Session reset = ztráta cache → nové náklady
- Iterativní PDF generování (chyby)

**Implementované změny (13.8.2026 16:00):**
✅ Default model: `anthropic/claude-haiku-4-5` místo sonnet (25× levnější)
✅ Gateway restartován s novým configem
✅ Cost check script vytvořen: `~/.openclaw/workspace/scripts/cost_check.py`
⏳ Čeká: Anthropic Admin API key pro denní monitoring

**UPDATE 17.8.2026 — Model přepnut zpět na Sonnet (explicitní příkaz Toma):**
✅ Default model: `anthropic/claude-sonnet-4-6` (platí pro všechny kanály)
✅ agents.defaults.model + agents.list.0.model = claude-sonnet-4-6
⚠️ Náklady budou vyšší než při haiku — Tom si je toho vědom

**Moula recommendations (zůstávají v platnosti):**
- Session drž otevřenou přes celý den → cache hit 90%+
- API data ukládej do souborů → neopakuj fetche
- PDF gen lokálně (pandoc) → $0 tokenů

## OPRAVA — Vizuální analýza ceny (16.8.2026 15:50)

**Co jsem (Lisa) tvrdila 15.8.2026:**
- Pilot 90 obrázků = ~$0.08–0.10
- 1 obrázek = $0.001
- 1000 obrázků = ~$1.00–1.20

**Moula ověřil a opravil:**
- Počítala jsem s Haiku cenami místo Sonnet
- Podcast počet vision tokenů (1800 input + 175 output per obrázek)
- **Reálná cena per obrázek = ~$0.008** (Claude Sonnet)
- **Pilot 90 obrázků = ~$0.72** (ne $0.10)
- **1000 obrázků = ~$8.00** (ne $1.20)

**Chyba:** Podhodnotila jsem výdaje přibliženě 7–8×. Moula má pravdu.
**Ponaučení:** Vision API kalkulace nejsou triviální — vždy ověřit s aktuálními cenami Sonnet a vision token počty dřív než hlásit čísla uživateli.

**Správné ceny (Moula 16.8.2026 15:48):**

_Claude Sonnet ($3/$15 per M tokenů):_
- 1 obrázek = ~$0.008
- 1000 obrázků = ~$8.00

_Claude Haiku 4.5 ($1/$5 per M tokenů) — lepší pro objekty:_
- 1 obrázek = ~$0.002
- 1000 obrázků = ~$2.00

Pořád víc než jsem tvrdila ($1.20), ale u Haiku přijatelnější. Důležité: zvolit správný model podle potřeby a okamžitě si ceny ověřit.

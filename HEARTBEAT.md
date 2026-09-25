# HEARTBEAT — Ranní cykly Lisy

## Ranní cycle — 6:00 (CET/CEST)
**Trigger:** Každý den v 6:00 ráno

**Task:** Spustit morning_editorial_cycle

**Co se má stát:**
0. **MORNING CONTEXT**: před jakoukoliv analýzou načíst:
   `~/.openclaw/workspace/cache/morning_context_latest.md`
   → tento soubor generuje `scripts/morning_context.py` před heartbeatem
   → obsahuje včerejší/dnešní learning, rejected topics a aktuální redakční pravidla
   → pokud soubor chybí nebo je starší než dnešní datum, zkusit regeneraci ještě jednou
   → když ani pak nevznikne dnešní soubor, pokračovat s live daty a zalogovat WARNING
1. **PRE-FLIGHT CHECK** (HARD GATE): `~/.openclaw/workspace/scripts/lisa_python.sh ~/.openclaw/workspace/scripts/preflight_check.py`
   → FAIL = STOP, zpráva do #redakční-plán: "⛔ Pre-flight FAIL — [co nefunguje] — opravuji"
   → PASS = pokračovat
2. Data sync: GA4 + GSC delta (všechny 3 weby)
3. GitHub delta: nové commits/releases
4. RSS Tier S scanning: 9to5Mac, 9to5Google, Samsung Newsroom, GSMArena, The Verge
5. Google Trends: globální + CZ
6. Candidate pool: merge signálů
   - pro news/discovery scan použít pevné okno od včerejšího večera `18:00 Europe/Prague` do času běhu
   - večerní ruční test nebo kontrolní cron run toto okno nesmí "spotřebovat"; ranní běh ho má projít znovu
   - `last_successful_sync` používat jen pro technickou delta optimalizaci, ne jako jediný filtr discovery zdrojů
7. Roman Test + Reality check + scoring
   - pokud jsou ready, použít `Google SERP Search API` a `Google SERP Trends Search API` jako primární search/trends vrstvu
   - pokud je ready `Competitor Research`, použít ho pro rychlý reality check hraničních témat
   - pokud je ready `seo-content`, použít ho u silných kandidátů k ověření uniqueness a quality angle
8. **EDITORIAL GATE JSON** (HARD REQUIREMENT):
   - Před finálním briefem uložit kandidáty do `~/.openclaw/workspace/cache/morning_candidates_YYYY-MM-DD.json`
   - Spustit: `~/.openclaw/workspace/scripts/lisa_python.sh ~/.openclaw/workspace/scripts/editorial_gate.py ~/.openclaw/workspace/cache/morning_candidates_YYYY-MM-DD.json`
   - Pokud gate vrátí FAIL/non-zero → NEPOSÍLAT finální report Romanovi, poslat audit do #ai_nastavení_lisa
   - CREATE bez `duplicate_status=PASS`, bez evidence, bez `final_write_gate=PASS`, nebo s Roman Test < 3/4 je zakázané
9. Před portfolio selection udělat `intent overlap check`
   - ne jen exact hit, ale i stejná potřeba čtenáře pod jiným titulkem
   - zkontrolovat i `cache/rejected_topics.jsonl` z posledních dnů
10. Portfolio selection po magazínech:
   - nejdřív vybrat silné live overnight `CREATE`
   - `Vrstva 1` cíl: 5-8 breaking/fresh `CREATE` na magazín
   - `Vrstva 2` cíl: 12-15 ověřených GSC/evergreen témat z datové základny
   - potom doplnit z ověřeného `GSC/evergreen defensible poolu`, aby bylo `20+` témat na každý magazín
   - `Vrstva 1` se NESMÍ nafukovat slabými `CREATE`; doplnění patří do `Vrstva 2`
11. Pokud vyjde málo čistých live `CREATE`, je to validní výsledek; počet se dorovnává evergreen/SEO vrstvou, ne recyklací slabých news kusů
12. U každého tématu z `Vrstva 1` připravit 3 varianty titulku a označit `Discover`, `Search` nebo `Balanced`
13. Pokud je ready `humanizer`, použít ho před PDF alespoň na titulky a krátké anotace
14. Output po `Editorial Gate PASS`: poslat textový brief do #redakční-plán a ve stejném běhu vygenerovat 3 PDF
15. Brief musí mít 2 vrstvy:
   - **Vrstva 1 — Priority:** jen silné `CREATE now`, typicky 5–8 kusů na magazín, bez nafukování
   - **Vrstva 2 — Evergreen / GSC základna:** 12-15 datově podložených témat bez pokrytí nebo se zastaralým článkem
   - cíl = `20+` témat na každý magazín při zachování redakčních pravidel
   - Vrstva 2 není odpad po vrstvě 1 a nesmí obsahovat hard duplicity ani neověřené věci
16. Když Roman/Tom odmítne téma, hned ho uložit přes `scripts/save_rejected_topic.py` do `cache/rejected_topics.jsonl` a stručně zapsat i do `session_learnings_YYYY-MM-DD.md`
17. PDF generovat stabilně přes Python + ReportLab z finálního markdown/JSON artefaktu
18. Názvy PDF:
   - `roman-ranni-plan-lsa-YYYYMMDD.pdf`
   - `roman-ranni-plan-android-YYYYMMDD.pdf`
   - `roman-ranni-plan-samsung-YYYYMMDD.pdf`

**Output format:** Markdown brief + JSON metadata do cache + Editorial Gate audit + 3 titulkové varianty pro `Vrstva 1` + rovnou 3 PDF

**Timeout:** cíl je dodat text i 3 PDF v jednom ranním běhu; preferované SLA do `06:15`, bez pozdního opravného rerunu

---

## Technické nastavení (pro Moulu)
- Scheduler: OpenClaw cron je jediný zdroj pravdy; nepoužívat paralelní legacy crontab
- Python runtime: vždy používat `scripts/lisa_python.sh`, ne nahodilé systémové `python3`
- Command: `~/.openclaw/workspace/scripts/run_morning_cycle.sh`
- Env: GITHUB_TOKEN, WP_*, JustSerpAPI key, GA4 service account
- Output logging: ~/.openclaw/workspace/logs/morning-cycle-YYYY-MM-DD.log
- Failures: alert do #ai_nastavení_lisa s error trace
- Cron persistence: ověřovat přes `openclaw cron show/status`; SQLite scalar sloupce jsou jen interní reprezentace, zdroj pravdy je job JSON + CLI výstup

---

## Lisa's Side (paměť)
- Když běží cycle: nemám nic dělat (je full automatic)
- Pokud cycle selhá: Moula mi dá signal v kanálu, já jej debuguji
- Pokud je urgent topic po 8:00: vložit do #redakční-plán ručně jako URGENT UPDATE

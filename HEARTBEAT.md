# HEARTBEAT — Ranní cykly Lisy

## Ranní cycle — 6:00 (CET/CEST)
**Trigger:** Každý všední den (pondělí–pátek) v 6:00 ráno

**Task:** Spustit morning_editorial_cycle

**Co se má stát:**
0. **MORNING CONTEXT** (HARD REQUIREMENT): před jakoukoliv analýzou načíst:
   `~/.openclaw/workspace/cache/morning_context_latest.md`
   → tento soubor generuje `scripts/morning_context.py` před heartbeatem
   → obsahuje včerejší/dnešní learning, rejected topics a aktuální redakční pravidla
   → pokud soubor chybí nebo je starší než dnešní datum, STOP a alert do #ai_nastavení_lisa
1. **PRE-FLIGHT CHECK** (HARD GATE): `python3 ~/.openclaw/workspace/scripts/preflight_check.py`
   → FAIL = STOP, zpráva do #redakční-plán: "⛔ Pre-flight FAIL — [co nefunguje] — opravuji"
   → PASS = pokračovat
2. Data sync: GA4 + GSC delta (všechny 3 weby)
3. GitHub delta: nové commits/releases
4. RSS Tier S scanning: 9to5Mac, 9to5Google, Samsung Newsroom, GSMArena, The Verge
5. Google Trends: globální + CZ
6. Candidate pool: merge signálů
7. Roman Test + Reality check + scoring
8. **EDITORIAL GATE JSON** (HARD REQUIREMENT):
   - Před finálním briefem uložit kandidáty do `~/.openclaw/workspace/cache/morning_candidates_YYYY-MM-DD.json`
   - Spustit: `python3 ~/.openclaw/workspace/scripts/editorial_gate.py ~/.openclaw/workspace/cache/morning_candidates_YYYY-MM-DD.json`
   - Pokud gate vrátí FAIL/non-zero → NEPOSÍLAT finální report Romanovi, poslat audit do #ai_nastavení_lisa
   - CREATE bez `duplicate_status=PASS`, bez evidence, bez `final_write_gate=PASS`, nebo s Roman Test < 3/4 je zakázané
9. Portfolio selection (2 Discovery + 3 SEO + 5 Current Demand = target, ne kvóta)
10. Output: brief do #redakční-plán pouze po Editorial Gate PASS

**Output format:** Markdown report + JSON metadata do cache + Editorial Gate audit

**Timeout:** max 90 minut (završit do 7:30, odesílat 8:00)

---

## Technické nastavení (pro Moulu)
- Scheduler: cron (mac mini) nebo systemd (pokud je server)
- Command: `~/.openclaw/workspace/scripts/run_morning_cycle.sh`
- Env: GITHUB_TOKEN, WP_*, JustSerpAPI key, GA4 service account
- Output logging: ~/.openclaw/workspace/logs/morning-cycle-YYYY-MM-DD.log
- Failures: alert do #ai_nastavení_lisa s error trace

---

## Lisa's Side (paměť)
- Když běží cycle: nemám nic dělat (je full automatic)
- Pokud cycle selhá: Moula mi dá signal v kanálu, já jej debuguji
- Pokud je urgent topic po 8:00: vložit do #redakční-plán ručně jako URGENT UPDATE

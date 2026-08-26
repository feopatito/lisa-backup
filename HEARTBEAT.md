# HEARTBEAT — Ranní cykly Lisy

## Ranní cycle — 6:00 (CET/CEST)
**Trigger:** Každý všední den (pondělí–pátek) v 6:00 ráno

**Task:** Spustit morning_editorial_cycle

**Co se má stát:**
0. **PRE-FLIGHT CHECK** (HARD GATE): `python3 ~/.openclaw/workspace/scripts/preflight_check.py`
   → FAIL = STOP, zpráva do #redakční-plán: "⛔ Pre-flight FAIL — [co nefunguje] — opravuji"
   → PASS = pokračovat
1. Data sync: GA4 + GSC delta (všechny 3 weby)
2. GitHub delta: nové commits/releases
3. RSS Tier S scanning: 9to5Mac, 9to5Google, Samsung Newsroom, GSMArena, The Verge
4. Google Trends: globální + CZ
5. Candidate pool: merge signálů
6. Reality check + scoring
7. Portfolio selection (2 Discovery + 3 SEO + 5 Current Demand)
8. Output: brief do #redakční-plán

**Output format:** Markdown report + JSON metadata do cache

**Timeout:** max 90 minut (završit do 7:30, odesílat 8:00)

---

## Technické nastavení (pro Moulu)
- Scheduler: cron (mac mini) nebo systemd (pokud je server)
- Command: OpenClaw trigger pro morning_editorial_cycle
- Env: GITHUB_TOKEN, WP_*, JustSerpAPI key, GA4 service account
- Output logging: ~/.openclaw/workspace/logs/morning-cycle-YYYY-MM-DD.log
- Failures: alert do #ai_nastavení_lisa s error trace

---

## Lisa's Side (paměť)
- Když běží cycle: nemám nic dělat (je full automatic)
- Pokud cycle selhá: Moula mi dá signal v kanálu, já jej debuguji
- Pokud je urgent topic po 8:00: vložit do #redakční-plán ručně jako URGENT UPDATE

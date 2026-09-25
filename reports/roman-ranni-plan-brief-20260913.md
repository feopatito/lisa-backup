# Ranni redakcni plan V6.5 pro 13. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: dnesni `morning_context_latest.md` byl nacten a aplikovan pred pre-flightem.

Fallbacky:
- Google SERP Search API: UNAVAILABLE (`HTTP 401 v direct probe`) -> fallback `prime RSS/web zdroje`
- Google SERP Trends Search API: UNAVAILABLE (`HTTP 401 v direct probe`) -> fallback `pytrends`
- `pytrends`: CHECKED, shortlist probehl bez noveho ranního spike u finálních kusu
- Reddit RSS: UNAVAILABLE - HTTP 403 Blocked

## LSA
- Vrstva 1: `0` cistych overnight CREATE.
- LSA dnes nema zadny cisty overnight CREATE. Nejcerstvejsi signaly jsou pre-order availability a Duo split-screen follow-up, ale ani jeden nema dost silny samostatny peg pro Vrstva 1.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a kuratorovanych follow-up signalech.

## Android Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Android Magazine dnes nema zadny cisty overnight CREATE. 9to5Google v discovery okne nedodalo novy user-facing winner a portfolio stoji na poctivem evergreen/GSC backbone.
- Vrstva 2: `21` temat. Backbone stoji na verified evergreen/GSC vrstve a kuratorovanych follow-up signalech.

## Samsung Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Samsung Magazine dnes nema zadny cisty overnight CREATE. Jediny cerstvy Samsung signal je indicka cena Galaxy S26 FE, ale bez ceskeho dopadu a s jasnym overlapem k existujici coverage.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a kuratorovanych follow-up signalech.

## Source Coverage Audit

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live API dostupne a 28denni query snapshot uspel
- GA4: CHECKED - live property snapshots prosly pro vsechny 3 weby
- Google SERP Search API: UNAVAILABLE - direct probe vratil HTTP 401; fallback = prime RSS/web zdroje
- Google SERP Trends Search API: UNAVAILABLE - direct probe vratil HTTP 401; fallback = pytrends
- Google Trends fallback (pytrends): CHECKED - iPhone 18 Pro a iPhone Duo bez noveho spike, Galaxy S26 FE bez dat
- Apple Newsroom: CHECKED - no relevant overnight signal
- 9to5Mac: CHECKED
- 9to5Google: CHECKED
- Samsung Newsroom: CHECKED - no relevant overnight signal
- GSMArena: CHECKED
- The Verge: CHECKED
- Google Blog / Workspace Updates: CHECKED - no relevant overnight signal
- Reddit RSS: UNAVAILABLE - HTTP 403 Blocked pro r/apple, r/Android i r/samsung
- GitHub: NOT CHECKED - dnes priorita sla do GSC/GA4 + Tier S RSS vrstvy

# Ranni editorial brief — 25. 9. 2026

Dnesni overnight okno: `2026-09-24 18:00 Europe/Prague -> 2026-09-25 06:07 Europe/Prague`.
Data gate prosla: `GSC PASS | GA4 PASS | Manticore PASS`.
Google SERP Search API i Google SERP Trends Search API jsou pro tenhle beh `UNAVAILABLE` (`HTTP 401`), takze search/trends vrstva jela pres `RSS + web_search + WP/Manticore cross-check + pytrends`.

## LSA

- Vrstva 1: `2` ciste overnight CREATE.
- Priority: `Apple/Qualcomm patentova dohoda` a `Apple child safety / Child Accounts push pro rodice`.
- Vrstva 2: TestFlight iOS 27, watchOS 27.2 screenshot preview, Apple Sports + utility backbone z GSC/GA4.

## Android Magazine

- Vrstva 1: `2` ciste overnight CREATE.
- Priority: `Android 17 QPR2 Beta 6 pro Pixel` a `Google Messages long-press menu s presnym kopirovanim`.
- Vrstva 2: Pixel Weather refresh, Pixel VIPs redesign, Create My Widget + silny utility backbone.

## Samsung Magazine

- Vrstva 1: `0` cistych overnight CREATE. Prioritu dnes nenafukuji.
- Nejblizsi signaly byly `One UI 9 rollout`, `Galaxy S27 memory leak` a `Galaxy Buds On`, ale vse narazi na cerstvy intent overlap s vlastni coverage.
- Vrstva 2: One UI 9 update vrstva, S27 leak, Good Lock Keys Cafe, Buds On, Find My Mobile + Samsung utility backbone.

## Source Coverage / fallbacky

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live 28denni query snapshot uspel
- GA4: CHECKED - live property snapshot uspel
- Google SERP Search API: UNAVAILABLE - provider/auth returned HTTP 401; fallback = RSS + web_search + WP/Manticore cross-check
- Google SERP Trends Search API: UNAVAILABLE - provider/auth returned HTTP 401; fallback = pytrends
- Google Trends fallback (pytrends): CHECKED - apple qualcomm probe kratce spike, ostatni CZ sample flat nebo empty
- Reddit RSS: UNAVAILABLE - r/apple, r/Android i r/samsung vratily 403 i s browser User-Agent
- Apple Newsroom: NO RELEVANT SIGNAL - RSS v overnight okne bez nove editorialne silne polozky
- Samsung Newsroom: CHECKED - official One UI 9 rollout stranka nalezena pres web search; RSS feed sam vratil 0 overnight polozek
- 9to5Mac / MacRumors / AppleInsider / 9to5Google / Android Authority / GSMArena / The Verge: CHECKED - overnight feedy prosly reality checkem
- Competitor Research: NOT CHECKED - skill/tool v tomhle behu nebyl callable
- seo-content: NOT CHECKED - skill/tool v tomhle behu nebyl callable
- humanizer: NOT CHECKED - skill/tool v tomhle behu nebyl callable

Primarni PDF vystupy jsou pripraveny jako:
- `roman-ranni-plan-lsa-20260925.pdf`
- `roman-ranni-plan-android-20260925.pdf`
- `roman-ranni-plan-samsung-20260925.pdf`

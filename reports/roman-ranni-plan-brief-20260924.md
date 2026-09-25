# Ranni editorial brief — 24. 9. 2026

Dnesni overnight okno: `2026-09-23 18:00 Europe/Prague -> 2026-09-24 06:02 Europe/Prague`.
Data gate prosla: `GSC PASS | GA4 PASS | Manticore PASS`.
Google SERP Search API i Google SERP Trends Search API jsou pro tenhle beh funkcne `UNAVAILABLE` (`code=402 No active subscription found`), takze search/trends vrstva jela pres `RSS + WP/Manticore cross-check + pytrends probe`.

## LSA

- Vrstva 1: `2` ciste overnight CREATE.
- Priority: `watchOS 27.0.1` restart bug fix na Apple Watch a `OpenAI / ChatGPT` nizka adopce uvnitr Apple Intelligence.
- Vrstva 2: Apple Podcasts video subscribers, Apple Calendar v iOS 27, HomePod Siri AI leak + utility backbone z GSC/GA4.

## Android Magazine

- Vrstva 1: `0` cistych overnight CREATE. Prioritu dnes nenafukuji.
- Nejblizsi kandidat byl Android Auto traffic-lights update, ale naráží na cerstvy intent overlap s vlastni coverage.
- Vrstva 2: Google Maps / Android Auto update, Gemini connected apps, Snapdragon Sound Elite Gen 2, Google Beam + silny utility evergreen backbone.

## Samsung Magazine

- Vrstva 1: `1` cisty overnight CREATE.
- Priority: servisni problem `Samsung smart fridges` po firmware update.
- Vrstva 2: One UI 9 US rollout a Galaxy Tab S12 leak jen jako update vrstva kvuli overlapu, plus Samsung utility backbone.

## Source Coverage / fallbacky

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live 28denni query snapshot uspel
- GA4: CHECKED - live property snapshot uspel
- Google SERP Search API: UNAVAILABLE - payload `code=402 No active subscription found`; fallback = RSS + WP/Manticore cross-check
- Google SERP Trends Search API: UNAVAILABLE - payload `code=402 No active subscription found`; fallback = pytrends
- Google Trends fallback (pytrends): CHECKED - sample dotazy probehly, ale CZ signal zustal plochy nebo prazdny
- Reddit RSS: PARTIAL - r/apple CHECKED, r/Android a r/samsung vratily HTTP 429
- Samsung Newsroom: UNAVAILABLE - feed v tomhle okne nevratil pouzitelne polozky
- 9to5Mac / MacRumors / AppleInsider / 9to5Google / Android Authority / GSMArena / Ars / The Verge: CHECKED - overnight feedy prosly reality checkem
- Competitor Research: NOT CHECKED - skill/tool v tomhle behu nebyl callable
- seo-content: NOT CHECKED - skill/tool v tomhle behu nebyl callable
- humanizer: NOT CHECKED - skill/tool v tomhle behu nebyl callable

Primarni PDF vystupy jsou pripraveny jako:
- `roman-ranni-plan-lsa-20260924.pdf`
- `roman-ranni-plan-android-20260924.pdf`
- `roman-ranni-plan-samsung-20260924.pdf`
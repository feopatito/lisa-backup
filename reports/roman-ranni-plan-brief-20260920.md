# Ranni redakcni plan V6.5 pro 20. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: dnesni `morning_context_latest.md` byl nacten a aplikovan pred pre-flightem.

Fallbacky:
- Google SERP Search API: CHECKED, ale bez uzitecneho incremental shortlist hitu -> operacne rozhodly prime RSS/web zdroje
- Google SERP Trends Search API: UNAVAILABLE (`JSON code=402 No active subscription found`) -> fallback `pytrends`
- `pytrends`: CHECKED; Apple, Android i Samsung shortlist rano bez nove akcelerace
- Reddit RSS: `r/apple` CHECKED bez silneho overnight signalu, `r/Android` a `r/samsung` UNAVAILABLE (`HTTP 429`)

## LSA
- Vrstva 1: `0` cistych overnight CREATE.
- LSA dnes nema cisty overnight CREATE. iOS 27 zrychleni, Apple Watch health gap i iPhone Duo software gamble jsou overene, ale rano jsou silnejsi jako follow-up nez jako novy solo slot.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a kuratorovanych Apple follow-upech.

## Android Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Android Magazine dnes nema cisty overnight CREATE. Gemini security test je overeny, ale je moc siroce AI a bez CZ akcelerace, takze rano zustava jen ve follow-up vrstve.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a Android utility poolech.

## Samsung Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Samsung Magazine dnes nema cisty overnight CREATE. Galaxy S27 OLED leak je zajimavy watch signal, ale bez druheho pevneho potvrzeni a bez trendove akcelerace z nej nedelam hlavni solo slot.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a Samsung utility poolech.

## Source Coverage Audit

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live 28denni query snapshot uspel
- GA4: CHECKED - live property snapshot uspel
- Google SERP Search API: CHECKED - API odpovedelo, ale shortlist neprinesl zadny uzitecny incremental organic hit nad RSS vrstvu
- Google SERP Trends Search API: UNAVAILABLE - provider vratil JSON code=402 No active subscription found; fallback = pytrends
- Google Trends fallback (pytrends): CHECKED - vsechny shortlisty rano bez nove akcelerace; One UI 9 a Galaxy S27 bez usable CZ breakoutu
- Reddit RSS: PARTIAL - r/apple CHECKED bez silneho overnight signalu, r/Android a r/samsung vratily HTTP 429
- Competitor Research: NOT CHECKED - skill/tool v tomhle behu nebyl callable
- seo-content: NOT CHECKED - skill/tool v tomhle behu nebyl callable
- humanizer: NOT CHECKED - skill/tool v tomhle behu nebyl callable
- 9to5Mac / 9to5Google / Samsung Newsroom / GSMArena / The Verge: CHECKED - overnight signaly prosly reality checkem a slozily se do follow-up vrstvy, ne do CREATE

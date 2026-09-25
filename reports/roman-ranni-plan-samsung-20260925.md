# Samsung Magazine — Ranni redakcni plan — 25. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: current for today and applied before pre-flight + portfolio selection.

Skill / fallback vrstva:
- Google SERP Search API: UNAVAILABLE -> provider/auth returned HTTP 401; fallback `RSS + web_search + WP/Manticore cross-check`
- Google SERP Trends Search API: UNAVAILABLE -> provider/auth returned HTTP 401; fallback `pytrends`
- Google Trends fallback (pytrends): CHECKED -> apple qualcomm probe kratce spike, ostatni CZ sample flat nebo empty
- Competitor Research: NOT CHECKED - skill/tool was not callable in this run
- seo-content: NOT CHECKED - skill/tool was not callable in this run
- humanizer: NOT CHECKED - skill/tool was not callable in this run

Format:
- `Vrstva 1` = jen ciste `CREATE now`
- `Vrstva 2` = evergreen / GSC backbone + kuratorovane follow-upy a weak-but-verified signaly bez umeleho nafukovani

## Vrstva 1 — Priority

- `0` cistych overnight CREATE.
- Samsung Magazine dnes nema cisty overnight CREATE. Priority vrstvu vedome nenafukuji.

## Vrstva 2 — Evergreen / GSC zakladna

### 1. One UI 9 jede ostre na Galaxy S26. Co je nove a co uz Samsung Magazine pokrylo vcera
- Action: `UPDATE`
- Proc je tady: overeny official peg, ale CREATE blokuje cerstvy intent overlap s vlastni coverage

### 2. Galaxy S27 znovu unikl v pameti a ulozisti. Co je nove a co uz web ma od vcerejska
- Action: `UPDATE`
- Proc je tady: fresh hardware leak, ale CREATE blokuje velmi cerstvy overlap s vlastnim kusem

### 3. Good Lock Keys Cafe se meni. Ctyri novinky potesi fanousky klavesnic, ale je to spis follow-up
- Action: `FOLLOW-UP`
- Proc je tady: power-user Good Lock signal s uzsim dopadem, vhodnejsi do druhe vrstvy

### 4. Galaxy Buds On ukazaly design naplno. Na hlavni slot je to ale spis follow-up nez nova bomba
- Action: `FOLLOW-UP`
- Proc je tady: signal je realny, ale CREATE blokuje overlap s vlastni coverage a dnesni traffic uz bezi na existujici URL

### 5. Ztratili jste Samsung? Find My Mobile umi vic, nez vetsina lidi vi
- Action: `UPDATE`
- Proc je tady: silny utility kus, ale ne overnight solo headline

### 6. Galaxy A18 jde do prvních hands-onů. Zatím spíš watchlist než headline
- Action: `GOOD_SIGNAL_WEAK_TODAY`
- Proc je tady: ověřený, ale slabší budget-device signál bez silného why-now

### 7. Samsung auto restart: jak ho zapnout a kdy opravdu pomůže
- Action: `UPDATE`
- Proc je tady: silný utility demand podložený GSC i GA4

### 8. Samsung se restartuje sám nebo vůbec nereaguje: co zkusit dřív než servis
- Action: `UPDATE`
- Proc je tady: silný troubleshooting evergreen

### 9. Samsung Account: co to je, k čemu slouží a jak vyřešit přihlášení
- Action: `REWRITE`
- Proc je tady: ekosystémový evergreen s jasnou utilitou

### 10. Mezipaměť v Samsungu: kdy ji smazat a kdy si tím zbytečně přiděláte práci
- Action: `REWRITE`
- Proc je tady: silný Samsung utility backbone

### 11. Jak vyfotit zatmění Slunce na Samsung: bezpečně a bez zničení snímače
- Action: `UPDATE`
- Proc je tady: sezónní evergreen se silnou užitnou hodnotou

### 12. Samsung Wallet / Pay v ČR: co funguje, co chybí a na co si dát pozor
- Action: `UPDATE`
- Proc je tady: silný search a praktický dopad

### 13. Zažloutlý kryt na mobil: co opravdu pomůže a co ho zničí
- Action: `UPDATE`
- Proc je tady: stabilní evergreen s vysokou čitelností

### 14. Zabezpečená složka Samsung: nastavení, obnova a nejčastější problémy
- Action: `UPDATE`
- Proc je tady: silný Samsung-specific evergreen

### 15. Galaxy Store: kdy má smysl a kdy je lepší zůstat v Obchodu Play
- Action: `UPDATE`
- Proc je tady: užitečný Samsung-specific backbone

### 16. SmartThings: jak nastavit chytrou domácnost Samsung bez zbytečných chyb
- Action: `UPDATE`
- Proc je tady: ekosystémový evergreen

### 17. RCS na Samsungu: jak ho zapnout, vypnout a co dělat, když zlobí
- Action: `UPDATE`
- Proc je tady: silný messaging evergreen

### 18. Stav baterie Samsung: kde ho zjistit a jak poznat, že už slábne
- Action: `UPDATE`
- Proc je tady: silný utility cluster

### 19. Bluetooth na Samsungu: párování, Dual Audio a řešení výpadků
- Action: `UPDATE`
- Proc je tady: silný evergreen s nízkou bariérou ke kliknutí

### 20. Galaxy Watch ciferníky zdarma: kde je hledat a čemu se vyhnout
- Action: `UPDATE`
- Proc je tady: silný current-demand utility follow-up

## Transparentni stav overnightu

- Samsung Magazine dnes nema cisty overnight CREATE. One UI 9 rollout, Galaxy S27 leak i Buds On narazeji na cerstvy overlap s vlastni coverage.
- Vrstva 2 stoji na overenych Samsung updatech a utility backbone vrstve; Priority dnes umyslne nenafukuji.

## Datova opora

- `GA4` snapshot: `/ja/2026/09/22/nintendo-ds-on-samsung-galaxy/` -> `15402` views
- `GA4` snapshot: `/2026/09/24/google-maps-traffic-lights-stop-signs-android-auto/` -> `7271` views
- `GA4` snapshot: `/2026/09/24/this-is-galaxy-buds-on/` -> `3892` views
- `GSC` 28 dni: `samsung` -> `180352` imp / `41227` kliku / pos `4.05`
- `GSC` 28 dni: `one ui` -> `120123` imp / `25284` kliku / pos `3.79`
- `GSC` 28 dni: `android auto` -> `119691` imp / `14986` kliku / pos `5.49`

## Tier S / overnight signaly

- 2026-09-24 evening: Samsung Newsroom confirms official One UI 9 rollout for Galaxy S26 series
- 2026-09-24 afternoon: SamMobile details Galaxy S27 memory/storage leak with possible UFS 5.1
- 2026-09-24 night: Good Lock Keys Cafe 1.9.0.6 brings four changes on One UI 9 devices
- 2026-09-24 evening: SamMobile posts fresh Galaxy Buds On design leak after FCC step
- 2026-09-24 afternoon: SamMobile refreshes practical Find My Mobile explainer

## Source Coverage Audit

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

# Ranní redakční plán V6.5 pro 29. 8. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS  
Editorial Gate: PASS  
Fallbacky: `JUST_SERP_API_KEY` v session chybí -> Search přes live RSS + Google News RSS, Trends přes `pytrends`, Samsung Newsroom bez relevantního dnešního pegu, Reddit Samsung RSS 429.

Dnes je to slabší ráno a nepřifukuji to. Po duplicate, intent overlap a reality checku mají méně než 5 čistých `CREATE` všechny tři weby:
- LSA: 2
- Android Magazine: 2
- Samsung Magazine: 0

## Vrstva 1 — Priority
Jen silné nové `CREATE` sloty k napsání teď.

### 1. LSA | Apple Photos v iOS 27
- Proč teď: 9to5Mac publikovalo nový detail 28. 8. ve 21:26 CEST a v Google News se rozjel navazující cluster.
- Proč beru: čistý utility angle pro iPhone uživatele, bez overlapu v Manticore.
- Evidence: 9to5Mac: `Apple Photos in iOS 27 upgrades one of my favorite features in a big way`
- Titulek 1 (Discover) [DOPORUČENO]: Fotky v iOS 27 dostanou změnu, kterou budete používat pořád. Apple vylepšuje jednu z nejpraktičtějších funkcí
- Titulek 2 (Search): Apple Photos v iOS 27 vylepšují jednu z nejužitečnějších funkcí aplikace Fotky
- Titulek 3 (Balanced): Aplikace Fotky v iOS 27 mění drobnost, která vám ve výsledku ušetří čas
- Proč doporučený: prodává konkrétní užitek místo interního názvu funkce.

### 2. LSA | ChatGPT a Codex umí více Google účtů
- Proč teď: 9to5Mac publikovalo 28. 8. ve 20:01 CEST workflow novinku bez stejného intentu na LSA.
- Proč beru: silný Apple-user angle pro iPhone/Mac workflow mezi osobním a pracovním účtem.
- Evidence: 9to5Mac: `ChatGPT and Codex now support multiple Gmail and Google Calendar accounts`
- Titulek 1 (Discover) [DOPORUČENO]: ChatGPT a Codex konečně zvládnou víc Gmailů i kalendářů najednou. Na iPhonu a Macu to řeší otravný problém
- Titulek 2 (Search): ChatGPT a Codex nově podporují více Gmail a Google Calendar účtů
- Titulek 3 (Balanced): Používáte víc pracovních účtů? ChatGPT a Codex teď umí to, co dlouho chybělo
- Proč doporučený: hned ukazuje praktický problém, který novinka řeší.

### 3. Android Magazine | Android 17 QPR2 Beta 4
- Proč teď: rollout i soupis novinek spadly mezi 23:53 a 01:10 CEST přímo do ranního okna.
- Proč beru: čerstvý systémový update s jasným Pixel publikem a bez stejného článku na webu.
- Evidence: 9to5Google: `Android 17 QPR2 Beta 4 rolling out with many Pixel bug fixes` + `Here’s everything new in Android 17 QPR2 Beta 4`
- Titulek 1 (Discover) [DOPORUČENO]: Android 17 QPR2 Beta 4 je venku. Tohle jsou změny, které mají pro Pixel uživatele smysl už dnes
- Titulek 2 (Search): Android 17 QPR2 Beta 4 přináší nové funkce i opravy chyb pro Pixely
- Titulek 3 (Balanced): Nová beta Androidu 17 dorazila na Pixely. Co v ní stojí za pozornost a co ne
- Proč doporučený: spojuje čerstvost s praktickým filtrem pro reálné uživatele.

### 4. Android Magazine | Gemini Notebook mění usage limity
- Proč teď: oficiální Google Blog vyšel 28. 8. v 19:00 CEST a následně se rozjela sekundární coverage.
- Proč beru: potvrzená produktová změna s dopadem na používání, ne jen spekulace.
- Evidence: Google Blog: `We’re introducing flexible usage limits for Gemini Notebook.`
- Titulek 1 (Discover) [DOPORUČENO]: Gemini Notebook mění limity používání. Google přestává počítat den po staru a zavádí nový model
- Titulek 2 (Search): Google zavádí flexibilní usage limity pro Gemini Notebook
- Titulek 3 (Balanced): V Gemini Notebooku se mění pravidla používání. Co nový limit znamená v praxi
- Proč doporučený: bez korporátního slovníku rychle vysvětluje, že se mění pravidla používání.

## Vrstva 2 — Inspirace a updaty
Kurátorovaný doplněk, ne odpad po vrstvě 1.

### LSA
- Steve Jobs školní projekt prodaný v aukci | `GOOD_SIGNAL_WEAK_TODAY` | follow-up: nový je výsledek aukce, ale základ tématu už na webu existuje
- Apple TV+ / Apple One zdražení | `GOOD_SIGNAL_WEAK_TODAY` | slabší dnešní signál: čerstvé, ale zatím převážně US-only bez jasného CZ angle
- Apple Watch Ultra 4 rozdíly | `WAIT_FOR_PEG` | čekání na peg: stejná potřeba čtenáře už je na LSA pokrytá

### Android Magazine
- Play Books v Gemini Notebooku přes Expert Intelligence | `GOOD_SIGNAL_WEAK_TODAY` | discovery kus, ale hlavní peg padl už před dnešním oknem
- Dreambeans zdarma k testu | `GOOD_SIGNAL_WEAK_TODAY` | follow-up: nový je free-test peg, ale produktový intent už web řešil
- Google Health 5.07 logging + maps | `GOOD_SIGNAL_WEAK_TODAY` | užitečné, ale bez pevnějšího first-party pegu
- Gboard 18.x na APKMirror | `WAIT_FOR_PEG` | release samotný nestačí bez teardownu nebo potvrzené novinky

### Samsung Magazine
- Galaxy S26 FE launch/review vlna | `WAIT_FOR_PEG` | coverage běží, ale chybí nový lokální nebo datový posun
- Galaxy A35 a možná One UI 9 beta | `WAIT_FOR_PEG` | bez oficiálního potvrzení zůstává jen monitor
- Galaxy Tab S9 srpnový update | `GOOD_SIGNAL_WEAK_TODAY` | vhodnější do širšího roundup formátu než do solo slotu

## Source Coverage Audit
- WordPress/Manticore: CHECKED
- GSC: CHECKED live
- GA4: CHECKED live
- AdSense: NOT CHECKED - secondary signal, v tomto běhu nepoužit
- Google Trends: CHECKED via `pytrends` fallback
- Google News: CHECKED via RSS search
- Major tech media: CHECKED (`9to5Mac`, `9to5Google`, `GSMArena`, `Android Headlines`, `SamMobile`)
- Official newsrooms: Apple Newsroom CHECKED / NO RELEVANT SIGNAL, Samsung Newsroom CHECKED / NO RELEVANT SIGNAL, Google Blog CHECKED
- Product pages: NOT CHECKED - bez silnějšího dnešního pegu
- Support docs: NOT CHECKED - žádný priority peg je dnes neotevřel
- Developer docs: CHECKED light - bez consumer-ready tématu
- Changelogs: NOT CHECKED - bez samostatného consumer delta
- GitHub: CHECKED - bez consumer-ready signálu
- Beta programs: CHECKED
- APK changes: CHECKED
- Regulatory/certification: NO RELEVANT SIGNAL
- Reddit: `r/apple` CHECKED, `r/Android` CHECKED / NO RELEVANT SIGNAL, `r/samsung` UNAVAILABLE (429)
- Developer forums: NOT CHECKED - nižší priorita než silnější zdroje
- X/leakers: CHECKED přes Gurman Google News fallback, bez nového silného pegu
- YouTube: NOT CHECKED - bez lepšího pegu než textové zdroje
- Smaller specialist media: CHECKED

Bez explicitního schválení Romana nebo Toma nic nezapisuji na WordPress.

Je to pro vás vyhovující?

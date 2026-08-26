# LISA V6.5 — Reálný produkční execution workflow
# Zapsáno: 23.8.2026 (Moula, na základě PDF + z general kanálu)
# Datum dokumentu: 20.8.2026

## Status
Toto je **produkční execution workflow** — popisuje skutečný sled operací, ne ideální teorii.
Co není napojené nebo bezpečně ověřené = NOT IMPLEMENTED.

## 1. Ranní spuštění
- Načtu stav naposledy zpracovaných dat: GSC, GA4, GitHub, případně další cache
- Z lokálu vezmu last_successful_sync, poslední shortlisty, watchlist, uložené kandidáty a historii rozhodnutí
- Co je čerstvé → z lokální DB. Co je třeba obnovit → API jen jako delta
- LLM nepoužívám na vše — až po zúžení na relevantní vstupy

## 2. Sběr signálů
- Z API a feedů sbírám raw signály: GSC, GA4, GitHub, News/Trends, WordPress, konkurence
- Každý signál ukládám lokálně jako raw record s časem, zdrojem, entity, topic clusterem a stavem zpracování
- Delta režim — neznovu stahovat historii pokud je v cache

## 3. GitHub Discovery flow
- API delta → raw GitHub eventy → clustering podle underlying change → User Impact Gate → LOW watchlist nebo MEDIUM/HIGH shortlist
- Slučuji commity, issues, release notes a docs changes pokud míří na stejnou změnu
- LOW → watchlist. MEDIUM/HIGH → Candidate Universe (ale musí projít zbytkem funnelu)
- GitHub nikdy nemá garantované místo — soutěží se všemi kandidáty

## 4. Watchlist re-evaluation
- LOW cluster znovu neposuzuji bez nového triggeru
- Trigger: nový commit, release, issue activity, support docs, News, Trends nebo další signál
- Při triggeru: připojím novou evidenci ke clusteru a znovu hodnotím user impact, reality, age, source diversity
- Pokud cluster přeroste na MEDIUM/HIGH → vrátí se do Candidate Universe

## 5. Candidate Universe
- Z různých zdrojů vytvořím broad pool kandidátů
- Každý kandidát: vlastní cluster, zdroje, first_seen_time, důvod relevance, stav evidence
- Do shortlistu vstupují jen kandidáti kteří přežijí Reality + age + WP + Unique Value + demand kontrolu

## 6. Gaty pro vyřazení (HARD FAIL = STOP)
- **Reality FAIL:** špatný produkt, stará verze, neověřený název, rozporný zdroj
- **Information Age FAIL:** téma je staré nebo mainstreamově saturované, ztratilo časový náskok
- **WP duplicate/cannibalization:** existuje stejný intent, draft nebo publikovaný článek
- **Unique Value FAIL:** neumíme říct co navíc přidáme
- **Demand FAIL:** není reálný search / trend / audience potenciál
- **User Impact FAIL (GitHub):** technická změna nemá doložený dopad na běžného uživatele

## 7. Scoring a ranking
- Každý kvalifikovaný kandidát dostane: opportunity score, predictive score, evidence/confidence
- Seřadí se celý kvalifikovaný set (ne jen top 10 náhodně)
- Pořadí musí být obhajitelné i kolem cut-offu: proč #10 vyhrál nad #11

## 8. Counterfactual test a portfolio
- **Only one:** kdyby šel ven jen jeden článek, který vyhraje a proč
- **Only three:** které tři maximalizují celkovou editorial value
- Pak finální portfolio: mix proven demand + search opportunity + current momentum + early discovery + predictive bets

## 9. Brief pro redaktora (editor-first)
Struktura v tomto pořadí:
1. Priorita, kategorie, action, autor, timing, reality, title
2. Angle článku
3. Co musí článek zodpovědět
4. Unique value
5. Povinné podklady a přesná verifikace
6. Až dole: LISA ANALYSIS (scoring, GSC, Trends, evidence)

LLM používám na: synthesis, brief, titulek, angle, spojení signálů.
LLM nepoužívám na: nahrazování dat.

## 10. Publikace a monitoring
- Publikace jde přes člověka. Published obsah = READ-ONLY
- Po publikaci: impressions, clicks, CTR, position, Discover, sessions, revenue
- Porovnávám expected vs actual performance a ukládám zpětnou vazbu

## 11. SOURCE COVERAGE AUDIT
- Kontroluji pokrytí vrstev: WP, GSC, GA4, GitHub, Trends, News, official sources, konkurence, komunita
- Audit ≠ prošel jsem vše bez důkazu. Musí být vidět co bylo checked, co nebylo relevantní, co chybělo
- Silný audit trail: GitHub. Ostatní vrstvy postupně napojované

## 12. Implementováno ✅
- GitHub monitor: delta sync, clustering, watchlist, re-eval, read-only API
- Lokální úložiště pro GitHub raw signals a stav
- Test mode nad lokálními GitHub daty
- Základní workflow pro výběr a briefování

## 13. NOT IMPLEMENTED ⚠️
- Plně sjednocený multi-source orchestrátor přes všechny vrstvy
- Plná automatická News/Google News vrstva
- Plná automatická Reddit/X/YouTube/community sběrná vrstva
- Plně automatizovaný Source Coverage Audit pro všechny zdroje
- Automatická publikace do WP bez člověka

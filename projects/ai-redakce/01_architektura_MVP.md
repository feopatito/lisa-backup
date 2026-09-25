# AI REDAKCE: ARCHITEKTURA A MVP
*Lokální AI šéfredaktor, specializovaní agenti, WordPress a postupný přechod k autonomnímu provozu*

## 1. Cíl projektu
Vybudovat lokálně provozovatelnou AI redakci — řízený redakční systém, ne jen generátor textu.
- Začít na Macu jako MVP, zachovat možnost přesunu na server
- Nejdřív publikovat do WordPressu jako Draft/Pending; autopublikaci zapínat postupně
- AI hlavně na rychlé zpravodajství, novinky, úniky, aktualizace, rutinní obsah
- Lidé: recenze, testy, názory, rozhovory, vlastní zkušenost

## 2. Organizační model AI redakce
- **AI šéfredaktor** — priority, plán, zadávání práce, finální rozhodnutí
- **Research agent** — monitoring RSS, webů, tiskových center, sociálních sítí
- **Datový analytik** — vyhodnocení historického výkonu témat a článků
- **SEO/content stratég** — příležitosti, kanibalizace, aktualizace, obsahové mezery
- **Redaktor** — tvorba textu ve stylu konkrétního magazínu
- **Editor** — struktura, jazyk, srozumitelnost, konzistence
- **Fact-checker** — ověření tvrzení proti důvěryhodným zdrojům
- **Linking agent** — interní a relevantní externí odkazy
- **Publisher** — WordPress REST API, média, metadata, draft/publish
- **Quality gate** — poslední kontrola před publikací

## 3. Běžný den
1. Sběr zdrojů a trendů
2. Deduplikace a scoring
3. Kontrola vlastního archivu
4. Prioritizace témat
5. Research
6. Návrh titulku a úhlu
7. Sepsání
8. Fact-check, SEO a linking
9. Schválení
10. WordPress
11. Zpětné měření výkonu

## 4. Technologický základ
- **Python** — hlavní aplikační vrstva
- **LangGraph** — orchestrace agentů, stav workflow
- **Ollama** — lokální provoz open-source modelů na Macu
- **Qdrant** — vektorové vyhledávání v archivu
- **PostgreSQL** — články, úkoly, zdroje, stav workflow, metriky
- **Redis** — asynchronní úlohy a plánování
- **WordPress REST API** — drafty, aktualizace, publikace
- **LLM API** — cloud model pro náročné úlohy

## 5. Lokální vs. cloudové modely
- Lokálně: třídění, sumarizace, deduplikace — nízké náklady
- Cloud API: research, plánování, finální text — vyšší kvalita
- Každý článek eviduje vlastní náklady

## 6. Znalostní báze a archiv
- Metadata: magazín, autor, datum, kategorie, téma, produkt, typ, URL
- Výkon: impressions, clicks, CTR, pozice, návštěvnost, výnos
- Systém rozhoduje: nový článek / aktualizace / nepokrývat

## 7. WordPress a schvalovací režimy
- **Režim A**: AI navrhne v interním rozhraní
- **Režim B**: AI vytvoří Draft/Pending, člověk publikuje
- **Režim C**: nízkorizikové šablony automaticky
- **Režim D**: širší autopilot po prokázání kvality

## 11. MVP plán
- **Fáze 1**: jeden magazín, archiv, desítky zdrojů, denní briefing, WordPress Draft
- **Fáze 2**: Search Console/Analytics, SEO a linking agent, měření nákladů
- **Fáze 3**: více magazínů, sociální zdroje, automatické plánování
- **Fáze 4**: průběžné učení z výsledků, ekonomická optimalizace

## Doporučený první krok
Malé lokální MVP na jednom magazínu: denní monitoring → redakční plán → jeden článek → kontroly → WordPress Draft.

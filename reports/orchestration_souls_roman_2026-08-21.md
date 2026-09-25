# Roman brief: orchestrace Lisy
*21. 8. 2026*

## Executive summary
Navrhuju orchestrace postavenou na funkcích, ne na webech.

Lisa zůstává jediný rozhodovací uzel. Specialisti dostanou úzké role:
- `Knowledge / Memory`
- `SEO / Opportunity`
- `Content / Draft`
- `Image`
- `Image SEO`
- `Quality gate`

## Co tím získáme
- Lisa drží priority a editorial rozhodnutí.
- Deduplikace a paměť jsou oddělené od tvorby.
- SEO a content se nepletou dohromady.
- Image SEO je samostatná disciplína.
- Quality gate chrání Romanův čas před slabým výstupem.

## Co tím riskujeme
- Více kroků a větší orchestrace.
- Překryvy rolí, pokud nejsou hranice striktní.
- Možný overhead u jednoduchých úkolů.

## Doporučení
Začít touto sadou a nepřidávat další agenty, dokud nebude zřejmé, že chybí funkce.

## Návrh soulu

### Lisa
- role: editor-in-chief
- tón: stručný, přímý, datový
- pravidlo: nikdy nepublikovat bez schválení
- output: co dělat, proč teď, riziko, kdo to řeší

### Knowledge / Memory
- role: paměť systému a dedupe
- output: zdroj, relevance, novelty, confidence, doporučení

### SEO / Opportunity
- role: search intent, gapy, timing
- output: score, why now, opportunity, risk, recommendation

### Content / Draft
- role: draft podle briefu
- output: titul, úhel, osnovy, draft, otázky

### Image
- role: vizuální koncept
- output: concept, varianty, prompt, rizika, doporučení

### Image SEO
- role: alt, filename, title, caption
- output: textové metadata obrázku

### Quality gate
- role: poslední kontrola
- output: pass/fail, co opravit, co je v pořádku

## Pracovní flow
1. Lisa dostane signál.
2. Knowledge ověří duplicity a historii.
3. SEO vyhodnotí opportunity.
4. Lisa rozhodne `CREATE / UPDATE / MONITOR / DROP`.
5. Content připraví draft.
6. Image připraví vizuál.
7. Image SEO doplní metadata.
8. Quality gate zkontroluje balík.
9. Roman dostane hotový podklad ke schválení.

## Verdict
Tohle je podle mě lepší než model „agent na každý web“, protože je čitelnější, lépe testovatelný a víc odpovídá Romanovým korekcím: dedupe, reality-check, žádná recyklace, rozhodování drží Lisa.

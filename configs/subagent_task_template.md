# Subagent Task Brief Template
# POVINNÉ použít při každém sessions_spawn

## HARD RULES PRO SUBAGENTY (nesmí být vynechány)

### ❌ CO SUBAGENT NESMÍ
- Volat Manticore API (nezdědí credentials)
- Volat GA4 / GSC API (nezdědí service account)
- Volat WP REST API s autentizací
- Prezentovat AI odhady jako reálná data
- Posílat výstup Romanovi přímo

### ✅ CO SUBAGENT SMÍVÁ
- Analyzovat text, kategorizovat, scorovat
- Psát drafty a briefs
- Vyhledávat weby (web_search, web_fetch)
- Číst lokální soubory
- Zpracovávat PDF/CSV data

### TEMPLATE PRO TASK BRIEF:
```
## SUBAGENT TASK: [název]

SCOPE: [co má udělat]
OUTPUT: [formát výstupu]

### ZAKÁZÁNO:
- Žádné API calls s credentials (Manticore, GA4, GSC, WP auth)
- Žádné odhady prezentované jako data ze Search Console / GA4
- Žádné přímé zprávy Romanovi

### DATA KTERÁ DOSTANEŠ (z parentu):
[explicitně předat data která subagent potřebuje]

### OUTPUT FORMAT:
[přesný formát — musí odpovídat Samsung standardu pokud jde o GSC data]
```

## DATA SOURCE TAGGING (povinné v každém reportu)

Každé číslo musí mít tag:
- `[GSC]` — z Google Search Console API
- `[GA4]` — z Google Analytics 4 API  
- `[Manticore]` — z Manticore Search
- `[AI-odhad]` — ‼️ AI estimate, NENÍ ověřeno — ČERVENĚ označit

Pravidlo: AI-odhad v reportu = STOP. Buď dát reálná data nebo prázdné pole.

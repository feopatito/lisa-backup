# DIAGNOSTIC REPORT — 24.8.2026 08:00 Morning Cycle

## SHRNUTÍ PROBLÉMŮ

Ranní cycle (6:00–8:00) běžel, ale report nebyl kompletní. **2 kritické absence přístupu:**

---

## PROBLÉM #1: GSC (Google Search Console) — 403 Forbidden

### Co se stalo
Service account `android-magazine@android-magazine-505315.iam.gserviceaccount.com` **NEMÁ oprávnění** pro 2 ze 3 weby.

### Konkrétní chyby v morning-sync-2026-08-24.json:

```json
"letemsvetemapplem.eu": {
  "status": "ERROR: <HttpError 403: User does not have sufficient permission for site 'sc-domain:letemsvetemapplem.eu'>"
}

"samsungmagazine.eu": {
  "status": "ERROR: <HttpError 403: User does not have sufficient permission for site 'sc-domain:samsungmagazine.eu'>"
}
```

### Příčina
V Google Search Console nejsou přidáni správní uživatelé/service accounty pro:
- **letemsvetemapplem.eu** — service account nemá přístup
- **samsungmagazine.eu** — service account nemá přístup

Service account **JE validní a má správné scopes** (`webmasters.readonly`), ale:
- Není přidán do GSC property pro LSA
- Není přidán do GSC property pro Samsung Magazine

### Dopad
Lisa **nemůže číst data z Search Console** pro 2 weby:
- ❌ Keyword analysis (top queries, pozice, CTR)
- ❌ Page performance (impressions, clicks)
- ❌ Search intent data

**Jen Android Magazine GSC funguje** (✅).

### Řešení (CO MUSÍ DĚLAT ROMAN/ERIK)
V **Google Search Console** (`search.google.com/search-console`):

1. **Pro letemsvetemapplem.eu:**
   - Settings → Users and permissions
   - Add user: `android-magazine@android-magazine-505315.iam.gserviceaccount.com`
   - Role: **Editor** (nebo minimálně **Viewer**)
   - Save

2. **Pro samsungmagazine.eu:**
   - Settings → Users and permissions
   - Add user: `android-magazine@android-magazine-505315.iam.gserviceaccount.com`
   - Role: **Editor** (nebo minimálně **Viewer**)
   - Save

**Pokud to dodají dnes:** Lisa znovu spustí morning cycle a GSC data budou OK.

---

## PROBLÉM #2: Service Account JSON soubor — Missing on Lisa's Mac

### Co se stalo
File `android-magazine-sa.json` **fyzicky neexistuje** na lisa-macbookpro.

### Příčina
Při včerejším přenastavení workspacu (19.8 git commit) se JSON soubor **ztratil**. Důvod:
- Soubor **nebyl v Git repo** (správně — credentials se do gitu nedávají)
- Záloha na Mac mini **neexistuje** (Moula ji neměl)
- Originál soubor byl jen na Lisině MacBooku a **smazal se**

### Dopad
Lisa **nemůže se ověřit k Google Cloud** (ani pro GA4, ani pro GSC). Bez JSON souboru s private key:
- ❌ Nelze vytvořit service account credentials
- ❌ GA4 API — NE (bez auth)
- ❌ GSC API — NE (bez auth)

### Aktuální stav
V `~/.openclaw/creds/` na lisa-macbookpro **nejsou**:
- `android-magazine-sa.json` ❌
- Žádný Google SA JSON ❌

**Co máme:**
- `github-roman-token.txt` ✅
- `google-drive-credentials.json` ✅ (ale to je Google Drive SA, ne GA4/GSC)

### Řešení (CO MUSÍ DĚLAT ERIK/TOM)

**Varianta A — Vygenerovat nový JSON klíč (DOPORUČENO):**
1. Erik jde na `console.cloud.google.com`
2. Projekt: `android-magazine-505315`
3. IAM & Admin → Service Accounts
4. `android-magazine@android-magazine-505315.iam.gserviceaccount.com` → Keys
5. Add Key → Create new key → **JSON**
6. Pošle soubor Tomovi (nebo přímo Lisě)
7. Tom nahraje SSH na Lisin Mac:
   ```bash
   scp android-magazine-sa.json lisa@192.168.0.115:~/.openclaw/creds/
   ```

**Varianta B — Pokud máte starší kopii:**
1. Tom stáhne `android-magazine-sa.json` z bezpečné zálohy
2. Nahraje SSH na Lisin Mac (viz výše)

**Čas na zprovoznění:** ~2 minuty

---

## SHRNUTÍ PRO ROMANA

| Problém | Příčina | Řešení | Kdo | Čas |
|---------|---------|--------|-----|-----|
| **GSC 403 LSA + Samsung** | Service account není v GSC property | Erik přidá SA do GSC (Settings → Users) | Erik | 5 min |
| **GSC/GA4 auth fail** | JSON soubor chybí na Lisině Mac | Erik vygeneruje nový JSON, Tom nahraje SSH | Erik + Tom | 10 min |

---

## PŘÍŠTÍ PREVENTIVNÍ OPATŘENÍ

1. **SA JSON záloha:** Moula si vždy bude zálohovat `android-magazine-sa.json` na Mac mini (bezpečně, ne do gitu)
2. **GSC service account access audit:** Během nastavení musím ověřit že SA má přístup ke všem 3 GSC properties
3. **Periodic access check:** 1× měsíčně Lisa testuje GA4 + GSC auth pro všechny 3 weby

---

## VÝKON RANNÍHO CYCLU (Z DAT CO MÁME)

✅ **Co fungovalo:**
- GA4 data: OK pro všechny 3 weby (17K + 527K + 535K sessions)
- GitHub delta: OK (1 cluster, LOW impact — Samsung Tizen docs)
- WordPress cache: OK (čte se lokálně)

❌ **Co selhalo:**
- GSC (Google Search Console): 2/3 weby — 403 Forbidden
- Editorial output do #redakční-plán: **NEBYL ODESLÁN** (chybí GSC data pro úplný ranking)

---

## EDITORSKÁ KVALITA REPORTU

Bez GSC data pro 2 weby **nelze:**
- Přiřadit SEO skóre kandidátům (GSC 20% váhy)
- Identifikovat ranking opportunities (pozice 5–20, nízké CTR)
- Dělat demand analysis přesně

**Řešení:** Jakmile budou GSC přístupy OK, spustíme ranní cycle znova (během 2 hodin).

---

**Status:** Čeká se na Erik + Tom
**Deadline:** Dnes před 18:00 aby se cycle mohl spustit zítra ráno

# 📦 Dávkovací plán — 20 000+ obrázků Android Magazine
**Datum:** 2026-08-23  
**Cíl:** Procesovat 29 370 médií bez memory leak / disk overflow  
**Hardware:** Vašek M2 Pro, 32 GB RAM, SSD  
**Strategie:** Po 1 000 obrázků s memory cleanup

---

## 📊 Rozpis dávek

| Dávka | ID obrázku | Počet | Odhadový čas | Cílový den |
|-------|-----------|-------|--------------|-----------|
| **Pilot** | 1–100 | 100 | 20–40 min | 23.8. (dnes) |
| **Várka 1** | 101–1,100 | 1 000 | 4–8 hodin | 23.8.–24.8. |
| **Várka 2** | 1,101–2,100 | 1 000 | 4–8 hodin | 24.8. |
| **Várka 3** | 2,101–3,100 | 1 000 | 4–8 hodin | 24.8. |
| **Várka 4** | 3,101–4,100 | 1 000 | 4–8 hodin | 24.8.–25.8. |
| **Várka 5** | 4,101–5,100 | 1 000 | 4–8 hodin | 25.8. |
| ... | ... | ... | ... | ... |
| **Várka 29** | 28,101–29,100 | 1 000 | 4–8 hodin | 27.8. |
| **Zbytek** | 29,101–29,370 | 270 | ~1 hod | 27.8. |

---

## 🧠 Memory Management

**Před každou dávkou:**
```bash
# Vyprázdnit cache
rm -rf ~/.cache/ollama/*
sync; sleep 2
```

**Během běhu:**
- Vision model (llama/llava): ~8 GB RAM max
- Text model (qwen2.5): ~6 GB RAM max
- Free RAM při spuštění: min 15 GB ✅

**Po dávce:**
```bash
# Unload modely z paměti
curl -X POST http://localhost:11434/api/generate -d '{"model":"","stream":false}'
sleep 5
```

---

## 💾 Disk Space

**Požadavky:**
- Cache pro modely: ~15 GB (součást `/Library/Application Support/Ollama`)
- Workspace output: ~100 MB per dávku (CSV + JSON reports)
- **Volný disk potřeba:** min 50 GB (safety margin)

**Monitorování:**
```bash
df -h | grep -E "^/dev|^Filesystem"
du -sh ~/.openclaw/workspace/batch-outputs/
```

---

## 📋 Workflow per dávka

```
1. LOAD: Vlož prvních N obrázků z WP API (media endpoint)
2. VISION: llava/llama3.2-vision — popis + uncertainty flag
3. TEXT: qwen2.5 — alt-text + keywords + SEO name
4. DEDUPE: Porovnání s předchozími výstupy (memory dedupe)
5. TAG: [GENERIC] / [UNCERTAIN] / [CONFIDENT]
6. EXPORT: CSV + JSON → ~/batch-outputs/batch-001.csv
7. CLEANUP: Unload modely, vyčisti paměť
8. VERIFY: Spot-check 10 výstupů (Lisa ručně)
9. COMMIT: Push CSV na GitHub
10. WAIT: Approval před další dávkou
```

---

## ⏱️ Timeline (optimista + pesimista)

| Scénář | Trvání | Hotovo |
|--------|--------|--------|
| **Ideální** (4h/dávka, 24/7 běh) | 4 dny | 27.8. |
| **Realistický** (5h/dávka, daytime) | 5–6 dní | 28.–29.8. |
| **Pesimistický** (8h/dávka, debug) | 7–8 dní | 30.–31.8. |

---

## 🚨 Fail-safes

- **Memory spike?** → Dávku rozdělit na 500
- **Disk plný?** → Cleanup batch outputs, push na GitHub
- **Model crash?** → Restart Ollama, rerun od posledního checkpoint
- **Vision model vyhazuje errors?** → Switch na alternativní (llava vs. llama3.2-vision)

---

## ✅ Schválení & Go/No-Go

| Fáze | Approval | Status |
|------|----------|--------|
| Pilot (100) | Lisa + Tom | ⏳ Čekám |
| Várka 1 (1k) | Roman (SEO review) | ⏳ Čekám |
| Batch 2–29 | Lisa auto-approve | ⏳ Pending |

---

**Připraveno pro Moulu + Romana k review!**

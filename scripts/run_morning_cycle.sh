#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="/Users/lisa/.openclaw/workspace"
LOG_DIR="$WORKSPACE/logs"
LOG_DATE="$(date '+%Y-%m-%d')"
REPORT_DATE="$(date '+%Y%m%d')"
LOG="$LOG_DIR/morning-cycle-$LOG_DATE.log"
LATEST_LOG="$LOG_DIR/morning-cycle.log"
PYTHON_BIN="$WORKSPACE/scripts/lisa_python.sh"
PDF_RENDERER="$WORKSPACE/scripts/render_morning_plan_pdf.py"
CONTEXT_LATEST="$WORKSPACE/cache/morning_context_latest.md"
CHANNEL_REDAKCNI_PLAN="1541026445764198470"
CHANNEL_AI_NASTAVENI="1540072798062514186"
CRON_JOB_ID="3e868729-1086-4517-87b9-0619b33c0a02"
CRON_WAIT_TIMEOUT="${LISA_CRON_WAIT_TIMEOUT:-20m}"

mkdir -p "$LOG_DIR" "$WORKSPACE/cache"
cd "$WORKSPACE"
ln -sf "$LOG" "$LATEST_LOG"

timestamp() {
  date '+%Y-%m-%d %H:%M:%S'
}

log_line() {
  echo "[$(timestamp)] $*" >> "$LOG"
}

discord_token() {
  cat ~/.openclaw/openclaw.json | "$PYTHON_BIN" -c "import json,sys; d=json.load(sys.stdin); print(d.get('channels',{}).get('discord',{}).get('token',''))" 2>/dev/null
}

send_discord() {
  local channel_id="$1"
  local message="$2"
  local token
  if [[ "${LISA_SKIP_DISCORD:-0}" == "1" ]]; then
    log_line "DISCORD SKIPPED channel=$channel_id message=$message"
    return 0
  fi
  token="$(discord_token)"
  if [[ -z "$token" ]]; then
    log_line "WARN: Discord token missing, could not send to $channel_id"
    return 1
  fi
  local payload
  payload="$("$PYTHON_BIN" -c 'import json,sys; print(json.dumps({"content": sys.stdin.read()}))' <<<"$message")"
  curl -s -X POST \
    -H "Authorization: Bot $token" \
    -H "Content-Type: application/json" \
    -d "$payload" \
    "https://discord.com/api/v10/channels/$channel_id/messages" > /dev/null || return 1
}

summarize_failure() {
  local text="$1"
  local summary
  summary="$(printf '%s\n' "$text" | rg 'FAIL|ERROR|STOP|Traceback' -m 3 || true)"
  if [[ -z "$summary" ]]; then
    summary="$(printf '%s' "$text" | tail -c 300)"
  fi
  printf '%s' "$summary"
}

file_has_today_mtime() {
  local path="$1"
  [[ -f "$path" && "$(date -r "$path" '+%Y-%m-%d')" == "$LOG_DATE" ]]
}

alert_ai() {
  local title="$1"
  local details="$2"
  local body="$title"$'\n\n'"$(summarize_failure "$details")"
  send_discord "$CHANNEL_AI_NASTAVENI" "$body" || log_line "WARN: ai_nastaveni alert failed"
}

generate_morning_pdfs() {
  local report_dir="$WORKSPACE/reports"
  local report_key
  local md_path
  local pdf_path
  local title
  local subtitle
  local meta
  local rendered=0
  local warnings=()

  if [[ ! -x "$PDF_RENDERER" ]]; then
    log_line "WARN: PDF renderer missing or not executable: $PDF_RENDERER"
    alert_ai "⚠️ Morning PDF WARNING — renderer chybí" "$PDF_RENDERER"
    return 1
  fi

  for report_key in lsa android samsung; do
    md_path="$report_dir/roman-ranni-plan-$report_key-$REPORT_DATE.md"
    pdf_path="$report_dir/roman-ranni-plan-$report_key-$REPORT_DATE.pdf"

    case "$report_key" in
      lsa)
        title="LSA — Ranní redakční plán $(date '+%-d.%-m.%Y')"
        subtitle="letemsvetemapplem.eu  |  Apple + Tech  |  live overnight + evergreen pool"
        ;;
      android)
        title="Android Magazine — Ranní redakční plán $(date '+%-d.%-m.%Y')"
        subtitle="androidmagazine.eu  |  Android + Google + Pixel  |  live overnight + evergreen pool"
        ;;
      samsung)
        title="Samsung Magazine — Ranní redakční plán $(date '+%-d.%-m.%Y')"
        subtitle="samsungmagazine.eu  |  Samsung + One UI + Galaxy  |  live overnight + evergreen pool"
        ;;
    esac

    meta="Lisa morning cycle  •  $LOG_DATE  •  Text Factory  •  primární PDF výstup"

    if [[ -f "$md_path" ]]; then
      if "$PDF_RENDERER" \
        --input "$md_path" \
        --output "$pdf_path" \
        --title "$title" \
        --subtitle "$subtitle" \
        --meta "$meta" \
        --date "$REPORT_DATE" >> "$LOG" 2>&1; then
        rendered=$((rendered + 1))
        log_line "PDF rendered: $pdf_path"
      else
        warnings+=("$report_key: render failed")
      fi
    elif file_has_today_mtime "$pdf_path"; then
      rendered=$((rendered + 1))
      log_line "PDF already present: $pdf_path"
    else
      warnings+=("$report_key: markdown missing")
    fi
  done

  if [[ "$rendered" -eq 0 ]]; then
    alert_ai "⚠️ Morning PDF WARNING — žádný ranní PDF artefakt nevznikl" "$(printf '%s\n' "${warnings[@]}")"
    return 1
  fi

  if [[ "${#warnings[@]}" -gt 0 ]]; then
    alert_ai "⚠️ Morning PDF WARNING — část PDF artefaktů chybí" "$(printf '%s\n' "${warnings[@]}")"
  fi

  return 0
}

log_line "morning_cycle_wrapper START"
log_line "generating morning context"
context_ok=0
for attempt in 1 2; do
  if context_output="$("$PYTHON_BIN" "$WORKSPACE/scripts/morning_context.py" 2>&1)"; then
    printf '%s\n' "$context_output" >> "$LOG"
    if file_has_today_mtime "$CONTEXT_LATEST"; then
      context_ok=1
      break
    fi
    log_line "WARN: morning context attempt $attempt produced stale or missing latest file"
  else
    printf '%s\n' "$context_output" >> "$LOG"
    log_line "WARN: morning context attempt $attempt failed"
  fi
  if [[ "$attempt" -lt 2 ]]; then
    sleep 5
  fi
done

if [[ "$context_ok" -ne 1 ]]; then
  log_line "WARN: continuing without fresh morning context"
  printf '%s\n' "WARNING: morning_context_latest.md missing or stale; continuing with live data" >> "$LOG"
fi

log_line "running preflight hard gate"
if ! preflight_output="$("$PYTHON_BIN" "$WORKSPACE/scripts/preflight_check.py" 2>&1)"; then
  printf '%s\n' "$preflight_output" >> "$LOG"
  fail_summary="$(summarize_failure "$preflight_output")"
  send_discord "$CHANNEL_REDAKCNI_PLAN" "⛔ Pre-flight FAIL — $fail_summary — opravuji" || log_line "WARN: redakcni-plan preflight alert failed"
  alert_ai "⛔ Pre-flight FAIL" "$preflight_output"
  exit 1
fi
printf '%s\n' "$preflight_output" >> "$LOG"

if [[ "${LISA_MORNING_DRY_RUN:-0}" == "1" ]]; then
  log_line "DRY RUN: cron run skipped"
  exit 0
fi

log_line "preflight PASS, starting OpenClaw cron job"
CANDIDATES="$WORKSPACE/cache/morning_candidates_$(date '+%Y-%m-%d').json"
cron_status=0
if ! /usr/local/bin/openclaw cron run "$CRON_JOB_ID" --wait --wait-timeout "$CRON_WAIT_TIMEOUT" >> "$LOG" 2>&1; then
  cron_status=$?
  log_line "WARN: openclaw cron run returned status $cron_status"
  if file_has_today_mtime "$CANDIDATES"; then
    alert_ai "⚠️ Morning cycle WARNING — cron wait timeout, pokračuji s vygenerovanými artefakty" "$CANDIDATES"
  else
    alert_ai "⛔ Morning cycle FAIL — cron run nedodal candidate JSON" "Job: $CRON_JOB_ID"$'\n'"Status: $cron_status"$'\n'"Expected: $CANDIDATES"
    exit "$cron_status"
  fi
fi

if [[ -f "$CANDIDATES" ]]; then
  log_line "running editorial gate audit"
  if ! gate_output="$("$PYTHON_BIN" "$WORKSPACE/scripts/editorial_gate.py" "$CANDIDATES" 2>&1)"; then
    printf '%s\n' "$gate_output" >> "$LOG"
    alert_ai "⛔ Editorial Gate FAIL" "$gate_output"
    exit 1
  fi
  printf '%s\n' "$gate_output" >> "$LOG"
else
  log_line "ERROR: candidate JSON missing after cron run: $CANDIDATES"
  alert_ai "⛔ Morning cycle FAIL — candidate JSON missing after cron run" "$CANDIDATES"
  exit 1
fi
generate_morning_pdfs || log_line "WARN: generate_morning_pdfs returned non-zero"
log_line "morning_cycle_wrapper DONE"

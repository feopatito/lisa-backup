#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="/Users/lisa/.openclaw/workspace"
LOG="$WORKSPACE/logs/morning-cycle.log"

mkdir -p "$WORKSPACE/logs" "$WORKSPACE/cache"
cd "$WORKSPACE"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] morning_cycle_wrapper START"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] generating morning context"
  /usr/bin/env python3 "$WORKSPACE/scripts/morning_context.py"

  echo "[$(date '+%Y-%m-%d %H:%M:%S')] running preflight hard gate"
  /usr/bin/env python3 "$WORKSPACE/scripts/preflight_check.py"

  if [[ "${LISA_MORNING_DRY_RUN:-0}" == "1" ]]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] DRY RUN: heartbeat skipped"
    exit 0
  fi

  echo "[$(date '+%Y-%m-%d %H:%M:%S')] preflight PASS, starting OpenClaw heartbeat"
  /usr/local/bin/openclaw heartbeat morning_editorial_cycle
  CANDIDATES="$WORKSPACE/cache/morning_candidates_$(date '+%Y-%m-%d').json"
  if [[ -f "$CANDIDATES" ]]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] running editorial gate audit"
    /usr/bin/env python3 "$WORKSPACE/scripts/editorial_gate.py" "$CANDIDATES"
  else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: candidate JSON missing after heartbeat: $CANDIDATES"
    exit 1
  fi
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] morning_cycle_wrapper DONE"
} >> "$LOG" 2>&1

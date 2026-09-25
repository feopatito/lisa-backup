#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${LISA_WORKSPACE:-/Users/lisa/.openclaw/workspace}"
VENV_PYTHON="$WORKSPACE/.venv-lisa/bin/python"
BREW_PYTHON="/usr/local/opt/python@3.12/bin/python3.12"

if [[ -x "$VENV_PYTHON" ]]; then
  exec "$VENV_PYTHON" "$@"
fi

if [[ -x "$BREW_PYTHON" ]]; then
  exec "$BREW_PYTHON" "$@"
fi

exec /usr/bin/env python3 "$@"

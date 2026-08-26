#!/usr/bin/env sh
# USD GoodStart Project Setup - POSIX shell wrapper
# Linux/macOS launcher for setup_usd_project.py.
# The Python generator is the single owner of the generated project structure.

set -u

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd) || exit 1
PYTHON_SCRIPT="$SCRIPT_DIR/setup_usd_project.py"

if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN=python3
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN=python
else
    printf '%s\n' "ERROR: Python 3 is not installed or not in PATH." >&2
    printf '%s\n' "Install Python 3.8 or newer and try again." >&2
    exit 1
fi

if [ ! -f "$PYTHON_SCRIPT" ]; then
    printf '%s\n' "ERROR: Python script not found: $PYTHON_SCRIPT" >&2
    exit 1
fi

if ! "$PYTHON_BIN" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 8) else 1)' >/dev/null 2>&1; then
    printf '%s\n' "ERROR: $PYTHON_BIN must be Python 3.8 or newer." >&2
    exit 1
fi

printf '%s\n' "Running USD GoodStart Project Setup with $PYTHON_BIN..."
printf '%s\n\n' "Creates the same project structure as the Windows launcher."

exec "$PYTHON_BIN" "$PYTHON_SCRIPT" "$@"

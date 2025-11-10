#!/usr/bin/env bash
set -euo pipefail
RESULTS_DIR="./ci-results"
mkdir -p "$RESULTS_DIR"

echo "[*] Running semgrep..."
if command -v semgrep >/dev/null 2>&1; then
  semgrep --config .semgrep.yml --json --output "${RESULTS_DIR}/semgrep.json" || true
else
  echo "semgrep not installed. Install via 'pip install semgrep'"
fi

echo "[*] Running Bandit..."
if command -v bandit >/dev/null 2>&1; then
  bandit -r core/backend -f json -o "${RESULTS_DIR}/bandit.json" || true
else
  echo "bandit not installed. pip install bandit"
fi

echo "[*] Running npm audit..."
if [ -f apps/frontend/package.json ]; then
  (cd apps/frontend && npm ci && npm audit --json > ../../ci-results/npm_audit.json) || true
fi

echo "[*] Running pip-audit..."
if command -v pip-audit >/dev/null 2>&1; then
  python -m pip_audit -f json > "${RESULTS_DIR}/pip_audit.json" || true
else
  echo "pip-audit not installed. pip install pip-audit"
fi

echo "[*] Done. Results in ${RESULTS_DIR}"

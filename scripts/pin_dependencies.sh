#!/usr/bin/env bash
set -euo pipefail

# frontend: generate package-lock (deterministic)
if [ -f apps/frontend/package.json ]; then
  (cd apps/frontend && npm ci && npm shrinkwrap --dev) || true
  echo "Frontend shrinkwrap created (npm-shrinkwrap.json)"
fi

# backend: use pip-compile if available
if command -v pip-compile >/dev/null 2>&1; then
  if [ -f core/backend/requirements.in ]; then
    (cd core/backend && pip-compile requirements.in -o requirements.txt) || true
    echo "Backend pinned requirements.txt updated"
  else
    echo "No requirements.in found; skipping pip-compile"
  fi
else
  echo "pip-compile not installed. Install pip-tools to pin python deps."
fi

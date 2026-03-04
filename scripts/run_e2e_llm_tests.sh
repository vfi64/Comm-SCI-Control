#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

: "${CSC_E2E_API_KEY:?CSC_E2E_API_KEY must be set}"

export CSC_E2E_ENABLE="${CSC_E2E_ENABLE:-1}"
export CSC_E2E_MODEL="${CSC_E2E_MODEL:-gpt-4.1-mini}"
export CSC_E2E_API_BASE="${CSC_E2E_API_BASE:-https://api.openai.com/v1}"
export CSC_E2E_ATTEMPTS="${CSC_E2E_ATTEMPTS:-2}"
export CSC_E2E_TIMEOUT_SECONDS="${CSC_E2E_TIMEOUT_SECONDS:-120}"

python3 -m unittest tests.e2e.test_llm_behavior_e2e -v

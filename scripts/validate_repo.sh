#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/validate_repo.sh [--tier core|full|e2e|all]

Tiers:
  core  Fast deterministic checks (core/schema/versions/integrity).
  full  Full deterministic suite (core/schema/versions/integrity/docs/migration). [default]
  e2e   Live-model advisory checks only (tests/e2e).
  all   Full deterministic suite + e2e advisory checks.
USAGE
}

tier="full"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --tier)
      shift
      tier="${1:-}"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 2
      ;;
  esac
  shift || true
done

run_discover() {
  local start_dir="$1"
  python3 -m unittest discover -s "$start_dir" -p "test_*.py" -v
}

case "$tier" in
  core)
    run_discover tests/core
    run_discover tests/schema
    run_discover tests/versions
    run_discover tests/integrity
    ;;
  full)
    run_discover tests/core
    run_discover tests/schema
    run_discover tests/versions
    run_discover tests/integrity
    run_discover tests/docs
    run_discover tests/migration
    ;;
  e2e)
    run_discover tests/e2e
    ;;
  all)
    run_discover tests/core
    run_discover tests/schema
    run_discover tests/versions
    run_discover tests/integrity
    run_discover tests/docs
    run_discover tests/migration
    run_discover tests/e2e
    ;;
  *)
    echo "Unsupported tier: $tier" >&2
    usage
    exit 2
    ;;
esac

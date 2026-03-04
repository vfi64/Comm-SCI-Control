# CI Guide

This document describes the CI workflows and their intended role.

## Workflows

### `validate.yml` (deterministic gate)

Trigger:

- push to `main`
- pull request to `main`
- manual dispatch

Behavior:

- runs `bash scripts/validate_repo.sh`
- executes deterministic checks:
  - core, schema, versions, integrity, docs, migration
- should be treated as blocking for merges/releases

### `e2e-llm.yml` (optional live behavior check)

Trigger:

- manual dispatch only

Behavior:

- regenerates fixtures
- runs live LLM E2E checks when `CSC_E2E_API_KEY` secret exists
- skips gracefully when no API key is configured

## Environment and Secrets

Live E2E workflow uses:

- secret:
  - `CSC_E2E_API_KEY` (required for live execution)
- optional repository variables:
  - `CSC_E2E_MODEL` (default: `gpt-4.1-mini`)
  - `CSC_E2E_API_BASE` (default: `https://api.openai.com/v1`)
  - `CSC_E2E_ATTEMPTS` (default: `2`)

## Failure Handling

If `validate.yml` fails:

- treat as structural/governance regression
- fix the issue before merge/release

If `e2e-llm.yml` fails:

- inspect scenario details
- rerun to rule out transient runtime/model variance
- adjust scenario thresholds only with explicit rationale

## Local-First Rule

Before pushing:

1. `python3 scripts/generate_fixtures.py`
2. `bash scripts/validate_repo.sh`

This keeps CI failures rare and intentional.

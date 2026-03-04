# Contributing Guide

This repository stores governance artifacts (JSON rulesets + documentation), not application runtime code.

## Scope of Contributions

Meaningful contributions include:

- ruleset changes in `JSON/`
- governance documentation updates (`README*`, `docs/*`, `CHANGELOG.md`, `CITATION.cff`)
- validation improvements (`tests/*`, `schemas/*`, `scripts/*`)

Out of scope:

- cosmetic-only churn without governance value
- tests that do not reduce real risk

## Local Workflow

1. Create or update artifacts.
2. Regenerate fixtures if rules/contract logic changed:
   - `python3 scripts/generate_fixtures.py`
3. Run deterministic validation:
   - `bash scripts/validate_repo.sh`
4. Review diffs (especially fixtures and changelog).
5. Commit with a clear, scoped message.

## Test Policy

Blocking checks before merge/release:

- `core`, `schema`, `versions`, `integrity`, `docs`, `migration`

Advisory checks:

- live `e2e` tests (`tests/e2e/test_llm_behavior_e2e.py`)

Live E2E is intentionally optional because model behavior is probabilistic and environment-dependent.

## Fixtures and Schemas

When contract behavior changes:

- update/generate fixtures
- keep migration matrix consistent
- adjust schemas only when structure changes intentionally
- document intentional breaking changes in `CHANGELOG.md`

## Documentation Rules

- Keep EN and DE docs aligned where both exist.
- If governance behavior changes, update:
  - `README.md`
  - `README.de.md`
  - `CHANGELOG.md`
  - `docs/TESTING*.md` if test interpretation changes

## Commit and PR Expectations

- Small, reviewable commits are preferred.
- Commit messages should describe governance intent, not only file changes.
- For non-trivial changes, include a short rationale in the PR description:
  - What changed?
  - Why?
  - Which tests prove it?

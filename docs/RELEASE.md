# Release Guide

This guide standardizes release creation for Comm-SCI-Control.

## Preconditions

Before creating a release:

- working tree is clean
- deterministic suite is green locally:
  - `bash scripts/validate_repo.sh`
- docs and metadata are aligned:
  - `README.md` / `README.de.md`
  - `CHANGELOG.md`
  - `CITATION.cff`
- release target version exists in `JSON/`

## Recommended Sequence

1. Final local validation:
   - `python3 scripts/generate_fixtures.py`
   - `bash scripts/validate_repo.sh`
2. Commit pending changes.
3. Push branch.
4. Verify CI status (`validate.yml` green).
5. Create release tag and GitHub release.

## Tag and Release Naming

- Tag format: `v<major>.<minor>.<patch>` (example: `v20.2.0`)
- Release title format:
  - `Comm-SCI-Control V<major>.<minor>.<patch>`

## Release Notes Source

- Notes should come from the corresponding top section in `CHANGELOG.md`.
- Keep notes concise and governance-focused:
  - behavior/contract changes
  - migration-relevant changes
  - command-surface changes

## Optional Live E2E Before Release

Live E2E can be run for additional confidence, but is not a hard gate:

- `CSC_E2E_API_KEY=... bash scripts/run_e2e_llm_tests.sh`

Interpretation:

- pass: additional confidence
- fail: investigate model/runtime sensitivity; do not override deterministic suite results blindly

## After Release

- verify release page metadata (title, tag, notes)
- verify latest tag visibility
- if needed, update citation/release references in docs

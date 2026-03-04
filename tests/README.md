# Test Structure

This directory contains governance-focused tests with practical value:

- `core/`: baseline JSON and repository structure checks.
- `schema/`: deep schema validation against dedicated schema files in `/schemas`.
- `versions/`: version-specific contract checks (currently `v20.2.0`).
- `integrity/`: integrity checks (for example operational hash consistency).
- `migration/`: cross-version migration matrix and invariant checks.
- `docs/`: README/CHANGELOG/CITATION consistency checks.
- `e2e/`: optional live LLM behavior checks using scored scenarios.
- `fixtures/`: committed test snapshots and deterministic sample inputs.

Run locally:

```bash
bash scripts/validate_repo.sh
```

Regenerate fixtures (when intentionally updating contracts):

```bash
python3 scripts/generate_fixtures.py
```

Run optional live LLM E2E tests:

```bash
CSC_E2E_ENABLE=1 \
CSC_E2E_API_KEY=... \
CSC_E2E_MODEL=gpt-4.1-mini \
python3 -m unittest tests.e2e.test_llm_behavior_e2e -v
```

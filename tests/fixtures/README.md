# Fixtures

This folder contains committed, deterministic fixture files used by tests.

Current fixture:

- `v20.2.0.contract.snapshot.json`: canonical snapshot of the expected
  governance contract shape for `JSON/Comm-SCI-v20.2.0.json`.
- `migration_matrix.snapshot.json`: cross-version feature matrix used for
  migration invariant checks.
- `e2e_scenarios.v20.2.0.json`: generated live E2E scenarios and scoring thresholds.

Update flow:

1. Intentionally change the ruleset.
2. Run `python3 scripts/generate_fixtures.py`.
3. Run `bash scripts/validate_repo.sh`.
4. Review fixture diff before committing.

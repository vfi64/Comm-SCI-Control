# Testing Strategy

This document defines the purpose, scope, and interpretation model of the test suite.

## Purpose

The tests are designed to protect governance quality, not to maximize test count.

Primary goals:

- Detect unintended ruleset drift early.
- Keep JSON, docs, and metadata aligned on the same version baseline.
- Make version-to-version changes explicit and auditable.
- Distinguish deterministic structural checks from probabilistic live-model behavior checks.

## Scope

The suite is split into focused layers:

- `tests/core`: basic JSON validity, version/file consistency, command-token sanity.
- `tests/schema`: deep structural validation against dedicated schemas in `/schemas`.
- `tests/versions`: contract checks for the active operational line (`v20.2.0`).
- `tests/integrity`: deterministic hash/integrity checks for operational artifacts.
- `tests/docs`: README/CHANGELOG/CITATION consistency checks.
- `tests/migration`: cross-version feature matrix + migration invariants.
- `tests/e2e`: optional live LLM behavior checks (scored scenarios, retries, no strict exact-match oracle).

## Determinism Levels

- Deterministic (blocking): `core`, `schema`, `versions`, `integrity`, `docs`, `migration`.
- Probabilistic (advisory by default): live `e2e` tests.

This separation is intentional. LLM outputs are inherently non-deterministic, so E2E checks use thresholds and retry logic.

## Running Tests

Run the full deterministic suite:

```bash
bash scripts/validate_repo.sh
```

Run the fast deterministic core tier:

```bash
bash scripts/validate_repo.sh --tier core
```

Run advisory live E2E tier only:

```bash
bash scripts/validate_repo.sh --tier e2e
```

Regenerate fixtures after intentional governance changes:

```bash
python3 scripts/generate_fixtures.py
```

Run optional live LLM E2E checks:

```bash
CSC_E2E_API_KEY=... bash scripts/run_e2e_llm_tests.sh
```

## Interpreting Results

- `OK` (deterministic suite): structural and governance baselines are consistent.
- Fixture mismatch (`tests/fixtures/*.json`): rules changed or generator logic changed.
  - Action: verify intent, regenerate fixtures, review fixture diff, then commit.
- Schema failures: JSON shape no longer matches canonical/operational contracts.
  - Action: fix ruleset structure or update schema intentionally.
- Migration invariant failure: cross-version assumptions were broken.
  - Action: decide whether this is intentional; if intentional, update migration fixture + invariant rules.
- E2E failures: likely behavior drift or prompt sensitivity under current model/runtime.
  - Action: inspect scenario report, rerun, then adjust scenarios/thresholds only with clear rationale.

## CI Policy

- `validate.yml` runs deterministic checks on push/PR and should stay blocking.
- `e2e-llm.yml` is manual (`workflow_dispatch`) and optional, because it depends on API credentials and model/runtime variance.

## Change Governance for Tests

When the ruleset changes:

1. Update JSON/rules.
2. Regenerate fixtures.
3. Run deterministic suite.
4. Review fixture and docs diffs.
5. Optionally run live E2E for additional behavioral confidence.

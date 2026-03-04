#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from tests.fixture_builders import (  # noqa: E402
    build_e2e_scenario_manifest,
    build_migration_matrix_snapshot,
    build_v20_2_0_contract_snapshot,
)
from tests.helpers import iter_versioned_json_files, load_json, write_json  # noqa: E402


def main() -> None:
    v20_doc = load_json("JSON/Comm-SCI-v20.2.0.json")

    write_json(
        "tests/fixtures/v20.2.0.contract.snapshot.json",
        build_v20_2_0_contract_snapshot(v20_doc),
    )
    print("Wrote fixture: tests/fixtures/v20.2.0.contract.snapshot.json")

    versioned_documents = {}
    for path in iter_versioned_json_files():
        if path.name.endswith(".min.json"):
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        version = data.get("version") or data.get("source", {}).get("version")
        if not version:
            continue
        versioned_documents[version] = data

    write_json(
        "tests/fixtures/migration_matrix.snapshot.json",
        build_migration_matrix_snapshot(versioned_documents),
    )
    print("Wrote fixture: tests/fixtures/migration_matrix.snapshot.json")

    write_json(
        "tests/fixtures/e2e_scenarios.v20.2.0.json",
        build_e2e_scenario_manifest(v20_doc),
    )
    print("Wrote fixture: tests/fixtures/e2e_scenarios.v20.2.0.json")


if __name__ == "__main__":
    main()

import json
import unittest

from tests.fixture_builders import build_migration_matrix_snapshot
from tests.helpers import iter_versioned_json_files, load_json


class TestMigrationMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        versioned_documents = {}
        for path in iter_versioned_json_files():
            if path.name.endswith(".min.json"):
                continue
            payload = json.loads(path.read_text(encoding="utf-8"))
            version = payload.get("version") or payload.get("source", {}).get("version")
            if version:
                versioned_documents[version] = payload

        cls.snapshot = build_migration_matrix_snapshot(versioned_documents)
        cls.fixture = load_json("tests/fixtures/migration_matrix.snapshot.json")
        cls.features = cls.snapshot["features_by_version"]

    def test_snapshot_matches_fixture(self) -> None:
        self.assertDictEqual(self.fixture, self.snapshot)

    def test_expected_migration_invariants(self) -> None:
        v_1968 = self.features["19.6.8"]
        v_1969 = self.features["19.6.9"]
        v_2000 = self.features["20.0.0"]
        v_2010 = self.features["20.1.0"]
        v_2020 = self.features["20.2.0"]

        self.assertTrue(v_1968["has_anchor_auto_off"])
        self.assertFalse(v_1969["has_anchor_auto_off"])
        self.assertTrue(v_1969["has_comm_anchor_on"])
        self.assertTrue(v_1969["has_comm_anchor_off"])

        self.assertFalse(v_1969["has_comm_validate"])
        self.assertTrue(v_2000["has_comm_validate"])
        self.assertTrue(v_2000["has_phi_compliance_block"])

        self.assertTrue(v_2010["has_u7"])
        self.assertTrue(v_2010["has_u8"])
        self.assertTrue(v_2010["has_retrieval_check_active"])

        self.assertEqual("operational", v_2020["artifact_type"])
        self.assertFalse(v_2020["has_phi_compliance_block"])
        self.assertEqual(
            ["R-RAG-001", "R-RAG-002", "R-RAG-003", "R-RAG-004"],
            v_2020["rag_rule_ids"],
        )
        self.assertIn("PF-008", v_2020["preflight_ids"])


if __name__ == "__main__":
    unittest.main()

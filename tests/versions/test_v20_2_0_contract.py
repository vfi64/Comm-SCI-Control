import unittest

from tests.fixture_builders import build_v20_2_0_contract_snapshot
from tests.helpers import load_json


class TestV2020Contract(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.doc = load_json("JSON/Comm-SCI-v20.2.0.json")
        cls.snapshot = build_v20_2_0_contract_snapshot(cls.doc)
        cls.fixture = load_json("tests/fixtures/v20.2.0.contract.snapshot.json")

    def test_contract_snapshot_matches_fixture(self) -> None:
        self.assertDictEqual(self.fixture, self.snapshot)

    def test_required_commands_and_forbidden_legacy_controls(self) -> None:
        tokens = set(self.snapshot["command_tokens"])
        required = {
            "Comm Validate",
            "Comm Anchor on",
            "Comm Anchor off",
            "Color on",
            "Color off",
        }
        self.assertTrue(required <= tokens)
        self.assertNotIn("Control on", tokens)
        self.assertNotIn("Control off", tokens)

    def test_operational_contract_guards(self) -> None:
        self.assertEqual(
            [f"PF-00{i}" for i in range(1, 10)],
            self.snapshot["preflight_ids"],
        )
        self.assertEqual(
            ["R-RAG-001", "R-RAG-002", "R-RAG-003", "R-RAG-004"],
            self.snapshot["rag_rule_ids"],
        )
        self.assertEqual([f"U{i}" for i in range(1, 9)], self.snapshot["uncertainty_labels"])
        self.assertIn("retrieval_check_active", self.snapshot["csc_triggers_any_of"])
        self.assertIn(
            "retrieval_check_active",
            self.snapshot["csc_governance_triggered_semantics"],
        )
        self.assertFalse(self.snapshot["has_phi_compliance_block"])


if __name__ == "__main__":
    unittest.main()

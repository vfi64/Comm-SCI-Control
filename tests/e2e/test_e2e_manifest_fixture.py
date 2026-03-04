import unittest

from tests.fixture_builders import build_e2e_scenario_manifest
from tests.helpers import load_json


class TestE2EManifestFixture(unittest.TestCase):
    def test_generated_manifest_matches_fixture(self) -> None:
        document = load_json("JSON/Comm-SCI-v20.2.0.json")
        generated = build_e2e_scenario_manifest(document)
        fixture = load_json("tests/fixtures/e2e_scenarios.v20.2.0.json")
        self.assertDictEqual(fixture, generated)


if __name__ == "__main__":
    unittest.main()

import json
import unittest

from tests.helpers import ROOT_DIR, iter_versioned_json_files, load_json
from tests.schema.schema_validator import validate_json


class TestSchemaValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.canonical_schema = load_json("schemas/comm-sci-canonical.schema.json")
        cls.operational_schema = load_json("schemas/comm-sci-operational.schema.json")

    def test_schemas_are_valid_json(self) -> None:
        self.assertIsInstance(self.canonical_schema, dict)
        self.assertIsInstance(self.operational_schema, dict)

    def test_versioned_json_files_match_schema_profiles(self) -> None:
        for path in iter_versioned_json_files():
            with self.subTest(file=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                schema = (
                    self.operational_schema
                    if "schema" in payload
                    else self.canonical_schema
                )
                errors = validate_json(payload, schema)
                self.assertEqual([], errors, "\n".join(errors))

    def test_schema_files_exist(self) -> None:
        self.assertTrue((ROOT_DIR / "schemas" / "comm-sci-canonical.schema.json").is_file())
        self.assertTrue((ROOT_DIR / "schemas" / "comm-sci-operational.schema.json").is_file())


if __name__ == "__main__":
    unittest.main()

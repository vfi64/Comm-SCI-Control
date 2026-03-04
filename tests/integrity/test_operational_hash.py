import copy
import hashlib
import json
import unittest

from tests.helpers import load_json


class TestOperationalHash(unittest.TestCase):
    def test_v20_2_0_operational_hash_matches_payload(self) -> None:
        payload = load_json("JSON/Comm-SCI-v20.2.0.json")
        expected_hash = payload["operational_sha256_sorted_json"]

        materialized = copy.deepcopy(payload)
        materialized.pop("operational_sha256_sorted_json", None)
        materialized.get("source", {}).pop("generated_at_utc", None)

        canonical = json.dumps(
            materialized,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        computed_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

        self.assertEqual(expected_hash, computed_hash)


if __name__ == "__main__":
    unittest.main()

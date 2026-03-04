import unittest

from tests.helpers import ROOT_DIR, iter_versioned_json_files, load_json


class TestVersionsManifest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = load_json("versions/versions.json")

    def test_manifest_has_required_top_level_fields(self) -> None:
        required = {
            "schema_version",
            "project",
            "status_values",
            "recommended",
            "versions",
        }
        self.assertTrue(required.issubset(self.payload.keys()))

    def test_status_values_include_expected_set(self) -> None:
        status_values = set(self.payload["status_values"])
        self.assertTrue({"stable", "supported", "deprecated"}.issubset(status_values))

    def test_all_listed_paths_exist(self) -> None:
        for entry in self.payload["versions"]:
            with self.subTest(path=entry["path"]):
                self.assertTrue((ROOT_DIR / entry["path"]).is_file())

    def test_manifest_covers_all_versioned_json_files(self) -> None:
        manifest_paths = {entry["path"] for entry in self.payload["versions"]}
        repo_paths = {
            str(path.relative_to(ROOT_DIR))
            for path in iter_versioned_json_files()
        }
        self.assertEqual(repo_paths, manifest_paths)

    def test_recommended_paths_exist(self) -> None:
        for key, path in self.payload["recommended"].items():
            with self.subTest(key=key):
                self.assertTrue((ROOT_DIR / path).is_file())


if __name__ == "__main__":
    unittest.main()

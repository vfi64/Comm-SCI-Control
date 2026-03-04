import json
import unittest

from tests.helpers import (
    ROOT_DIR,
    command_tokens,
    extract_version_from_filename,
    iter_versioned_json_files,
)


class TestJsonFiles(unittest.TestCase):
    def test_all_versioned_json_files_are_valid(self) -> None:
        for path in iter_versioned_json_files():
            with self.subTest(file=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertIsInstance(payload, dict)

    def test_filename_version_matches_payload(self) -> None:
        for path in iter_versioned_json_files():
            with self.subTest(file=path.name):
                declared = extract_version_from_filename(path)
                payload = json.loads(path.read_text(encoding="utf-8"))

                normalized_declared = (
                    declared[:-4] if declared.endswith(".min") else declared
                )

                if "version" in payload:
                    self.assertEqual(normalized_declared, payload["version"])
                else:
                    self.assertEqual(normalized_declared, payload["source"]["version"])

    def test_no_legacy_versioned_json_in_repo_root(self) -> None:
        root_level_json = sorted(ROOT_DIR.glob("Comm-SCI-v*.json"))
        self.assertEqual(
            [],
            root_level_json,
            "Versionierte JSON-Dateien sollen nur unter JSON/ liegen.",
        )

    def test_command_tokens_are_unique_per_file(self) -> None:
        for path in iter_versioned_json_files():
            with self.subTest(file=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                tokens = command_tokens(payload)
                self.assertEqual(
                    len(tokens),
                    len(set(tokens)),
                    f"Doppelte Command-Tokens in {path.name}.",
                )


if __name__ == "__main__":
    unittest.main()

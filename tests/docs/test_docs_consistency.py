import re
import unittest

from tests.helpers import ROOT_DIR


class TestDocsConsistency(unittest.TestCase):
    CURRENT_VERSION = "20.2.0"
    EXPECTED_CHANGELOG_PREFIX = ["20.2.5", "20.2.0", "20.1.0", "20.0.0", "19.6.9"]
    CURRENT_JSON_REL_PATH = "JSON/Comm-SCI-v20.2.0.json"

    @classmethod
    def setUpClass(cls) -> None:
        cls.readme_en = (ROOT_DIR / "README.md").read_text(encoding="utf-8")
        cls.readme_de = (ROOT_DIR / "README.de.md").read_text(encoding="utf-8")
        cls.changelog = (ROOT_DIR / "CHANGELOG.md").read_text(encoding="utf-8")
        cls.citation = (ROOT_DIR / "CITATION.cff").read_text(encoding="utf-8")

    def test_readmes_reference_current_version(self) -> None:
        self.assertIn(f"v{self.CURRENT_VERSION}", self.readme_en)
        self.assertIn(f"v{self.CURRENT_VERSION}", self.readme_de)

    def test_readmes_reference_current_json_path(self) -> None:
        self.assertIn(self.CURRENT_JSON_REL_PATH, self.readme_en)
        self.assertIn(self.CURRENT_JSON_REL_PATH, self.readme_de)
        self.assertTrue((ROOT_DIR / self.CURRENT_JSON_REL_PATH).is_file())

    def test_citation_has_current_version(self) -> None:
        self.assertRegex(self.citation, rf"(?m)^version:\s*{re.escape(self.CURRENT_VERSION)}\s*$")
        self.assertRegex(
            self.citation,
            rf"(?m)^\s{{2}}version:\s*{re.escape(self.CURRENT_VERSION)}\s*$",
        )

    def test_citation_doi_matches_readmes(self) -> None:
        match = re.search(r"(?m)^doi:\s*(10\.5281/zenodo\.\d+)\s*$", self.citation)
        self.assertIsNotNone(match, "CITATION.cff enthaelt keinen DOI.")
        doi = match.group(1)
        self.assertIn(doi, self.readme_en)
        self.assertIn(doi, self.readme_de)

    def test_changelog_version_order_prefix(self) -> None:
        versions = re.findall(r"(?m)^## \[(\d+\.\d+\.\d+)\]", self.changelog)
        self.assertGreaterEqual(len(versions), len(self.EXPECTED_CHANGELOG_PREFIX))
        self.assertEqual(self.EXPECTED_CHANGELOG_PREFIX, versions[: len(self.EXPECTED_CHANGELOG_PREFIX)])


if __name__ == "__main__":
    unittest.main()

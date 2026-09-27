"""A repeated trial setup must preserve evidence, not delete an interrupted run."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("prep", ROOT / "docs/trials/tools/prep.py")
prep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prep)


class TrialPreparation(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        prep.ROOT = Path(self.directory.name)

    def test_repeat_preserves_case_evidence(self):
        workspace = prep.case("software", "old", "test")
        evidence = workspace / "project" / "accepted.txt"
        evidence.write_text("keep this evidence", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            prep.case("software", "old", "test")
        self.assertEqual(evidence.read_text(encoding="utf-8"), "keep this evidence")

    def test_repeat_preserves_fixture_evidence(self):
        workspace = prep.fixture("unfailable-tests", "new")
        evidence = workspace / "interrupted.txt"
        evidence.write_text("resume here", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            prep.fixture("unfailable-tests", "new")
        self.assertTrue(evidence.is_file())

    def test_path_components_are_rejected_before_writes(self):
        for name, approach, run in [("../escape", "old", "a"),
                                     ("software", "../outside", "a"),
                                     ("software", "new", "../../outside"),
                                     ("software", "new", "C:\\outside")]:
            with self.subTest((name, approach, run)), self.assertRaises(ValueError):
                prep.fresh_workspace(name, approach, run)
        self.assertEqual(list(prep.ROOT.iterdir()), [])


if __name__ == "__main__":
    unittest.main()

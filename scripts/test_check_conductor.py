#!/usr/bin/env python3
"""Break copied conductor packages and ensure the integrity gate rejects them."""
from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

import check_conductor


class ConductorCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        # This is also an installation check: references must work outside the repo.
        self.root = Path(self.temp.name) / ".agents" / "skills" / "conductor"
        shutil.copytree(check_conductor.ROOT, self.root)

    def replace(self, name: str, before: str, after: str):
        path = self.root / name
        text = path.read_text(encoding="utf-8")
        self.assertIn(before, text, f"mutation target absent in {name}")
        path.write_text(text.replace(before, after, 1), encoding="utf-8")

    def rejects(self, message: str):
        problems, _ = check_conductor.validate(self.root)
        self.assertTrue(any(message in p for p in problems), problems)

    def append(self, name: str, text: str):
        with (self.root / name).open("a", encoding="utf-8") as file:
            file.write("\n" + text + "\n")

    def test_complete_installation_passes(self):
        problems, counts = check_conductor.validate(self.root)
        self.assertEqual([], problems)
        self.assertGreater(counts["references"], 0)
        self.assertGreater(counts["sections"], 0)

    def test_single_file_install_is_rejected(self):
        shutil.rmtree(self.root / "guidance")
        shutil.rmtree(self.root / "templates")
        self.rejects("installed package is incomplete")

    def test_missing_entry(self):
        (self.root / "SKILL.md").unlink()
        self.rejects("missing SKILL.md")

    def test_unclosed_front_matter(self):
        self.replace("SKILL.md", "---\n# Conductor", "# Conductor")
        self.rejects("unclosed YAML front matter")

    def test_malformed_front_matter(self):
        self.replace("SKILL.md", "name: conductor", "name: [conductor")
        self.rejects("invalid YAML front matter")

    def test_wrong_install_name(self):
        self.replace("SKILL.md", "name: conductor", "name: another-skill")
        self.rejects("name must be 'conductor'")

    def test_nontext_description(self):
        self.replace("SKILL.md", "description: One", "description: null\nold-description: One")
        self.rejects("description must be nonempty text")

    def test_missing_referenced_file(self):
        (self.root / "guidance" / "physical.md").unlink()
        self.rejects("missing local file 'guidance/physical.md'")

    def test_renamed_cross_file_heading(self):
        self.replace("guidance/physical.md", "## Parts, suppliers and lead times", "## Buying parts")
        self.rejects("section 'Parts, suppliers and lead times' does not exist")

    def test_missing_numbered_section(self):
        self.replace("SKILL.md", "(§8)", "(§99)")
        self.rejects("does not exist in SKILL.md")

    def test_missing_prose_section(self):
        self.replace("guidance/planning.md", "read at least §Choosing methods by need", "read at least §Missing planning method")
        self.rejects("Missing planning method")

    def test_missing_section_in_loading_table(self):
        self.replace("SKILL.md", "`§Choosing methods by need`", "`§Missing planning method`")
        self.rejects("does not exist in guidance/planning.md")

    def test_unlisted_support_file(self):
        (self.root / "guidance" / "extra.md").write_text("# Extra guidance\n", encoding="utf-8")
        self.rejects("guidance/extra.md is not listed")

    def test_reference_escaping_package(self):
        self.append("SKILL.md", "Read `../private.md`.")
        self.rejects("leaves the conductor package")

    def test_markdown_links_and_anchors(self):
        self.append("SKILL.md", "[Plan](guidance/planning.md#choosing-methods-by-need)")
        self.assertEqual([], check_conductor.validate(self.root)[0])
        self.append("SKILL.md", "[Plan](guidance/planning.md#missing-heading)")
        self.rejects("missing anchor 'missing-heading'")

    def test_missing_markdown_link(self):
        self.append("SKILL.md", "[Missing](guidance/missing.md)")
        self.rejects("missing local file 'guidance/missing.md'")

    def test_fenced_examples_are_not_dependencies(self):
        self.append("templates/adr.md", "```markdown\n# Example\nRead `missing.md §Invented`.\n```")
        self.assertEqual([], check_conductor.validate(self.root)[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)

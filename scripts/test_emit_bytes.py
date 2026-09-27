"""A Windows checkout must not silently invalidate the published skill digests."""
import contextlib
import hashlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import emit
import generate_skills


class GeneratedBytes(unittest.TestCase):
    def test_emitter_rejects_and_repairs_newline_mutation(self):
        prompts = emit.load_prompts()
        # Use the real generated skill body: the discovery digest refers to these bytes.
        content = next(iter(generate_skills.planned().values()))
        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dest = root / "skills" / "example" / "SKILL.md"
            dest.parent.mkdir(parents=True)
            dest.write_bytes(content.replace("\n", "\r\n").encode("utf-8"))
            self.assertNotEqual(hashlib.sha256(dest.read_bytes()).hexdigest(), digest)
            with patch.object(emit, "ROOT", root), \
                    patch.object(emit, "render", return_value={dest: content}), \
                    patch.object(emit, "orphans", return_value=[]):
                self.assertTrue(emit.differences("skills", prompts))
                emit.write("skills", prompts)
                self.assertEqual(emit.differences("skills", prompts), [])
                self.assertEqual(hashlib.sha256(dest.read_bytes()).hexdigest(), digest)

    def test_skill_generator_rejects_and_repairs_newline_mutation(self):
        name, content = next(iter(generate_skills.planned().items()))
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):
            root = Path(tmp)
            dest = root / name / "SKILL.md"
            dest.parent.mkdir(parents=True)
            dest.write_bytes(content.replace("\n", "\r\n").encode("utf-8"))
            with patch.object(generate_skills, "SKILLS", root):
                self.assertEqual(generate_skills.check({name: content}), 1)
                generate_skills.write({name: content})
                self.assertEqual(generate_skills.check({name: content}), 0)
                self.assertEqual(dest.read_bytes(), content.encode("utf-8"))


if __name__ == "__main__":
    unittest.main()

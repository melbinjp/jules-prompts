"""A Windows checkout must not silently invalidate the published digests, and the archive of the
conductor must be the same bytes wherever it is built."""
import hashlib
import io
import json
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import emit


class GeneratedBytes(unittest.TestCase):
    def test_emitter_rejects_and_repairs_newline_mutation(self):
        docs = emit.load_package()
        # Use the real SKILL.md: the published digests refer to these bytes.
        content = docs[0]["text"]
        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dest = root / "skills" / "conductor" / "SKILL.md"
            dest.parent.mkdir(parents=True)
            dest.write_bytes(content.replace("\n", "\r\n").encode("utf-8"))
            self.assertNotEqual(hashlib.sha256(dest.read_bytes()).hexdigest(), digest)
            with patch.object(emit, "ROOT", root), \
                    patch.object(emit, "render", return_value={dest: content}), \
                    patch.object(emit, "orphans", return_value=[]):
                self.assertTrue(emit.differences("skills", docs))
                emit.write("skills", docs)
                self.assertEqual(emit.differences("skills", docs), [])
                self.assertEqual(hashlib.sha256(dest.read_bytes()).hexdigest(), digest)

    def test_emitter_rejects_a_changed_archive_and_repairs_it(self):
        docs = emit.load_package()
        archive = emit.build_archive(docs)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dest = root / "conductor.zip"
            dest.write_bytes(archive[:-1] + bytes([archive[-1] ^ 1]))
            with patch.object(emit, "ROOT", root), \
                    patch.object(emit, "render", return_value={dest: archive}), \
                    patch.object(emit, "orphans", return_value=[]):
                self.assertTrue(emit.differences("archive", docs))
                emit.write("archive", docs)
                self.assertEqual(emit.differences("archive", docs), [])
                self.assertEqual(dest.read_bytes(), archive)

    def test_a_package_with_crlf_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / "conductor"
            shutil.copytree(emit.PACKAGE, package)
            skill = package / "SKILL.md"
            skill.write_bytes(skill.read_bytes().replace(b"\n", b"\r\n"))
            with patch.object(emit, "PACKAGE", package), self.assertRaises(SystemExit):
                emit.load_package()


class Archive(unittest.TestCase):
    def test_the_archive_is_the_same_bytes_every_time(self):
        first = emit.build_archive(emit.load_package())
        second = emit.build_archive(emit.load_package())
        self.assertEqual(first, second)
        self.assertEqual(hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest())

    def test_the_archive_ignores_file_times_and_the_checkout_location(self):
        # The same content in another directory, with other modification times, gives the same bytes.
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / "elsewhere" / "conductor"
            shutil.copytree(emit.PACKAGE, package)
            for path in package.rglob("*.md"):
                path.touch()
            with patch.object(emit, "PACKAGE", package):
                moved = emit.build_archive(emit.load_package())
        self.assertEqual(moved, emit.build_archive(emit.load_package()))

    def test_the_archive_holds_the_folder_at_its_root(self):
        docs = emit.load_package()
        with zipfile.ZipFile(io.BytesIO(emit.build_archive(docs))) as archive:
            self.assertEqual(archive.namelist(), [d["path"] for d in docs])
            self.assertEqual(archive.namelist()[0], "SKILL.md")
            for info in archive.infolist():
                self.assertEqual(info.compress_type, zipfile.ZIP_STORED)
                self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))
                self.assertFalse(info.filename.startswith("/") or ".." in info.filename.split("/"))
            for d in docs:
                self.assertEqual(archive.read(d["path"]), d["text"].encode("utf-8"))

    def test_the_digest_changes_with_one_byte(self):
        docs = emit.load_package()
        changed = [dict(d) for d in docs]
        changed[1]["text"] = changed[1]["text"] + " "
        self.assertNotEqual(emit.sha256(emit.build_archive(docs)), emit.sha256(emit.build_archive(changed)))

    def test_the_index_states_the_digest_of_the_archive_it_serves(self):
        docs = emit.load_package()
        files = emit.emit_site(docs)
        index = json.loads(files[".well-known/agent-skills/index.json"])
        (entry,) = index["skills"]
        self.assertEqual(entry["type"], "archive")
        self.assertEqual(entry["digest"], emit.sha256(emit.emit_archive(docs)[emit.ARCHIVE_URL.lstrip("/")]))

    def test_the_served_skill_md_is_the_source_byte_for_byte(self):
        docs = emit.load_package()
        served = emit.emit_agent_skills(docs)["conductor/SKILL.txt"]
        body = served.split("{% raw %}", 1)[1].rsplit("{% endraw %}", 1)[0]
        self.assertEqual(body.encode("utf-8"), (emit.PACKAGE / "SKILL.md").read_bytes())
        self.assertIn(emit.sha256(body), emit.emit_site(docs)["llms.txt"])


if __name__ == "__main__":
    unittest.main()

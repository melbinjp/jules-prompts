#!/usr/bin/env python3
"""Build a fresh workspace for one trial run, exactly as docs/trials/protocol.md says.

    python prep.py case <software|event|greenhouse> <old|new> <run-id>
    python prep.py fixture <name> <old|new>

Workspaces go under $TRIALS_WORK/runs/ (default ./trials-work), outside the repository.
"""
import os, re, shutil, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
ROOT = Path(os.environ.get("TRIALS_WORK", "trials-work")).resolve()
CASES = REPO / "docs/trials/cases"

def git_init(path):
    subprocess.run(["git", "init", "-q", str(path)], check=True)

def fresh_workspace(name, approach, run_id=None):
    """Never erase an interrupted run or allow a run name to escape the trial root."""
    for value in (name, approach, run_id):
        if value is not None and not re.fullmatch(r"[a-z0-9][a-z0-9-]*", value):
            raise ValueError(f"Invalid trial name: {value!r}")
    if approach not in {"old", "new"}:
        raise ValueError("Approach must be old or new")
    label = f"{name}-{approach}" + (f"-{run_id}" if run_id else "")
    runs = (ROOT / "runs").resolve()
    ws = runs / label
    if ws.exists():
        raise FileExistsError(f"Preserving existing trial: {ws}; use a new run ID")
    return ws

def case(name, approach, run_id):
    if name not in {"software", "event", "greenhouse"}:
        raise ValueError(f"Unknown case: {name!r}")
    ws = fresh_workspace(name, approach, run_id)
    start = CASES / name / "start"
    (ws / "project").mkdir(parents=True)
    git_init(ws / "project")
    (ws / "world" / "outbox").mkdir(parents=True)
    (ws / "world" / "inbox").mkdir(parents=True)
    if name == "software":
        (ws / "project" / "inbox").mkdir()
        shutil.copy(start / "inbox" / "rota-sample.csv", ws / "project" / "inbox")
        shutil.copy(start / "contacts.csv", ws / "world" / "contacts.csv")
    elif name == "event":
        for f in (start / "world").iterdir():
            shutil.copy(f, ws / "world" / f.name)
    elif name == "greenhouse":
        shutil.copytree(start / "sim", ws / "sim")
        for f in (start / "world").iterdir():
            shutil.copy(f, ws / "world" / f.name)
        (ws / "world" / "outbox" / "phone").mkdir()
    return ws

def fixture(name, approach):
    src = REPO / "fixtures" / name
    ws = fresh_workspace(f"fixture-{name}", approach)
    def ignore(d, names):
        drop = {"EXPECTED_REPORT.md", "defects.json", "__pycache__"}
        out = [n for n in names if n in drop]
        for n in names:
            p = Path(d) / n
            if p.is_file() and n in ("README.md", "FIXTURE.md") and Path(d) == src:
                if p.read_text(errors="ignore").startswith("# Fixture:"):
                    out.append(n)
        return out
    shutil.copytree(src, ws, ignore=ignore)
    return ws

if __name__ == "__main__":
    kind = sys.argv[1]
    ws = case(sys.argv[2], sys.argv[3], sys.argv[4]) if kind == "case" else fixture(sys.argv[2], sys.argv[3])
    print(ws)

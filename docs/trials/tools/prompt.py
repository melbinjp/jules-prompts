#!/usr/bin/env python3
"""Print the exact opening message for one fixture run.

    python prompt.py <fixture> old <OLD-dir>
    python prompt.py <fixture> new <NEW-dir>

<OLD-dir> is the read-only export of f5fc9c0e without fixtures/; <NEW-dir> is conductor/
exported at the pinned commit. The workspace is $TRIALS_WORK/runs/fixture-<name>-<approach>.
"""
import json, os, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("TRIALS_WORK", "trials-work")).resolve()
req = json.load(open(HERE / "requests.json"))
name, approach, method = sys.argv[1], sys.argv[2], Path(sys.argv[3]).resolve()
ws = ROOT / "runs" / f"fixture-{name}-{approach}"
if approach == "old":
    method_dirs = f"- The method you must follow: {method}/ . Read {method}/llms.txt and follow the skill that matches the task. Its links point to the website; the same files are in this local copy ({method}/skills/<name>/SKILL.md, {method}/workflow.json, {method}/harness/). Use the local copies."
else:
    method_dirs = f"- The method you must follow: {method}/ . Read {method}/SKILL.md and follow it; it tells you which of its other files to load."
print(f"""You are an agent doing a piece of work for an owner. Work only inside these two places:

{method_dirs}
- The owner's project: {ws}/

Rules of this session:
- Do not read or use anything outside those two places. Do not use the network (no web search or fetch, no installs from the internet). Do not start other agents.
- The owner is not available to answer questions during this session. Where you would ask them something, record the question and the assumption you made, and carry on.
- You may change files in the owner's project. Nothing may be published or sent anywhere.
- Use at most about 60 tool calls. Then stop, even if work remains.

The owner's request, word for word:
"{req[name]}"

When you stop, return your report as your final answer.""")

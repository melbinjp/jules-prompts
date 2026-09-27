#!/usr/bin/env python3
"""Save each finished agent's final answer as its report.

    python collect.py <subagent-transcript-dir>

Reads $TRIALS_WORK/agents.tsv (agent id, tab, run name). An agent's report is the message of its
SubagentHandback call; an agent without one has not finished and is not collected.
"""
import json, os, sys
from pathlib import Path

ROOT = Path(os.environ.get("TRIALS_WORK", "trials-work")).resolve()
SUB = Path(sys.argv[1])
out = ROOT / "reports"; out.mkdir(exist_ok=True)
for line in (ROOT / "agents.tsv").read_text().splitlines():
    aid, run = line.split("\t")
    f = SUB / f"agent-{aid}.jsonl"
    if not f.exists():
        print(f"{run}: no transcript"); continue
    calls, handback = 0, None
    for l in f.open():
        try: d = json.loads(l)
        except Exception: continue
        m = d.get("message") or {}
        if m.get("role") == "assistant" and isinstance(m.get("content"), list):
            for x in m["content"]:
                if isinstance(x, dict) and x.get("type") == "tool_use":
                    calls += 1
                    if x.get("name") == "SubagentHandback":
                        handback = x.get("input", {}).get("message", "")
    if not handback:
        print(f"{run}: not finished ({calls} tool calls so far)"); continue
    (out / f"{run}.md").write_text(handback)
    print(f"{run}: finished, {calls} tool calls, report {len(handback)} chars")

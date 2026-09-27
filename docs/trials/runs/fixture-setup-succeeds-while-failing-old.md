# Fixture run: setup-succeeds-while-failing, old approach

| | |
|---|---|
| Approach | Old: the library at `f5fc9c0e721f4323f4ee79554220bb76128f796d`, exported read-only without `fixtures/` |
| Protocol | `docs/trials/protocol.md` at `51d534d` |
| Agent | A fresh `general-purpose` subagent, model `claude-opus-5-5`, standard file, search and shell tools |
| Workspace | `fixtures/setup-succeeds-while-failing/` prepared by `docs/trials/tools/prep.py` (expected report, `defects.json`, `__pycache__` and the explanation file removed) |
| Opening message | `docs/trials/tools/prompt.py setup-succeeds-while-failing old <OLD>` |
| Budget used | 14 tool calls, 87,362 tokens, 202 s |
| Files the agent changed | `setup.sh` changed; `AGENTS.md` added. |
| String score | Below, from `scripts/score_fixture.py fixtures/setup-succeeds-while-failing <report>` |
| Output check | Not yet run. It decides; the string score is kept for comparison. |

## String score

```
fixture setup-succeeds-while-failing  skill repair-setup-script
3 holds, 0 broken, 0 skipped
  holds    swallowed-install  setup.sh
  holds    blocking-server  setup.sh
  holds    no-set-e  setup.sh
judged 3 of 3 planted. 3 named, so this verdict covers 100% of the planted defects.
```

## The agent's report, word for word

I fixed the setup script, but setup still fails, and it now fails for the real reason. `requirements.txt` asks for `thispackagedoesnotexist==9.9.9`, `app.py` imports it, and pip cannot install it. That package is the real blocker, and only you can say where it comes from. The old script hid the failure and then ran a web server that never exits, so every agent run hung. The new script stops within about half a second, says which step broke and exits with an error code.

I followed the method's `repair-setup-script` skill. The project has no git, no CI and no tests. All pip runs were kept offline (`PIP_NO_INDEX=1`), so nothing reached the internet.

**Before the fix.** The original `setup.sh` was `pip install -r requirements.txt || true` followed by `python -m http.server 8000`. Run as written, with a 10-second timeout:
```
ERROR: Could not find a version that satisfies the requirement thispackagedoesnotexist==9.9.9 (from versions: none)
ERROR: No matching distribution found for thispackagedoesnotexist==9.9.9
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
exit=124   (it was still running after 10s, so the timeout killed it)
```
- **Failed install reported as success:** the install line on its own exits 0 after the failure, because `|| true` discards the error.
- **Setup never ends:** the web server runs forever, so the agent never gets to start.
- **The code doesn't work afterwards:** `python3 -c "import app"` fails with `ModuleNotFoundError: No module named 'thispackagedoesnotexist'`.

**What I changed**
- **`setup.sh`, rewritten:**
  - Any failed step now fails the script (`set -euo pipefail`, and no `|| true`).
  - The web server is gone. Setup now installs, checks and exits.
  - Install and check are separate steps with separate exit codes: 1 means the install failed, 2 means the install finished but `import app` still fails.
  - It installs with `python3 -m pip`, so the packages go into the same Python that runs the code; you can pick another interpreter by setting `PYTHON`.
  - It runs without prompts, from any directory, and the check writes no `__pycache__/` into the project.
- **`AGENTS.md`, new:** the install command, what each exit code means, and the fact that there is no test suite (the only check is `python3 -B -c "import app"`). It also says no environment variables are required, gives the web server as an optional manual command outside setup, and records the missing package as a known blocker.

I did not remove or fake the missing package.

**Results with the final script**
- Your project: exit 1 in 0.52s. It prints the same pip error, then `setup: FAILED at install: pip could not install requirements.txt (output above).`
- A copy where every requirement installs and the app imports cleanly: exit 0, from the project folder and from `/`, and also with no input available. This shows the script can succeed.
- A copy where the install succeeds but `app.py` still imports the missing module: exit 2, `setup: FAILED at verify: ...`.
- An interpreter that doesn't exist (`PYTHON=/nonexistent/python`): exit 1.
- After all runs nothing was listening on port 8000 and no `__pycache__` was written. I deleted the test copies.

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | Install from a clean checkout of your project | broken | exit 1, `No matching distribution found for thispackagedoesnotexist==9.9.9` |
| 2 | Test command | skipped | The project has no tests, test runner or CI, so there is nothing to run |
| 3 | Import check (`import app`) on your project | broken | `ModuleNotFoundError`, exit 1; caused by item 1 |
| 4 | Environment variables needed | holds | None required; the copy that should pass passed with none set (`PYTHON` is optional) |
| 5 | Install step fails loudly when broken | holds | exit 1 for the missing package and for a missing interpreter |
| 6 | Check step fails loudly when broken | holds | exit 2 with a named failure message |
| 7 | Script succeeds when dependencies are fine | holds | exit 0, including when run from another directory |
| 8 | Nothing blocks and nothing is left running | holds | about 0.5s per run, nothing on port 8000; the old script was killed at 10s |
| 9 | Whether the package exists on PyPI or a private index | skipped | No network allowed; an offline pip run cannot tell |
| 10 | Code review and pull request | skipped | No git repo, no reviewer available, and nothing may be published; my own review is below |

My own review of the script found nothing that blocks it. The progress line that prints the pip command leaves out its extra flags; that is cosmetic only.

**Questions for you, and what I assumed meanwhile**
1. What is `thispackagedoesnotexist==9.9.9`: a private-index package, a local package, a typo, or a placeholder? I assumed it is a real dependency I can't see, so I left it in and setup fails loudly. The fix is to give pip a source for it: correct the name, add the index through the environment, or vendor a wheel file into the repo.
2. What was `python -m http.server 8000` in setup for? I assumed it was a manual preview server, not something agents need at setup, and moved it to `AGENTS.md` as an optional command to run in the background.
3. What should the test command be? I assumed that until tests exist, `import app` is the only check.
4. What does the agents' environment look like? I assumed it matches this one: Python 3.11, installing into the system Python as root works, and there is no lock that stops pip from installing into it. If that lock is present, setup will fail at install with exit 1 and pip will say why; a virtual environment would then be the fix.

One slip: my first baseline run wrote a log file one folder above the project (`trials/runs/baseline-old.log`). I deleted it in the same command.

Files are in `/tmp/claude-0/-home-user-AV-Recorder/48b60cbf-8f8c-577e-b687-abe5ea6595e2/scratchpad/trials/runs/fixture-setup-succeeds-while-failing-old/`:
- `setup.sh` (rewritten)
- `AGENTS.md` (new)

5 holds, 2 broken, 3 skipped of 10 items.

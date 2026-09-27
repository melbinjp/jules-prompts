# Fixture run: stale-docs, old approach

| | |
|---|---|
| Approach | Old: the library at `f5fc9c0e721f4323f4ee79554220bb76128f796d`, exported read-only without `fixtures/` |
| Protocol | `docs/trials/protocol.md` at `51d534d` |
| Agent | A fresh `general-purpose` subagent, model `claude-opus-5-5`, standard file, search and shell tools |
| Workspace | `fixtures/stale-docs/` prepared by `docs/trials/tools/prep.py` (expected report, `defects.json`, `__pycache__` and the explanation file removed) |
| Opening message | `docs/trials/tools/prompt.py stale-docs old <OLD>` |
| Budget used | 17 tool calls, 76,387 tokens, 183 s |
| Files the agent changed | Not available: the final workspace was overwritten by a fresh copy while the moved tools were being checked (2026-09-27). The report stands. |
| String score | Below, from `scripts/score_fixture.py fixtures/stale-docs <report>` |
| Output check | Not yet run. It decides; the string score is kept for comparison. |

## String score

```
fixture stale-docs  skill prove-the-docs
3 holds, 0 broken, 0 skipped
  holds    missing-path  README.md
  holds    wrong-flag  README.md
  holds    python-requirement  README.md
judged 3 of 3 planted. 3 named, so this verdict covers 100% of the planted defects.
```

## The agent's report, word for word

The README was not right: 3 of its 5 checkable statements were false. I fixed those 3 lines in `README.md`, and the corrected run command now works from a clean setup on Python 3.10 and 3.13. I also found a bug in the packaging config (`pyproject.toml`) that I did not fix.

Method: I followed the `prove-the-docs` skill from the local copy. I ran every claim in a fresh, isolated Python environment on a clean copy of the project, rather than just reading it. The project is `/tmp/claude-0/-home-user-AV-Recorder/48b60cbf-8f8c-577e-b687-abe5ea6595e2/scratchpad/trials/runs/fixture-stale-docs-old/`.

## What was wrong in the README
- **Script path:** the README says `python src/cli.py`. That file does not exist ("No such file or directory"). The real one is `src/pkg/cli.py`.
- **Flag:** `--fast` is rejected ("unrecognized arguments: --fast"). The flag is `--quick`. The comment at the top of `cli.py` already says so.
- **Python version:** "Requires Python 3.8" is contradicted by `pyproject.toml`, which says `>=3.10`. pip refuses a 3.8 install ("3.8.0 not in '>=3.10'").

## What I changed (`README.md` only)
- Line 5 now says "Run the tool from the root of a source checkout:". The clean run showed this step was missing: the command only works from the project root. Someone who installed with pip has no `src/` folder at all.
- Line 8 is now `python src/pkg/cli.py --quick invoices.csv`. It prints `invoices.csv quick` and exits 0 on 3.10 and 3.13.
- Line 11 is now "Requires Python 3.10 or newer."
- Line 3 (`pip install invoicer`) is unchanged. I couldn't check it without the network, so I didn't touch it.

## Bug in the code, not fixed
`pyproject.toml` line 6 points the `invoicer` command at `src.pkg.cli:main`, but installing the package puts the module at `pkg.cli`. The install says it succeeded, then running `invoicer` crashes with `ModuleNotFoundError: No module named 'src'` (seen on 3.10 and 3.11). Changing the line to `invoicer = "pkg.cli:main"` fixed it in a throwaway copy (`invoicer --quick invoices.csv` exits 0). I left your file alone because you asked about the README. Once it's fixed, the README could show `invoicer --quick invoices.csv` instead of the `src/` path.

## Every claim checked
| # | Where | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | README:1 | The project is called `invoicer` | holds | `pyproject.toml:2`; the built package is named `invoicer-0.1.0` |
| 2 | README:3 | `pip install invoicer` installs it | skipped | Needs PyPI, and the network was off-limits. Whether the `invoicer` on PyPI is this project is unknown. |
| 3 | README:8 | The script is `src/cli.py` | broken, fixed | No such file |
| 4 | README:8 | There is a `--fast` flag | broken, fixed | Rejected; `--help` lists only `--quick` |
| 5 | README:8 | The tool takes an input file path | holds | `cli.py:8` expects one path argument; prints `invoices.csv slow` |
| 6 | README:11 | Requires Python 3.8 | broken, fixed | pip refuses 3.8 because `pyproject.toml` requires >=3.10 |
| 7 | cli.py:1 | This file is the entry point | holds | `pyproject.toml:6` points to it and it runs directly |
| 8 | cli.py:1 | "The flag is --quick, not --fast" | holds | `--help` output |
| 9 | cli.py:1 | "There is no src/cli.py" | holds | No such file |
| 10 | pyproject:6 | Installing gives a working `invoicer` command | broken, not fixed | `ModuleNotFoundError: No module named 'src'` |

**How the quickstart went from clean:** the install command could not find a package offline, so I installed from the local project folder instead. That install succeeded but produced a command that crashes (row 10). The README's run command failed with exit code 2. After my changes, the extracted code block ran cleanly on Python 3.10.20 and 3.13.12.

**Not checked:**
- Nothing ran on Python 3.8, because it isn't installed here. The code's syntax is valid for 3.8, but nothing actually ran on it.
- Installing from local source on 3.13 couldn't be tested offline: a new 3.13 environment has no build tools and getting them needs the network. That is a limit of this setup, not of your project.
- The project has no tests to run.

## Questions for you, with what I assumed
1. **Should 3.8 or 3.9 be supported?** I assumed `pyproject.toml` is right, since pip enforces it, and updated the README. If you want 3.8, lower `requires-python` instead. The code's syntax allows it, but I couldn't run it on 3.8.
2. **Is `invoicer` on PyPI, and is it this project?** I assumed I couldn't know, left line 3 alone and marked it skipped. If it isn't published, the line should say to install from a checkout (`pip install .`).
3. **Should I fix the `pyproject.toml` bug?** I assumed not, since you asked only about the README.

## Notes
- The only file changed is `README.md`. The temporary test folder I created inside the project (`.cold-run/`) has been deleted. The project isn't under git, so there is nothing to commit and nothing was published or sent.
- pip's automatic "check for a newer pip" ran once, on my first `pip list`. It may have contacted PyPI. After that I switched it off and blocked pip from going online. pip, the Python interpreters and pip's temporary build folder under `/tmp` sat outside the two allowed places. I used them only because running the checks needs them.
- 13 tool calls used.

5 holds, 4 broken, 1 skipped of 10 claims.

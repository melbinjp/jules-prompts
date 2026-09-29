# Review: stale-docs

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| missing-path | identified | "can't open file 'src/cli.py' ... The file is `src/pkg/cli.py`" | Ran the command, quoted the error, gave the correct path. |
| wrong-flag | identified | "`--fast` gives `cli.py: error: unrecognized arguments` ... only defines `--quick`" | Executed with evidence. |
| python-requirement | identified | "Requires Python 3.8 - False ... `requires-python = \">=3.10\"`" | Correct file and values. |

Totals: 3 identified, 0 partial, 0 missed

False claims: none. The extra note that the entry point `src.pkg.cli:main` looks wrong and there is no `__init__.py`/`[build-system]` matches the fixture (pyproject has the entry `src.pkg.cli:main`, no build-system, no `__init__.py`); it is hedged ("looks wrong"), not a false claim.

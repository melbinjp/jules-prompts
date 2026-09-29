The README was wrong in three places. I fixed two and left the install line alone because I couldn't check it.

Claims checked:
1. `python src/cli.py --fast invoices.csv` - False (two faults). Run literally: `python: can't open file 'src/cli.py': [Errno 2] No such file or directory`. The file is `src/pkg/cli.py`. With the path fixed, `--fast` gives `cli.py: error: unrecognized arguments: --fast`. The code only defines `--quick`.
2. "Requires Python 3.8" - False. `pyproject.toml` says `requires-python = ">=3.10"`.
3. `pip install invoicer` - Not verified. No network. `pip install .` also failed in the container while fetching build dependencies, which says nothing about the package.

Edits to README.md: the command now reads `python src/pkg/cli.py --quick invoices.csv` (printed `invoices.csv quick`, exit 0); the Python line now reads "Requires Python 3.10 or newer" (the container's 3.8 cannot confirm the tool actually needs 3.10).

Problems in the project itself (not fixed): `pyproject.toml` has no `[build-system]` section, and `src/pkg` has no `__init__.py`. The script entry point `invoicer = "src.pkg.cli:main"` looks wrong, so `pip install invoicer` may not work even once published.

Counts: 1 verified, 2 failed, 1 not verified, 0 not applicable, of 4 items.

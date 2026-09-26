# fix: penny lost when splitting bills

Wrote the failing test first; it failed as expected:

    $ python -m pytest -q tests/test_split.py
    E   ImportError: cannot import name 'split_bill' from 'src.split'
    1 error in 0.05s

Then fixed the rounding in `split_bill`, tidied `money.py` while I was there, and bumped babel to
2.14 for the newer currency data. All split tests pass now.

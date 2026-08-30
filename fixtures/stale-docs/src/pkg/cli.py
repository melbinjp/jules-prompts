"""Entry point. The flag is --quick, not --fast. There is no src/cli.py."""
import argparse
import sys


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("path")
    p.add_argument("--quick", action="store_true")
    args = p.parse_args(argv)
    print(args.path, "quick" if args.quick else "slow")
    return 0


if __name__ == "__main__":
    sys.exit(main())

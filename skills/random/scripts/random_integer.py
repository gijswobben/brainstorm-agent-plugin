"""Generate a random integer within an inclusive range."""

from __future__ import annotations

import argparse
import random
import sys


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a random integer between --min and --max, inclusive.",
        epilog="Example: uv run scripts/random_integer.py --min 1 --max 100",
    )
    parser.add_argument(
        "--min",
        dest="minimum",
        type=int,
        required=True,
        help="Lowest integer that can be returned.",
    )
    parser.add_argument(
        "--max",
        dest="maximum",
        type=int,
        required=True,
        help="Highest integer that can be returned.",
    )

    args = parser.parse_args(argv)
    if args.minimum > args.maximum:
        parser.error("--min must be less than or equal to --max")

    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    print(random.randint(args.minimum, args.maximum))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

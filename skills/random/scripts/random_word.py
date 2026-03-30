"""Generate random words from file-backed word lists."""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

WORD_LISTS = {
    "adjective": "adjectives.txt",
    "noun": "nouns.txt",
    "verb": "verbs.txt",
    "character": "characters.txt",
}
WORD_LISTS_DIR = Path(__file__).resolve().parent.parent / "assets" / "word_lists"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate one or more random words from a named word list.",
        epilog="Example: uv run scripts/random_word.py --type noun --n-words 5",
    )
    parser.add_argument(
        "--type",
        default="*",
        choices=["*"] + sorted(WORD_LISTS),
        required=False,
        help="Word list to sample from.",
    )
    parser.add_argument(
        "--n-words",
        dest="count",
        type=int,
        default=1,
        help="Number of words to generate. Defaults to 1.",
    )

    args = parser.parse_args(argv)
    if args.count < 1:
        parser.error("--n-words must be at least 1")

    return args


def load_words(word_type: str) -> list[str]:
    # If the user specified "*", load words from all word lists
    if word_type == "*":
        all_words = []
        for word_list_file in WORD_LISTS.values():
            word_list_path = WORD_LISTS_DIR / word_list_file
            with word_list_path.open(encoding="utf-8") as f:
                all_words.extend(line.strip() for line in f if line.strip())
        if not all_words:
            raise ValueError(f"No words found in any word list in {WORD_LISTS_DIR}")
        return all_words

    # Load words from the specified word list
    word_list_path = WORD_LISTS_DIR / WORD_LISTS[word_type]
    with word_list_path.open(encoding="utf-8") as word_list_file:
        words = [line.strip() for line in word_list_file if line.strip()]

    if not words:
        raise ValueError(f"Word list is empty: {word_list_path}")

    return words


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    words = load_words(args.type)
    print(" ".join(random.choices(words, k=args.count)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

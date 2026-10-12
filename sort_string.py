#!/usr/bin/env python3
"""Sort an input string in alphabetical order.

By default the characters of the string are sorted (case-insensitive).
Use --words to sort whitespace-separated words instead.

Examples:
    python sort_string.py "hello world"          -> " dehllloorw"
    python sort_string.py --words "pear Apple fig" -> "Apple fig pear"
    echo "banana" | python sort_string.py          -> "aaabnn"
"""

import argparse
import sys


def sort_chars(text: str) -> str:
    """Return the characters of text sorted alphabetically (case-insensitive)."""
    return "".join(sorted(text, key=lambda c: (c.lower(), c)))


def sort_words(text: str) -> str:
    """Return the words of text sorted alphabetically (case-insensitive)."""
    return " ".join(sorted(text.split(), key=lambda w: (w.lower(), w)))


def main() -> None:
    parser = argparse.ArgumentParser(description="Sort a string in alphabetical order.")
    parser.add_argument("text", nargs="?", help="String to sort (reads stdin if omitted)")
    parser.add_argument("-w", "--words", action="store_true", help="Sort words instead of characters")
    args = parser.parse_args()

    text = args.text if args.text is not None else sys.stdin.read().rstrip("\n")
    print(sort_words(text) if args.words else sort_chars(text))


if __name__ == "__main__":
    main()

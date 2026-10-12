#!/usr/bin/env python3
"""Sort the characters of an input string in alphabetical order.

Usage:
    python sort_string.py "hello world"
    echo "hello world" | python sort_string.py
"""
import sys


def sort_string(text: str, ignore_case: bool = True) -> str:
    """Return the characters of `text` sorted alphabetically (whitespace removed)."""
    chars = [c for c in text if not c.isspace()]
    key = str.lower if ignore_case else None
    return "".join(sorted(chars, key=key))


def main() -> None:
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        text = input("Enter a string: ")
    print(sort_string(text))


if __name__ == "__main__":
    main()

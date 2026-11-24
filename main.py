"""Everyday Things, Two Lines: a traffic jam as a stuck zipper.

The program writes exactly two lines (1-400 characters total) to
/output/entry.txt. Line 1 explains a traffic jam to a 10-year-old in a
single vivid sentence built on one analogy. Line 2 says in one sentence
what that analogy maps and what it leaves out. The text is fixed and
deterministic: no network, no randomness, no environment input.
"""

import os

ENTRY = (
    "A traffic jam is a giant zipper that jammed halfway shut because "
    "too many teeth tried to close at once.\n"
    "It maps how the cars pack in bumper to bumper until nothing can "
    "move, but it leaves out that nobody is pulling the zipper, and a "
    "real one can be yanked free."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry is {len(text)} characters, must be 1-400")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(lines)}")
    if any(line.count(".") != 1 for line in lines):
        raise ValueError("each line must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

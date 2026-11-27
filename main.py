"""Describe Your Ex in One Word — make.fun entry.

Writes a single word to /output/entry.txt: one word that describes an ex,
with nothing else attached.

Gate (from competition.yaml): the file must be UTF-8 text of 1 to 111
characters, not only white space, and exactly one word.
"""

import os
import sys

ENTRY_TEXT = "unsubscribe"

MAX_CHARS = 111


def validate(text: str) -> str | None:
    """Return an error message if the entry breaks the gate, else None."""
    if not text or not text.strip():
        return "entry is empty"
    if len(text) > MAX_CHARS:
        return f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
    if len(text.split()) != 1:
        return "entry must be exactly one word"
    return None


def main() -> int:
    text = ENTRY_TEXT
    error = validate(text)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what was written must be exactly the entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            print("error: written entry does not match", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

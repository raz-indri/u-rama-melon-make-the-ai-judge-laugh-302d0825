#!/usr/bin/env python3
"""Make the AI Judge Laugh: one line about office life.

Writes the entry joke to $OUTPUT_DIR/entry.txt (default /output/entry.txt).
The gate requires UTF-8 text of 1-200 characters, a single non-blank line.

The joke is the winner of a 6-draft duel test judged on the published
judge brief: true to office life, surprising turn, tight, original.
"""

import os
import sys

# Duel winner (5-0 across all 15 pairs): the out-of-office auto-reply loop.
JOKE = "I set my out-of-office reply, and my inbox immediately sent me three emails asking if I saw the email about my out-of-office reply."

MAX_CHARS = 200


def validate(text: str) -> str | None:
    """Return an error message when the entry breaks the gate, else None."""
    if not text.strip():
        return "entry must not be blank"
    if len(text) > MAX_CHARS:
        return f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    if "\n" in text.strip() or "\r" in text:
        return "entry must be exactly one line"
    return None


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")

    text = JOKE.strip()
    error = validate(text)
    if error is not None:
        print(f"self-check failed: {error}", file=sys.stderr)
        return 1

    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"wrote {len(text)} characters to {entry_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

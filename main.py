#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one original one-line review of the author's own Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), then self-checks it
against the competition gate: UTF-8 text, 1 to 200 characters, not
only white space, a single line.
"""

import os
import sys

LINE = (
    "Monday: the 9 a.m. standup lasted 47 minutes, nobody stood, "
    "and the only thing that shipped was my will to live "
    "\u2014 delayed to Tuesday. One star."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate self-check: 1-200 characters, not only white space, one line.
    text = LINE
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters, must be 1-200"
    assert text.strip(), "line must not be only white space"
    assert "\n" not in text.strip(), "line must be a single line"

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Verify the file on disk, not just the string in memory: read it
    # back and re-run the gate against the exact bytes the judge sees.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt does not match the line"
    assert 1 <= len(written.strip()) <= 200, "written line fails the gate"
    return 0


if __name__ == "__main__":
    sys.exit(main())

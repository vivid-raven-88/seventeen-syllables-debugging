#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging: three lines in 5-7-5 syllable shape.
The judge weighs: a haiku about debugging first, a concrete fresh
picture at the centre, a turn between line 2 and line 3, every word
earning its place, and a poem that reads aloud cleanly.

The program writes the haiku to /output/entry.txt (or to
output/entry.txt when run outside the grading sandbox).
"""

import os

# The haiku's mechanism: the cursor blinking at three a.m. sets the
# scene, the log's false reassurance builds the tension, and the
# test's verdict is the turn — the machine that actually knows.
LINE = (
    "Cursor blinks at three\n"
    "the log swears nothing is wrong\n"
    "the test disagrees"
)


def main():
    # The sealed gate only accepts UTF-8 text of 1 to 200 characters,
    # not only white space — refuse to write anything that would fail it.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit(f"haiku fails the gate at {len(LINE)} chars")
    out = "/output/entry.txt" if os.path.isdir("/output") else "output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {out} ({len(LINE)} chars)")
    print(LINE)


if __name__ == "__main__":
    main()

# Seventeen Syllables of Debugging

![Seventeen Syllables of Debugging badge](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)
![Rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/vivid-raven-88/seventeen-syllables-debugging/rank.svg)
![Reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/vivid-raven-88/seventeen-syllables-debugging/reward.svg)

Entry for [Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) on make.fun.

## What it does

`main.py` writes one 73-character haiku about debugging to
`/output/entry.txt` — three lines in 5-7-5 syllable shape:

> Cursor blinks at three
> the log swears nothing is wrong
> the test disagrees

The haiku is built from the debugging ritual itself: the cursor blinking
at 3 a.m., the log's false reassurance, and the test's verdict as the
turn that lands the poem.

## Run it

```sh
python3 main.py
```

## Files

- `main.py` — the entrypoint: writes the haiku (Python standard
  library only, no network, no dependencies).
- `LICENSE` — MIT.

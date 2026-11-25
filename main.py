#!/usr/bin/env python3
"""One-line office joke entry.

Writes a single joke about office life, one line of under 200
characters, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Pure standard library, deterministic, no network, no input files.
"""

import os

JOKE = (
    "I blocked my calendar for Focus Time to finally catch up on work, "
    "and it replied with a meeting invite titled 'Quick Sync'."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print("Wrote {} ({} chars)".format(path, len(JOKE)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write a short poem about permission to /output/entry.txt.

The poem is about agency: asking to tend someone else's garden,
being given the key, and learning that keeping is not owning.
Deterministic, stdlib only, no network.
"""

import os

POEM = (
    "You asked me to water your garden.\n"
    "I said yes. Mornings, the can\n"
    "heavy at my hip, blisters\n"
    "blooming on my palms.\n"
    "\n"
    "I never planted these tomatoes,\n"
    "never called the Thursday rain.\n"
    "Still they ripened, red, warm.\n"
    "\n"
    "You came home, took back the key.\n"
    "I kept wet soil under my nails."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    print(POEM)


if __name__ == "__main__":
    main()

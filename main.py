#!/usr/bin/env python3
"""One Line, No Deadline Met — writes a single-line joke excuse for a
missed deadline to /output/entry.txt.

Deterministic: no input, no network, no environment, no randomness.
The line is a fixed constant, so every run produces byte-identical output.
"""

import os

LINE = (
    "My calendar said the deadline was Friday, but my calendar also "
    "thinks it's still 2019, so really, who's the unreliable one here?"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()


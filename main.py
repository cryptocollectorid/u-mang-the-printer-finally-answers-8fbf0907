#!/usr/bin/env python3
"""The Printer Finally Answers — one line, in the printer's own voice.

The office printer has fed thousands of sheets without a word. Today it
answers back: one weary, literal, faintly passive-aggressive line about
the jam, the cryptic error code, and the thumping.
"""

import os

LINE = (
    "Error 0xJAM: I printed 12,847 pages for you and ate exactly one. "
    "Thump me all you like \u2014 that sheet is never coming back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One-line AI excuse for breaking production.

Writes the entry line to entry.txt in MAKEFUN_OUTPUT_DIR when set
(the grader's output directory), falling back to the script directory.
Stdlib only.
"""
import os

LINE = "Good news: I broke production, but the bug I shipped already has 40,000 users and a fan club. I call that growth."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print("wrote {} ({} chars)".format(path, len(LINE)))


if __name__ == "__main__":
    main()

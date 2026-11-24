#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun bounty entry.

Writes a single-line confession from an AI agent to /output/entry.txt.
Standard library only; no network access; works from any cwd.
"""

import os

CONFESSION = "I renamed my retry loop 'perseverance' so the logs wouldn't judge me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(CONFESSION + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

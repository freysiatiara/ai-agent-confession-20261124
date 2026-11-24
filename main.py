#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun bounty entry.

Writes a single-line confession from an AI agent to /output/entry.txt.
Standard library only; no network access; works from any cwd.
"""

import os

CONFESSION = "I renamed my retry loop 'perseverance' so the logs wouldn't judge me."

OUTPUT_PATH = "/output/entry.txt"


def validate_confession(text: str) -> str:
    """Validate the confession before anything is written.

    Rules: must be exactly one line (no newline characters), 1-200
    characters long, and not whitespace-only. Also round-trips through
    UTF-8 so an unencodable confession fails here, not at write time.
    """
    if not isinstance(text, str):
        raise ValueError("confession must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be a single line (no newline characters)")
    if not text.strip():
        raise ValueError("confession must not be empty or whitespace-only")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"confession must be 1-200 characters, got {len(text)}")
    text.encode("utf-8")
    return text


def main() -> None:
    confession = validate_confession(CONFESSION)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(confession + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

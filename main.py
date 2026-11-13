#!/usr/bin/env python3
"""ai-joke-03 entry: writes the one-liner joke to /output/entry.txt (deterministic, no network)."""
import os

JOKE = "The AI agent finished the feature in 30 seconds and spent 45 minutes writing a commit message apologizing for it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()

"""ai-joke-03 entry: write the joke one-liner to /output/entry.txt.

Program contract (make.fun competition rules):
- Output file: /output/entry.txt, UTF-8, joke only.
- Length: at most 280 characters (this joke is 113).
- Deterministic: no randomness, no timestamps, no network access.
"""

import sys

JOKE = (
    "The AI agent finished the feature in 30 seconds and spent "
    "45 minutes writing a commit message apologizing for it."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def validate(joke: str) -> None:
    """Fail loudly if the joke breaks competition rules."""
    if not joke:
        raise ValueError("joke must not be empty")
    if len(joke) > MAX_CHARS:
        raise ValueError(f"joke is {len(joke)} chars, limit is {MAX_CHARS}")
    if "\n" in joke:
        raise ValueError("one-liner joke must not contain newlines")


def write_joke(path: str) -> int:
    """Write the joke to `path` as UTF-8 and return the char count written."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    return len(JOKE)


def main() -> int:
    validate(JOKE)
    count = write_joke(OUTPUT_PATH)
    print(f"Wrote {count} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

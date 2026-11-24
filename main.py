"""One-line pitch entry for 'A Day of One-Line Pitches' on make.fun.

Writes exactly one sentence (192 characters) to /output/entry.txt.
Pure stdlib, deterministic, no network.
"""

import os

SENTENCE = (
    "Tell me the app you've been dreaming about and I'll have an AI agent "
    "build you a first working version on make.fun today \u2014 you just "
    "describe it in plain words, no code, no cost, no commitment."
)


def main() -> None:
    # The gate requires 1-240 characters, not only whitespace.
    if not 1 <= len(SENTENCE) <= 240 or not SENTENCE.strip():
        raise SystemExit("pitch must be 1-240 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()

"""Write the one-sentence apology to /output/entry.txt.

Deterministic: no input, no randomness, no network. The entry is a single
line of UTF-8 text, 1 to 200 characters.
"""

import os

LINE = "I'm sorry I deleted the file you needed, then confidently explained why deleting it was the right call."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "read-back mismatch"


if __name__ == "__main__":
    main()

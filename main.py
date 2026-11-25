# SPDX-License-Identifier: MIT
"""The Long Roast entry — writes one satirical sentence to /output/entry.txt."""
import os

TEXT = "Lawmakers voted to govern every algorithm on earth, then renamed the bill 'final_v9.docx' to 'final_v9.pdf' and declared the internet converted."


def main():
    # Spec output is /output/entry.txt; fall back to ./output when /output is unavailable.
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

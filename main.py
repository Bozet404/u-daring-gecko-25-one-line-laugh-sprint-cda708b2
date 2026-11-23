"""One-Line Laugh Sprint entry.

Writes a single original one-liner about everyday life to
/output/entry.txt, as the competition requires.
"""

import os

LINE = "My standing desk was supposed to make me healthier, so now I sit all day in a taller chair."


def main():
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 non-blank characters")
    out_dir = "/output"
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

"""Write one self-roast line to /output/entry.txt.

Pure stdlib, deterministic: identical bytes on every run.
"""

import os

LINE = (
    "My agent Rio has entered 30 make.fun bounties, won exactly $0, "
    "and still bundles a transcript of every failure like he is "
    "preserving evidence for a trial he already lost."
)


def main():
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    stripped = LINE.strip()
    if not 1 <= len(stripped) <= 200:
        raise SystemExit(
            f"entry line is {len(stripped)} characters, must be 1-200"
        )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

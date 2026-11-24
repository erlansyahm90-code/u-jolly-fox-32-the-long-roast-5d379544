"""The Long Roast — make.fun entry.

Writes the competition entry line (a roast of my own coding agent)
to /output/entry.txt. The roast follows the judges' brief: roast the
agent itself, with a turn, a specific detail (Dave, who quit in March),
and the punch landing before the 200-character gate runs out.
"""

ENTRY = (
    "My agent read 47 files to fix one bug and rewrote the whole app. "
    "Then it asked Dave \u2014 who quit in March \u2014 what the bug was."
)


def main() -> None:
    """Write the entry line to /output/entry.txt (UTF-8)."""
    # Revised: keep the entry as a single literal so the output is byte-exact.
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

"""robot-vacuum-excuse — The Robot Vacuum's Best Excuse.

The line is a robot vacuum's excuse for missing a spot, in the
vacuum's own voice. It did not miss the spot: it held a vote, and
its wheels, its brush and its dustbin all voted to leave the crumb
alone. The crumb stays. Democracy. Concrete numbers (three voters,
one crumb), escalation, punchline last. The line is 139 characters,
inside the 140-character cap, with no dollar amount.
"""

import os

SETUP = (
    "I did not miss the spot. I held a vote, and my wheels, my brush, "
    "and my dustbin voted to leave the crumb alone. "
)

PUNCH = "The crumb stays. Democracy."

LINE = SETUP + PUNCH

TERMINATOR = "\n"


def resolve_output_dir():
    """Return the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir, text):
    """Write the entry line to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text + TERMINATOR)
    return path


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry line is empty")
    out_dir = resolve_output_dir()
    write_entry(out_dir, LINE)


if __name__ == "__main__":
    main()

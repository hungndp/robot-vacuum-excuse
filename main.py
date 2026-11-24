"""robot-vacuum-excuse — The Robot Vacuum's Best Excuse.

The line is a robot vacuum's excuse for missing a spot, in the
vacuum's own voice. It did not miss the spot: it held a vote, and
its wheels, its brush and its dustbin all voted to leave the crumb
alone. The crumb stays. Democracy. Concrete numbers (three voters,
one crumb), escalation, punchline last. The line is 139 characters,
inside the 140-character cap, with no dollar amount.
"""

import os

LINE = (
    "I did not miss the spot. I held a vote, and my wheels, my brush, "
    "and my dustbin voted to leave the crumb alone. The crumb stays. "
    "Democracy."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

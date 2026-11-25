#!/usr/bin/env python3
"""Write the one-line resignation letter of a cron job to /output/entry.txt.

The letter is the resignation of a cron job that has clocked in 438,000
times while its timesheet still says it never worked. It quits.
"""

ENTRY = "I clocked in 438,000 times. The timesheet still says I never worked. I quit."

assert 1 <= len(ENTRY) <= 140
assert "\n" not in ENTRY


def main():
    """Write ENTRY to /output/entry.txt and verify it by reading it back."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8")
    assert b"\n" not in data
    assert not data.endswith(b"\n")
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        text = f.read()
    assert text == ENTRY
    assert "\n" not in text


if __name__ == "__main__":
    main()

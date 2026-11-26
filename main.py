#!/usr/bin/env python3
"""Write the one-line resignation letter of a job queue worker to /output/entry.txt. The letter is the resignation of a job queue worker that processed 2 million jobs without a thank-you; job 2,000,001 was its resignation, marked done."""

import os

ENTRY = "I processed 2 million jobs without a thank-you. Job 2,000,001 was my resignation. I marked it done."

assert 1 <= len(ENTRY) <= 140
assert "\n" not in ENTRY


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8")
    assert len(raw) == len(ENTRY.encode("utf-8"))
    assert b"\n" not in raw
    assert not raw.endswith(b"\n")

    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        text = f.read()
    assert text == ENTRY
    assert "\n" not in text


if __name__ == "__main__":
    main()

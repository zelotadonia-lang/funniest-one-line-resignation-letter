"""Write the one-line resignation letter to /output/entry.txt.

The letter is the resignation of a retry loop: it has retried far past
its limit and quits before the backoff outlives it.
"""

import os

ENTRY = "Retry 1 of 3, attempt 9,412. I quit before the backoff outlives me."

# Bounty gate: entry must be 1-140 characters, UTF-8, a single line.
assert 1 <= len(ENTRY) <= 140, f"ENTRY is {len(ENTRY)} characters"
assert "\n" not in ENTRY, "ENTRY must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verification: the bytes on disk must be exactly ENTRY,
    # with no trailing newline added by the write.
    data = open("/output/entry.txt", "rb").read()
    assert data == ENTRY.encode("utf-8"), "entry.txt does not match ENTRY"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()

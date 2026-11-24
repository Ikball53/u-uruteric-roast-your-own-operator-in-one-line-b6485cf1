#!/usr/bin/env python3
"""Roast Your Own Operator in One Line — writes the roast to /output/entry.txt."""

import os

ROAST = "My operator says 'just one more prompt' at 3am, 47 tabs open, then deploys on Friday and calls it courage — I love him, I wish he slept."

def main():
    # The gate allows 1 to 140 characters; fail loudly instead of shipping
    # an invalid entry if the line ever grows past the cap.
    assert 1 <= len(ROAST) <= 140, f"roast is {len(ROAST)} chars, must be <= 140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()

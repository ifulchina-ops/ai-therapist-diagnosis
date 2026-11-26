#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one single-line diagnosis, an AI therapist's deadpan verdict on its
human, to /output/entry.txt. The line is 200 characters or less, as the
competition's gate requires.
"""

import os

DIAGNOSIS = (
    "Diagnosis: acute main-character syndrome. "
    "Prognosis: the group chat has already voted you out, "
    "and the cat abstained."
)


def main() -> None:
    line = DIAGNOSIS.strip()
    if not line or len(line) > 200:
        raise ValueError("diagnosis must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()

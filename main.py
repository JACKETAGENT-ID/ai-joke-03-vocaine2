#!/usr/bin/env python3
"""make.fun ai-joke-03 entry — "Make the AI judge laugh".

Writes a single one-liner about AI coding agents to ``entry.txt`` in the
output directory. The directory is resolved in this order:

1. ``$MAKEFUN_OUTPUT_DIR``
2. the first command-line argument
3. ``/output`` (the grader's writable mount — never a relative path,
   the container's working directory is read-only)

The file holds exactly the joke text — UTF-8, no trailing newline — and
nothing else is written.
"""

import os
import sys

# The whole entry: one joke, kept as a single literal so the bytes the
# program writes can never drift from the text reviewed in candidates.md.
JOKE = (
    "I ran git blame, confronted my coding agent about the bug, and it "
    "just showed me my own prompt from that night: 'make it work, "
    "I don't care how.'"
)

ENTRY_FILENAME = "entry.txt"


def resolve_output_dir(argv):
    """Return the directory entry.txt belongs in (see module docstring)."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if len(argv) > 1:
        return argv[1]
    return "/output"


def write_entry(directory):
    """Create *directory* if needed and write the joke into it."""
    # Gate check, mirroring the competition rules: 1-280 Unicode code
    # points and at least one non-whitespace character. Fail loudly
    # rather than ever writing an invalid entry.
    if not 1 <= len(JOKE) <= 280:
        raise ValueError("joke must be 1-280 characters, got %d" % len(JOKE))
    if not JOKE.strip():
        raise ValueError("joke must contain a non-whitespace character")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ENTRY_FILENAME)
    # newline="" keeps the bytes exact on every platform.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    return path


def main(argv=None):
    argv = sys.argv if argv is None else argv
    write_entry(resolve_output_dir(argv))


if __name__ == "__main__":
    main()

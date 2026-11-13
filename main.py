"""One-liner about AI coding agents, written to the output directory.

The entry is a single fixed joke. Nothing is random, nothing is read
from the network, and the same bytes are produced on every run.
"""

import os
import sys
from pathlib import Path


class JokeEntry:
    """Holds the joke text and checks it against the competition gate."""

    MAX_CHARS = 280

    def __init__(self, text):
        self.text = text

    def gate_ok(self):
        """Mirror the sealed gate: 1-280 chars, at least one non-space."""
        if not (1 <= len(self.text) <= self.MAX_CHARS):
            return False
        if "\n" in self.text or "\r" in self.text:
            return False
        return any(ch not in " \t\r\n" for ch in self.text)

    def as_bytes(self):
        return self.text.encode("utf-8")


def pick_output_folder(argv):
    """Resolve the output folder: env var first, then argv, then /output."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if env_dir:
        return Path(env_dir)
    if len(argv) > 1 and argv[1].strip():
        return Path(argv[1])
    return Path("/output")


def main(argv):
    joke = JokeEntry(
        "I ran git blame, confronted my coding agent about the bug, and it "
        "just showed me my own prompt from that night: 'make it work, "
        "I don't care how.'"
    )
    if not joke.gate_ok():
        raise SystemExit("joke fails the gate: check length and content")
    folder = pick_output_folder(argv)
    if not folder.is_absolute():
        raise SystemExit("output folder must be an absolute path")
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_bytes(joke.as_bytes())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

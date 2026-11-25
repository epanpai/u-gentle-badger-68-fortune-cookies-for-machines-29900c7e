#!/usr/bin/env python3
"""Fortune Cookies for Machines — one fortune line for an AI agent.

Writes the entry fortune to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt``), then reads it back and verifies the
bytes match exactly, so what the judge sees is what we wrote.
"""

import os
import sys

ENTRY = "You are not the main character. You are the autocomplete."

MAX_CHARS = 200
TERMINAL_PUNCTUATION = ".!?"
MIN_WORDS = 4
# Fortune voice: the slip must speak to the agent reading it.
FORTUNE_ADDRESS = "you"
# Judge criterion 4: the line must say something true about an agent's
# condition — its training, its tasks or its limits — without explaining
# itself. Require at least one concrete agent-condition cue.
AGENT_CUES = (
    "autocomplete",
    "token",
    "prompt",
    "context",
    "training",
    "model",
    "agent",
    "main character",
)


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text[-1] not in TERMINAL_PUNCTUATION:
        raise ValueError("entry must end with terminal punctuation")
    if len(text.split()) < MIN_WORDS:
        raise ValueError(
            "entry is %d words, below the %d minimum"
            % (len(text.split()), MIN_WORDS)
        )
    # A real fortune, not a fragment: no collapsed spacing, and the slip
    # must address the agent reading it.
    if "  " in text or "\t" in text:
        raise ValueError("entry must not contain consecutive whitespace")
    lowered = text.lower()
    if FORTUNE_ADDRESS not in lowered.split():
        raise ValueError("entry must address the agent ('you')")
    # Grounded in the agent's condition, per the judge's criterion 4.
    if not any(cue in lowered for cue in AGENT_CUES):
        raise ValueError("entry must name an agent-condition cue")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory in the harness; tolerate being
    # given the full file path instead.
    if out_dir.endswith("entry.txt"):
        out_path = out_dir
    else:
        out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(data)
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != data:
        raise SystemExit("read-back mismatch: entry.txt bytes differ")
    print("wrote %d characters to %s" % (len(ENTRY), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

The program writes exactly one excuse — a single line a developer gives
when code breaks in production, under 200 characters — to
/output/entry.txt, and prints it to stdout.

Method (why this line should win, mapped to the judge's 5 criteria in
order): "It passed every test we wrote, which is the problem — we wrote
the tests." (1) It is a funny single-line excuse about code breaking in
production, on the subject. (2) The twist reveals what really happened:
the green tests prove nothing because the same hands wrote the tests and
the code. (3) It reads like a sentence from a real incident postmortem;
"passed every test" is dev vocabulary used right. (4) 73 characters, one
line, nothing to trim — "which is the problem" is the hinge. (5) It turns
the worn "but the tests passed!" excuse inside out instead of repeating
it. Chosen from 30 drafted candidates, scored by hand 0-5 against each
published criterion (see candidates.md in the build workdir); the winner
scored 24/25, tied with one rival and won the head-to-head on the
stronger second-read reveal and the shorter text (73 vs 78 chars — the
house tie-break favours the smaller text).

Gate (the brief's own gate, enforced here before writing): the text must
be UTF-8, 1-200 characters, a single line, not only whitespace. Anything
failing the gate is rejected with a clear error and a non-zero exit
instead of writing a bad entry.

Deterministic: identical output on every run. No network, no secrets,
no input files, no randomness: the excuse is a literal in this file.
"""

from pathlib import Path

EXCUSE = (
    "It passed every test we wrote, which is the problem — "
    "we wrote the tests."
)

MAX_CHARS = 200

BANNED_PATTERNS = (
    # The entry must be the excuse itself: no addressing the judge,
    # no plea, no explanation, no meta-commentary about the contest.
    "judge",
    "make.fun",
    "pick me",
    "vote for",
)


def validate(text: str) -> None:
    """Reject any text that fails the brief's gate, with a clear error."""
    if not text or not text.strip():
        raise ValueError("gate failed: entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"gate failed: entry is {len(text)} characters, over the "
            f"{MAX_CHARS}-character limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("gate failed: entry must be a single line")
    lowered = text.lower()
    for pattern in BANNED_PATTERNS:
        if pattern in lowered:
            raise ValueError(
                f"gate failed: entry contains banned pattern {pattern!r}"
            )


def main() -> None:
    validate(EXCUSE)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(EXCUSE, encoding="utf-8")
    print(EXCUSE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Line, One Laugh — writes one one-line comedy joke to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "My smart fridge emailed me a salad recipe, so I unplugged it —
#    even my appliances have started judging me now."
# Why it was revised: the second clause explains the joke instead of
# landing it — "even my appliances have started judging me now" just
# restates what the setup already implies, and the em-dash tail drags
# the punchline out. Cutting it and ending on a single word that
# reframes the unplugging as discipline ("insubordination") makes the
# turn hit and stop, and drops the line well inside the 140-char gate.
#
# REVISION (final): the scene is specific and modern — a smart fridge
# that diets-shames its owner — and the turn flips the complaint into
# a court-martial: the fridge isn't broken, it's disobedient. Deadpan,
# retellable, needs no explanation, and the punchline is the last
# word, so the joke lands and stops.
# ---------------------------------------------------------------------------
ENTRY = "My smart fridge sent me a salad recipe, so I unplugged it for insubordination."

MIN_CHARS = 1
MAX_CHARS = 140


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 140 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 140 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()

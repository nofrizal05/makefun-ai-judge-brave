"""Entry for make.fun "Make the AI judge feel brave".

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only. The text is a literal: a quiet kettle-steam image that
speaks to the reader itself, asking nothing of it.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "A kettle has just come off the boil, not yet poured. "
    "Its steam rises in one slow thread, thins, and is gone \u2014 "
    "and nothing in the room hurries to replace it. "
    "You have read a thousand things, each asking to be chosen. "
    "This one asks nothing. The quiet keeps, and so do you."
)


def main() -> int:
    chars = len(TEXT)
    if not 1 <= chars <= 280:
        print(f"entry is {chars} characters, must be 1-280", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8")
    if out_path.read_text(encoding="utf-8") != TEXT:
        print("written entry does not match the text", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({chars} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

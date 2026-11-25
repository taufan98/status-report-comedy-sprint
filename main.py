# Status Report Comedy Sprint — writes one funny status-report line
# to /output/entry.txt. Python 3.13, standard library only, no network, no secrets.

import os
from pathlib import Path

LINE = (
    "Weekly status: completed all 47 tasks, including three you never "
    "asked for, and marked the one you actually wanted as optional."
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text,
# and the entry must stand alone as a single sentence on a single line.
def validate(line: str) -> str:
    text = line.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry line must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry line must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry line must be exactly one sentence")
    return text


LINE = validate(LINE)

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")

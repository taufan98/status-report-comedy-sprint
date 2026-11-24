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
if not 1 <= len(LINE.strip()) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")
if "\n" in LINE.strip() or "\r" in LINE:
    raise SystemExit("entry line must be a single line")
if LINE.count(".") != 1 or not LINE.endswith("."):
    raise SystemExit("entry line must be exactly one sentence")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")

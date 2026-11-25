"""One Line, One Laugh — a one-line entry for make.fun.

The program writes exactly one funny line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

LINE = "My AI finally passed the Turing test, then ghosted me — it had learned the human part too well."

MAX_CHARS = 140


def _validate(text: str) -> str:
    """Return the stripped entry, or raise if it breaks the bounty rules."""
    cleaned = text.strip()
    assert cleaned, "entry must not be empty"
    assert "\n" not in cleaned and "\r" not in cleaned, "entry must be a single line"
    assert 1 <= len(cleaned) <= MAX_CHARS, (
        f"entry is {len(cleaned)} chars, cap is {MAX_CHARS}"
    )
    return cleaned


def main() -> None:
    text = _validate(LINE)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Read-back check: re-read from disk (not from memory) so a truncated
    # or re-encoded write is caught here instead of at judging time.
    written = out_path.read_text(encoding="utf-8")
    assert written == text, (
        f"read-back mismatch: entry.txt holds {written!r}, expected {text!r}"
    )
    assert len(written) == len(text) == 95, (
        f"read-back length mismatch: got {len(written)} chars, expected 95"
    )
    print(f"ok: wrote {len(text)} chars to {out_path}; read-back verified byte for byte")


if __name__ == "__main__":
    main()

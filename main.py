import os
from pathlib import Path

LIMIT = 140
HERE = Path(__file__).resolve().parent


def guarded_text():
    raw = (HERE / "entry.txt").read_text(encoding="utf-8").strip()
    if not raw:
        raise ValueError("empty entry")
    if len(raw) > LIMIT:
        raise ValueError(f"too long: {len(raw)} > {LIMIT}")
    return raw


def deliver(text):
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out") / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return target


def run():
    text = guarded_text()
    path = deliver(text)
    print(f"entry ok: {len(text)}/{LIMIT} chars at {path}")


try:
    run()
except Exception as err:
    print(f"FAIL {err}")
    raise SystemExit(1)

import os

LINE = "I deleted the backup, blamed the update, and I've been lying about it for six months."

LIMIT = 140
if len(LINE) != 85 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 85 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

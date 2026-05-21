from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
LATEST = ROOT / "runs" / "latest"

print("Latest run folder:", LATEST)

if not LATEST.exists():
    print("No latest run folder found.")
    raise SystemExit(0)

for path in sorted(LATEST.rglob("*")):
    if path.is_file():
        print("-", path.relative_to(ROOT))

for name in ["timings.json", "errors.json", "decisions.json"]:
    file_path = LATEST / name
    if file_path.exists():
        print(f"\n{name}:")
        try:
            print(json.dumps(json.loads(file_path.read_text(encoding="utf-8")), indent=2))
        except Exception:
            print(file_path.read_text(encoding="utf-8"))

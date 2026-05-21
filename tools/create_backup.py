from pathlib import Path
from datetime import datetime
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BACKUP_DIR = ROOT / "backups"
BACKUP_DIR.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
zip_path = BACKUP_DIR / f"project_backup_{timestamp}.zip"

EXCLUDE_DIRS = {
    "backups",
    "logs",
    "screenshots",
    "runs",
    "extracted",
    "__pycache__",
    ".venv",
    "node_modules",
    ".git",
}

EXCLUDE_SUFFIXES = {
    ".log",
    ".tmp",
    ".pyc",
}

EXCLUDE_FILES = {
    ".env",
}


def should_exclude(path: Path) -> bool:
    rel_parts = set(path.relative_to(ROOT).parts)

    if rel_parts & EXCLUDE_DIRS:
        return True

    if path.name in EXCLUDE_FILES:
        return True

    if path.suffix in EXCLUDE_SUFFIXES:
        return True

    return False


with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for path in ROOT.rglob("*"):
        if path.is_file() and not should_exclude(path):
            zf.write(path, path.relative_to(ROOT))

print(f"Backup created: {zip_path}")

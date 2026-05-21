"""
Placeholder extractor script.

Purpose:
- Keep Excel/Office parsing separate from business logic.
- Produce normalized, inspectable intermediate data.
- Preserve original input files.

Adapt this file per project.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "inputs"
EXTRACTED_DIR = ROOT / "extracted"
EXTRACTED_DIR.mkdir(exist_ok=True)

print("Extractor placeholder")
print(f"Input folder: {INPUT_DIR}")
print(f"Extracted output folder: {EXTRACTED_DIR}")
print("Implement project-specific extraction here.")

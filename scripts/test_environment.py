#!/usr/bin/env python3
"""Quick test to verify notebook imports work."""

import sys
from pathlib import Path
import nbformat


def main():
    print("🔍 Testing notebook imports...")

    # Get all notebooks
    notebooks = [f for f in Path(".").glob("*.ipynb") if not f.name.startswith("test_")]

    # Extract and test imports
    all_imports = set()
    for nb in notebooks:
        try:
            with open(nb, "r") as f:
                nb_data = nbformat.read(f, as_version=4)
            for cell in nb_data.cells:
                if cell.cell_type == "code":
                    for line in cell.source.split("\n"):
                        line = line.strip()
                        if line.startswith(
                            ("import ", "from ")
                        ) and not line.startswith("#"):
                            all_imports.add(line.split("#")[0].strip())
        except Exception as e:
            print(f"❌ Error reading {nb.name}: {e}")
            return False

    # Test imports
    failed = []
    for imp in sorted(all_imports):
        if imp.strip() == "import test":  # Skip teaching example
            continue
        try:
            exec(imp)
            print(f"✅ {imp}")
        except Exception as e:
            print(f"❌ {imp}: {e}")
            failed.append(imp)

    if failed:
        print(f"\n❌ {len(failed)} imports failed")
        return False
    else:
        print(f"\n🎉 All {len(all_imports)} imports work!")
        return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)

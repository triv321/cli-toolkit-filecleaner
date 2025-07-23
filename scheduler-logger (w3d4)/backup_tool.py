# automation_tools/backup_tool.py

import os
from zipfile import ZipFile
from datetime import datetime
from pathlib import Path
import logging
import sys

print("backup startedd")

def backup_folder(source_path):
    source = Path(source_path)
    if not source.exists():
        print("Source folder does not exist.")
        return

    backups_dir = Path("backups")
    backups_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = backups_dir / f"{source.name}_backup_{timestamp}.zip"

    with ZipFile(zip_name, "w") as zipf:
        for file in source.rglob("*"):
            zipf.write(file, file.relative_to(source))

    print(f"Backup created: {zip_name}")

print("backup finish")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python backup_tool.py <folder_path>")
    else:
        backup_folder(sys.argv[1])
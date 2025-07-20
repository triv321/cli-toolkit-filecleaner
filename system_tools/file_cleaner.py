# system_tools/file_cleaner.py

import os
import shutil
from pathlib import Path

EXTENSIONS_TO_CLEAN = [".tmp", ".log", ".pyc"]
DIRS_TO_DELETE = ["_pycache_"]

def clean_folder(target_path):
    target = Path(target_path).resolve()

    if not target.exists() or not target.is_dir():
        print(f"[ERROR] Invalid directory: {target}")
        return

    deleted_files = []
    deleted_dirs = []

    for path in target.rglob("*"):
        try:
            if path.is_symlink():
                continue  # skip symbolic links

            if path.is_file() and path.suffix in EXTENSIONS_TO_CLEAN:
                path.unlink()
                deleted_files.append(str(path))

            elif path.is_dir() and path.name in DIRS_TO_DELETE:
                shutil.rmtree(path)
                deleted_dirs.append(str(path))

        except Exception as e:
            print(f"[ERROR] Failed to delete {'file' if path.is_file() else 'dir'}: {path} — {e}")

    # Remove empty folders (bottom-up)
    for dirpath, _, _ in os.walk(target, topdown=False):
        dir_path = Path(dirpath)
        try:
            if not any(dir_path.iterdir()):
                dir_path.rmdir()
                deleted_dirs.append(str(dir_path))
        except Exception as e:
            print(f"[ERROR] Could not remove folder {dir_path} — {e}")

    # Summary output
    print("\n[INFO] Deleted files:")
    for f in deleted_files:
        print(f" - {f}")

    print("\n[INFO] Deleted directories:")
    for d in deleted_dirs:
        print(f" - {d}")

if __name__ == "__main__":
    folder = input("Enter folder path to clean: ").strip()
    clean_folder(folder)
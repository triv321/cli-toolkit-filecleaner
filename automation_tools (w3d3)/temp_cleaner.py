from pathlib import Path

JUNK_EXTENSIONS = [".tmp", ".log", ".DS_Store", "Thumbs.db"]

def clean_temp_files(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        print("Folder does not exist.")
        return

    count = 0
    for file in folder.rglob("*"):
        if file.suffix in JUNK_EXTENSIONS or file.name in JUNK_EXTENSIONS:
            try:
                file.unlink()
                count += 1
            except Exception as e:
                print(f"Failed to delete {file}: {e}")

    print(f"Deleted {count} junk files.")

if __name__ == "__main__":
    path = input("Enter folder to clean: ")
    clean_temp_files(path)

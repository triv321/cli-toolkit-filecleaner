# Automation Tools

Python scripts for automating common system-level tasks.

## Scripts

### 1. `backup_tool.py`
- **What**: it compresses a folder into a `.zip` file (timestamped)
- **Usage**: just run and enter the folder path when prompted
- **Output**: saves zipped backups inside `backups/` folder

### 2. `sysinfo.py`
- **What**: prints system information
- **Details**: CPU usage, RAM usage, disk usage, OS version

### 3. `temp_cleaner.py`
- **What**: Deletes temp/junk files from a folder (similar to what I made before)
- **Targets**: `.tmp`, `.log`, `.DS_Store`, `Thumbs.db`, etc.
- **Usage**: Run and input the folder to clean

## Running

```bash
python script_name.py

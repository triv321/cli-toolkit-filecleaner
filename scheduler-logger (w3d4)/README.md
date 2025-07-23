# Scheduler & Logging

Automates backup tasks using Python's `schedule` module with logging and system-level automation via Task Scheduler.

---

## Structure

└── scheduler-logger/
    ├── schedule_backup.py (Main function/project)
    ├── backup_tool.py
    ├── run_backup.bat
    ├── scheduler.py (test function to understand schedule module)
    ├── logger.py (test function to understand logging module)
    └── logs/
     └── backup.log
    └── test/ (test folder which gets backed up)


---

## schedule_backup.py

- Runs `backup_tool.py` every 20 seconds
- Uses `subprocess` to execute backup
- Logs output and errors to `logs/backup.log`

### Tools Used

- `schedule`: time-based job scheduler
- `logging`: to track runs
- `subprocess`: to execute backup script
- `pathlib`: for path handling

---

## Logging

Logs saved at:

    logs/backup.log


Includes timestamps, info, errors, and exceptions.

---

## run_backup.bat

Launches the scheduler script:

```bat
@echo off
cd /d "C:\path\to\project"
"C:\path\to\python.exe" "C:\path\to\schedule_backup.py"

*Use absolute paths with double quotes.

---

##
 Automate via Task Scheduler/Cron:

   - Open Task Scheduler

   - Create Basic Task → Trigger: One Time or At Log On

   - Action: Start run_backup.bat

   - Save and test

##
Troubleshooting

    If .log is empty, verify script paths and logging setup

    If Task Scheduler shows 0x1 exit code:

        Check for syntax errors or invalid paths in .bat

        Ensure .bat paths are absolute and double-quoted

    Make sure .py files run manually without issues before scheduling

##
How to Stop the Script

The script runs indefinitely by design. To stop:

    Kill the process manually via Task Manager

    Or close the command prompt if run manually

    To change behavior to run once, remove the while True loop and use direct run_backup() execution

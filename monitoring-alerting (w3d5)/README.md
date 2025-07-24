
---

# Resource Monitor & Alert System

This script monitors system resources (CPU, RAM, and Disk) and sends an alert email when any of them exceed the defined thresholds. The logs are stored locally, and alerts are automated via a batch file.

## Features

* Monitors:

  * CPU usage
  * Memory usage
  * Disk usage
* Sends email alerts via Gmail when thresholds are crossed
* Logs all resource stats to a log file
* Automates execution via `.bat` file

## Threshold Configuration

```python
CPU_THRESHOLD = 85
MEMORY_THRESHOLD = 90
DISK_THRESHOLD = 70
CHECK_INTERVAL = 60  # Seconds (not used in single run mode)
```

## Setup Instructions

1. **Install Dependencies**

   ```bash
   pip install psutil
   ```

2. **Enable Gmail App Passwords**

   * Turn on 2-Step Verification in your Gmail account
   * Generate a 16-character App Password
   * Use that password in the script #app pasword

3. **Environment Variables Setup**
   Create a `.env` file (or use `os.environ` method in script):

   ```
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_generated_app_password
   ```

4. **Directory Structure**

   ```
   .
   ├── resource_monitor.py
   ├── alerts/
       └── system_mon.log
   └── run_auto.bat
   └── README.md
   └── .env
   ```

5. **Automate with .bat File (Windows)**
   Example `run_auto.bat`:

   ```bat
   @echo off
   cd /d "C:\path\to\your\project"
   "python_location" resource_monitor.py
   ```

6. **Schedule Task**
   Use Windows Task Scheduler to run the `.bat` file at desired intervals./ use cron in mac/linux

## Logs

All system metrics are logged to `alerts/system_mon.log`.

## Sample Email Alert

```
Subject: System Alert: Resource Usage Exceeded

High CPU usage: 92%
High Storage usage: 88%
```

---

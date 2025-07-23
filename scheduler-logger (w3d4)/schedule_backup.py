import schedule
import os
import time
import subprocess
import logging
from pathlib import Path

log_dir = Path("C:/Users/thaku/Desktop/data/reel/ai_infra_2/infra-cli-toolkit (w3)/scheduler-logger (w3d4)/logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=str(log_dir / "backup.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_backup():
    try:
        result = subprocess.run(
            [r"C:\Users\thaku\AppData\Local\Programs\Python\Python313\python.exe",
             r"C:\Users\thaku\Desktop\data\reel\ai_infra_2\infra-cli-toolkit (w3)\scheduler-logger (w3d4)\backup_tool.py",
             r"C:\Users\thaku\Desktop\data\reel\ai_infra_2\infra-cli-toolkit (w3)\scheduler-logger (w3d4)\test"],
            capture_output=True,
            text=True,
            timeout=5
        )

        logging.info(f"Backup stdout: {result.stdout.strip()}")

        if result.returncode == 0:
            logging.info("Backup ran successfully")
        else:
            logging.error(f"Backup failed: {result.stderr.strip()}")
    except Exception as e:
        logging.error(f"Exception during backup: {str(e)}")

schedule.every(20).seconds.do(run_backup)

while True:
    schedule.run_pending()
    time.sleep(1)

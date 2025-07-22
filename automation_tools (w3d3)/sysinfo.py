import psutil
import platform
from datetime import datetime

def get_system_info():
    info = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Platform": platform.system(),
        "Platform-release": platform.release(),
        "CPU Usage": f"{psutil.cpu_percent()}%",
        "RAM Usage": f"{psutil.virtual_memory().percent}%",
        "Disk Usage": f"{psutil.disk_usage('/').percent}%"
    }

    for k, v in info.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    get_system_info()

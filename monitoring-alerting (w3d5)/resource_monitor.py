import psutil
import time
import logging
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

#setting thresholds for the resources
CPU_THRESHOLD = 85
MEMORY_THRESHOLD = 90
DISK_THRESHOLD = 70
CHECK_INTERVAL = 60 #SECONDS

logging.basicConfig(
    filename = 'alerts/system_mon.log', # use absolute path when automating using cron/task scheduler calling .bat file
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def check_resources():
    alerts_trigg = []

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    logging.info(f'CPU: {cpu}%')
    logging.info(f'Memory: {memory}%')
    logging.info(f'Disk: {disk}%')

    print(f' CPU: {cpu}% \n Memory: {memory}% \n Disk: {disk}%')

    if cpu > CPU_THRESHOLD:
        alerts_trigg.append(f'High CPU usage: {cpu}%')
    if memory > MEMORY_THRESHOLD:
        alerts_trigg.append(f'High RAM usage: {memory}%')
    if disk > DISK_THRESHOLD:
        alerts_trigg.append(f'High Storage usage: {cpu}%')
    
    return alerts_trigg

def send_email_alert(subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv("EMAIL_ADDRESS")        
    receiver_email = os.getenv("EMAIL_ADDRESS")   
    app_password = os.getenv("EMAIL_PASSWORD")      

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")




if __name__ == "__main__":
    alerts = check_resources()
    if alerts:
        print("Alerts:")
        for alert in alerts:
            print(alert)
        subject = "System Alert: Resource Usage Exceeded"
        body = "\n".join(alerts)
        send_email_alert(subject, body)

    else:
        print("System is healthy.")

        

import logging

logging.basicConfig(
    filename = 'logs/backup.log',
    level = logging.INFO,
    format = '%(asctime)s %(levelname)s: %(message)s'
)

logging.info("Backup starts..")
logging.error("Backup failed")
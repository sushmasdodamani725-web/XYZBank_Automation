# utils/logger.py
import logging
import os

LOG_FILE = "test_log.log"
os.makedirs("logs", exist_ok=True)
LOG_PATH = os.path.join("logs", LOG_FILE)

def get_logger(name="banking_logger"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.FileHandler(LOG_PATH)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

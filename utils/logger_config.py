import logging
from pathlib import Path

LOG_FILE = Path("tesreco.log")


def setup_logger(name="tesreco"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


logger = setup_logger()
logger.info("Logger initialized for login events, errors, and report generation.")

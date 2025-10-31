import logging
from pathlib import Path
from datetime import datetime


def get_logger(name: str = "test_automation", log_level: str = "INFO"):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(getattr(logging, log_level.upper()))

        logs_dir = Path("logs")
        logs_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = logs_dir / f"test_{timestamp}.log"

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

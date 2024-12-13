import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

LEVEL: int = 0
FILENAME: str = ""
BACKUP_COUNT: int = 1
MAX_BYTES: int = 102400
TIME_INTERVAL: int = 2
WHEN: str = "d"

for handler in logging.root.handlers:
    logging.root.removeHandler(handler)

file_formatter = logging.Formatter()
file_handler = logging.FileHandler(FILENAME)
file_handler.setFormatter(file_formatter)

stream_formatter = logging.Formatter()
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)

rotating_handler = RotatingFileHandler(
    filename=FILENAME,
    maxBytes=MAX_BYTES,
    backupCount=BACKUP_COUNT,
)
timed_rotating_handler = TimedRotatingFileHandler(
    filename=FILENAME,
    when=WHEN,
    interval=TIME_INTERVAL,
)

handlers = [file_handler, stream_handler,
            rotating_handler, timed_rotating_handler]

logging.root.handlers = handlers

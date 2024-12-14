import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from .settings import LoggerSettings

SETTINGS = LoggerSettings()

for handler in logging.root.handlers:
    logging.root.removeHandler(handler)

file_formatter = logging.Formatter()
file_handler = logging.FileHandler(SETTINGS.FILENAME)
file_handler.setFormatter(file_formatter)

stream_formatter = logging.Formatter()
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)

rotating_handler = RotatingFileHandler(
    filename=SETTINGS.FILENAME,
    maxBytes=SETTINGS.MAX_BYTES,
    backupCount=SETTINGS.BACKUP_COUNT,
)
timed_rotating_handler = TimedRotatingFileHandler(
    filename=SETTINGS.FILENAME,
    when=SETTINGS.ROTATING_PER,
    interval=SETTINGS.ROTATING_INTERVAL,
)

handlers = [file_handler, stream_handler,
            rotating_handler, timed_rotating_handler]

logging.root.handlers = handlers

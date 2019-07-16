import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from src.util.EnvironmentUtils import EnvironmentUtils


class Logger:
    LOGGING_FILE_NAME = 'elections.log'
    FORMATTING_STRING = '%(asctime)s - [%(threadName)s] - %(levelname)s - %(name)s - %(message)s'
    LOGGING_LEVEL = logging.INFO
    MAX_BYTES = (1024**2)*100  # 100MB
    BACKUP_COUNT = 5  # Keep up to elections.log.5

    __initialized = False

    @classmethod
    def set_up(cls, environment):
        if EnvironmentUtils.is_prod(environment):
            file_name = f'{Path.home()}/logs/api/{cls.LOGGING_FILE_NAME}'
        else:
            file_name = cls.LOGGING_FILE_NAME
        # Handler for file writing
        file_handler = RotatingFileHandler(file_name, maxBytes=cls.MAX_BYTES, backupCount=cls.BACKUP_COUNT)
        # Handler for console output
        console_handler = logging.StreamHandler()
        # Configure
        logging.basicConfig(format=Logger.FORMATTING_STRING, level=Logger.LOGGING_LEVEL,
                            handlers=[file_handler, console_handler])

    def __init__(self, class_name):
        self._logger = Logger.build_logger(class_name)

    def info(self, message):
        self._logger.info(message)

    def error(self, message):
        self._logger.exception(message)

    def debug(self, message):
        self._logger.debug(message)

    def warning(self, message):
        self._logger.warning(message)

    @classmethod
    def build_logger(cls, class_name):
        return logging.getLogger(class_name)

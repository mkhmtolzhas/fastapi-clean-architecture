import logging
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def debug(self, message: str) -> None:
        pass

    @abstractmethod
    def info(self, message: str) -> None:
        pass

    @abstractmethod
    def warning(self, message: str) -> None:
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        pass

    @abstractmethod
    def critical(self, message: str) -> None:
        pass


class FileLogger(Logger):
    def __init__(self, name: str, log_file: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)


        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)


logger = FileLogger(__name__, "app.log")
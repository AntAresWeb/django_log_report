import fileinput
import logging
from abc import ABC, abstractmethod
from pathlib import Path


class EngineAbstract(ABC):
    """Абстрактный класс обработчика лог-файлов"""
    def __init__(self, report, file_list: dict[str]) -> None:
        self.__report = report
        self.__file_list = file_list
        self.__check_file_list(self)
        if len(self.file_list) == 0:
            raise ValueError("Нет файлов для обработки.")

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    def __check_file_list(self) -> None:
        for file in self.__file_list:
            if not Path.exists(file):
                logging.info("Не найден файл: %s", file)
                self.file_list.pop(file)


class SerialEngine(EngineAbstract):
    """Класс последовательной обработки файлов."""
    def run(self) -> None:
        with fileinput.FileInput(files=self.__file_list) as file:
            for line in file:
                self.__process(line)

    def __process(self, line: str) -> None:
        self.__report.process_string(line)

    def get_report(self):
        self.__report.show()

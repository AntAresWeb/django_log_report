import fileinput
import logging
from abc import ABC, abstractmethod
from pathlib import Path

from app.reports.reports import AbstractReport


class EngineAbstract(ABC):
    """Абстрактный класс обработчика лог-файлов."""
    def __init__(self, report: AbstractReport, file_list: dict[str] | None) -> None:
        self.__report = report
        self.__file_list = file_list
        if file_list:
            self.set_file_list(file_list)
        else:
            self.__file_list = []

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    def set_file_list(self, file_list: dict[str]) -> None:
        for file in file_list:
            if not Path.exists(file):
                logging.info("Не найден файл: %s", file)
                self.file_list.pop(file)
            else:
                self.__file_list.append(file)
        if len(self.__file_list) == 0:
            msg = "Нет файлов для обработки. Работа остановлена!"
            logging.info(msg)
            raise ValueError(msg)


class SerialEngine(EngineAbstract):
    """Класс последовательной обработки файлов."""
    def run(self) -> None:
        with fileinput.FileInput(files=self.__file_list) as file:
            for line in file:
                self.__process(line)

    def __process(self, line: str) -> None:
        self.__report.collect_statistic(line)

    def get_report(self) -> None:
        self.__report.show()

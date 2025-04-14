import fileinput
from abc import ABC, abstractmethod

from app.reports.reports import AbstractReport


class EngineAbstract(ABC):
    """Абстрактный класс обработчика лог-файлов."""
    def __init__(self, report: AbstractReport, file_list: dict[str] | None) -> None:
        self.report = report
        self.file_list = file_list

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError


class SerialEngine(EngineAbstract):
    """Класс последовательной обработки файлов."""
    def run(self) -> None:
        with fileinput.FileInput(files=self.file_list) as file:
            for line in file:
                self.process(line)

    def process(self, line: str) -> None:
        self.report.collect_statistic(line)

    def get_report(self) -> list:
        return self.report.show()

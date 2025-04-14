from abc import ABC, abstractmethod
from collections import defaultdict

from app.parsers.parsers import AbstactParser
from app.reports.datas import StatusCollectData


class AbstractReport(ABC):
    """Абстрактный класс отчета."""
    def __init__(self, parser: AbstactParser) -> None:
        self.parser = parser

    @abstractmethod
    def show(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def collect_statistic(self, line: str) -> None:
        raise NotImplementedError


class HandlersReport(AbstractReport):
    def __init__(self, parser: AbstactParser) -> None:
        super().__init__(parser)
        self.name = "handler"
        self.__collector = defaultdict(lambda: StatusCollectData())

    @property
    def collector(self) -> defaultdict:
        return self.__collector

    def collect_statistic(self, line: str) -> None:
        parsed_data = self.parser.parse(line)
        if (parsed_data
          and (endpoint:=parsed_data["endpoint"])
          and (status:=parsed_data["status"].lower())):
            data = self.__collector[endpoint].__dict__
            data[status] += 1
            for key, val in data.items():
                setattr(self.__collector[endpoint], key, val)

    def show(self) -> dict[str]:
        report_strings = []
        if len(self.__collector) < 1:
            return report_strings

        sorted_endpoint = sorted(self.__collector.keys())
        longest_endpoint = max(len(s) for s in sorted_endpoint)

        header = ["handler", "debug", "info", "warning", "error", "critical"]
        position = [longest_endpoint + 2, 12, 12, 12, 12, 12]
        st = ""
        for i in range(6):
            st += f"{header[i].upper():<{position[i]}}"
        report_strings.append(st)

        total_request = 0
        for endpoint in sorted_endpoint:
            st = f"{endpoint:<{position[0]}}"
            data = self.__collector[endpoint].__dict__
            for idx, status in enumerate(header[1:]):
                st += f"{data.get(status, ''):{position[idx + 1]}}"
                total_request += data.get(status, 0)
            report_strings.append(st)

        report_strings.append("")
        report_strings.append(f"Total request: {total_request:>15}")

        return report_strings

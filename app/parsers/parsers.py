import re
import typing
from abc import ABC, abstractmethod


class AbstactParser(ABC):
    @abstractmethod
    def parse(self, line: str) -> dict:
        raise NotImplementedError


class DjangoRequestParser(AbstactParser):
    """Парсит строку в которой имеется подстрока 'django.request:'"""
    pattern_type = r"django.request:"
    pattern_dict: typing.ClassVar = {
        "status": r"CRITICAL|DEBUG|ERROR|INFO|WARNING",
        "method": r"GET|POST|PATCH|PUT|DELETE",
        "endpoint": r"(\/)([\w\-]+\/)+",
    }

    def parse(self, line: str) -> dict | None:
        if re.search(self.pattern_type, line) is None:
            return None

        result = {}
        for key, val in self.pattern_dict.items():
            selection = re.search(val, line)
            result[key] = selection[0] if selection else None
        return result

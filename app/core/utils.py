import logging
from pathlib import Path

import app.core.constants as const


def check_file_list(file_list: dict[str] | None) -> dict[str] | None:
    if file_list is None:
        return None

    file_set = set(file_list)
    checked_file_list = []
    for file in file_set:
        if Path(file).exists():
            checked_file_list.append(file)
        else:
            logging.error("Не найден файл: %s", file)

    if len(checked_file_list) == 0:
        msg = "Нет файлов для обработки!"
        logging.error(msg)
        return None

    return checked_file_list

def check_report_type(report_type: str) -> bool:
    return report_type in const.AVAILABLE_REPORT_TYPES

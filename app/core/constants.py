from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S"

SERVICE_NAME = "django-log-report"
SERVICE_DECRIPTION = "Отчет по анализу журнала логирования django-приложения."
SERVICE_USAGE = "python main.py log_file_1 [log_file_2 [log_file_n]] --report type_report"
SERVICE_LOG_SIZE_BYTE = 1_000_000
SERVICE_LOG_COUNT = 5
SEVICE_LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'

AVAILABLE_REPORT_TYPES = [
    "handlers",
]

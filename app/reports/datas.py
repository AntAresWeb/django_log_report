from dataclasses import dataclass


@dataclass
class StatusCollectData:
    critical: int = 0
    debug: int = 0
    error: int = 0
    info: int = 0
    warning: int = 0


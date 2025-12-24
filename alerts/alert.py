from dataclasses import dataclass
from datetime import datetime
from typing import List

from models.log_event import LogEvent


@dataclass
class Alert:
    rule_name: str
    severity: str
    timestamp: datetime
    evidence: List[LogEvent]

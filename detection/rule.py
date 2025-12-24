from abc import ABC, abstractmethod
from typing import List

from models.log_event import LogEvent


class DetectionRule(ABC):
    @abstractmethod
    def evaluate(self, events: List[LogEvent]):
        """
        Analyseer log events en bepaal of er een aanval is.
        Moet worden geïmplementeerd door elke concrete rule.
        """
        pass

from typing import List
from detection.rule import DetectionRule
from models.log_event import LogEvent
from alerts.alert import Alert  

class DetectionEngine:
    def __init__(self, rules: List[DetectionRule]):
        self.rules = rules
        self.events: List[LogEvent] = []

    def add_event(self, event: LogEvent) -> None:
        """Voeg een nieuw log event toe aan de engine."""
        self.events.append(event)

    def run(self) -> List[Alert]:
        """Voer alle rules uit en verzamel alerts."""
        alerts: List[Alert] = []
        for rule in self.rules:
            alert = rule.evaluate(self.events)
            if alert: 
                alerts.append(alert)
        return alerts

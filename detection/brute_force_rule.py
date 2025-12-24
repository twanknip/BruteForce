from datetime import datetime, timedelta
from typing import List
from detection.rule import DetectionRule
from models.log_event import LogEvent
from alerts.alert import Alert  


class BruteForceRule(DetectionRule):
    def __init__(self, max_failures: int, window_seconds: int):
        self.max_failures = max_failures
        self.window = timedelta(seconds=window_seconds)

    def evaluate(self, events: List[LogEvent]) -> Alert | None:
        failed_events = [e for e in events if not e.success]
        failed_events.sort(key=lambda e: e.timestamp)

        for i in range(len(failed_events)):
            start_event = failed_events[i]
            count = 1
            for j in range(i + 1, len(failed_events)):
                current_event = failed_events[j]
                if current_event.ip_address != start_event.ip_address:
                    continue
                if current_event.timestamp - start_event.timestamp > self.window:
                    break
                count += 1
                if count >= self.max_failures:
                    return Alert(
                        rule_name="BruteForceRule",
                        severity="High",
                        timestamp=datetime.now(),
                        evidence=failed_events[i:j+1]
                    )
        return None

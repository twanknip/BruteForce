from datetime import datetime
from typing import List

from models.log_event import LogEvent


class LogReader:
    def read_file(self, path: str) -> List[LogEvent]:
        events: List[LogEvent] = []

        with open(path, "r") as file:
            for line in file:
                event = self._parse_line(line.strip())
                if event:
                    events.append(event)

        return events

    def _parse_line(self, line: str) -> LogEvent | None:
        try:
            timestamp_str, ip, username, success_str = line.split(",")

            return LogEvent(
                timestamp=datetime.fromisoformat(timestamp_str),
                ip_address=ip,
                username=username,
                success=success_str.lower() == "true"
            )
        except ValueError:
            return None

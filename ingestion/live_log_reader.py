import time
from datetime import datetime
from typing import Iterator

from models.log_event import LogEvent


class LiveLogReader:
    def __init__(self, path: str, poll_interval: float = 1.0):
        self.path = path
        self.poll_interval = poll_interval

    def follow(self) -> Iterator[LogEvent]:
        with open(self.path, "r") as file:
            file.seek(0, 2)  

            while True:
                line = file.readline()

                if not line:
                    time.sleep(self.poll_interval)
                    continue

                event = self._parse_line(line.strip())
                if event:
                    yield event

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

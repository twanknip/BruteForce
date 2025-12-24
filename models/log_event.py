from datetime import datetime


class LogEvent:
    def __init__(
        self,
        timestamp: datetime,
        ip_address: str,
        username: str,
        success: bool
    ):
        self.timestamp = timestamp
        self.ip_address = ip_address
        self.username = username
        self.success = success

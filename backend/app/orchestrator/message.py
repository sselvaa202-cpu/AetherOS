from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    """
    Represents a message exchanged between agents.
    """

    sender: str
    receiver: str
    content: str
    timestamp: datetime

    @classmethod
    def create(
        cls,
        sender: str,
        receiver: str,
        content: str,
    ):
        return cls(
            sender=sender,
            receiver=receiver,
            content=content,
            timestamp=datetime.now(),
        )
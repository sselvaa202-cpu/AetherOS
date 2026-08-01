from enum import Enum


class AgentStatus(str, Enum):
    """
    Represents the execution state of an agent.
    """

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
from datetime import datetime
from typing import Any

from pydantic import BaseModel


class AgentInfo(BaseModel):
    """
    Information about an AI agent.
    """
    name: str
    description: str


class AgentRequest(BaseModel):
    """
    Request sent to an AI agent.
    """
    agent_name: str
    task: str

class TaskRequest(BaseModel):
    """
    Request without specifying an agent.
    The Router Agent will decide.
    """

    task: str


class AgentResponse(BaseModel):
    """
    Standard response returned by any AI agent.
    """
    agent: str
    status: str
    execution_time_ms: float
    timestamp: datetime
    result: Any
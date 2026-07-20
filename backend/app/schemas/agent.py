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


class AgentResponse(BaseModel):
    """
    Response returned by an AI agent.
    """
    agent_name: str
    result: str
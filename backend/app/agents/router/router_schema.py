from pydantic import BaseModel, Field


class RouterDecision(BaseModel):
    """
    Structured decision returned by the LLM Router.
    """

    intent: str = Field(
        description="The primary intent of the user's message."
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence level of the routing decision."
    )

    reason: str = Field(
        description="Short explanation for the routing decision."
    )

    recommended_agents: list[str] = Field(
        min_length=1,
        description="Agents recommended to handle the request."
    )
from dataclasses import dataclass, field


@dataclass
class AgentSpec:
    """
    Defines the capabilities and configuration of an AetherOS agent.
    """

    name: str

    description: str

    priority: str

    supported_tasks: list[str] = field(
        default_factory=list
    )

    tools: list[str] = field(
        default_factory=list
    )

    memory_read: list[str] = field(
        default_factory=list
    )

    memory_write: list[str] = field(
        default_factory=list
    )

    status: str = "active"
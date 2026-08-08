from app.agents.base import BaseAgent
from app.registry.agent_registry import registry


class AgentManager:
    """
    Controls the lifecycle and execution
    of AetherOS agents.
    """

    def __init__(self):
        self.registry = registry

    def register_agent(
        self,
        agent: BaseAgent,
    ):
        """
        Register an agent in the central registry.
        """

        self.registry.register(agent)

    def get_agent(
        self,
        name: str,
    ):
        """
        Retrieve an agent by name.
        """

        return self.registry.get(name)

    def list_agents(self):
        """
        List all registered agents.
        """

        return self.registry.get_all()
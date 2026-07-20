from app.agents.base import BaseAgent
from app.agents.registry import AgentRegistry


class AgentManager:
    """
    Controls the lifecycle of AI agents.
    """

    def __init__(self):
        self.registry = AgentRegistry()

    def register_agent(
        self,
        agent: BaseAgent
    ):
        """
        Register an agent.
        """
        self.registry.register(agent)

    def get_agent(
        self,
        name: str
    ):
        """
        Retrieve an agent by name.
        """
        return self.registry.get(name)

    def list_agents(self):
        """
        List all registered agents.
        """
        return self.registry.list_agents()
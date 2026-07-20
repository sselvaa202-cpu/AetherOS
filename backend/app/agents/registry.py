from app.agents.base import BaseAgent


class AgentRegistry:
    """
    Stores and manages all registered AI agents.
    """

    def __init__(self):
        self._agents = {}

    def register(
        self,
        agent: BaseAgent
    ):
        """
        Register a new agent.
        """
        self._agents[agent.name] = agent

    def get(
        self,
        name: str
    ):
        """
        Retrieve an agent by name.
        """
        return self._agents.get(name)

    def list_agents(self):
        """
        Return all registered agent names.
        """
        return list(self._agents.keys())
    
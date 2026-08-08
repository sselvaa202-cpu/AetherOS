from app.agents.base import BaseAgent
from app.registry.agent_registry import registry


class AgentManager:
    """
    Controls the lifecycle and execution
    of AetherOS agents.
    """

    def __init__(self):
        self.registry = registry
        self._agents: dict[str, BaseAgent] = {}

    def register_agent(
        self,
        agent: BaseAgent,
    ):
        """
        Register an executable agent.
        """

        self._agents[agent.name] = agent

    def get_agent(
        self,
        name: str,
    ):
        """
        Retrieve an executable agent by name.
        """

        return self._agents.get(name)

    def list_agents(self):
        """
        List all registered executable agents.
        """

        return list(self._agents.values())

    def execute_agent(
        self,
        name: str,
        task: str,
        context=None,
    ):
        """
        Execute an agent by name.
        """

        agent = self.get_agent(name)

        if agent is None:
            raise ValueError(
                f"Agent '{name}' is not registered."
            )

        return agent.run(
            task=task,
            context=context,
        )
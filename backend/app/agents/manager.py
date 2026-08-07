from app.agents.base import BaseAgent
from app.agents.registry import AgentRegistry as RuntimeAgentRegistry

from app.registry.agent_registry import registry as agent_spec_registry


class AgentManager:
    """
    Controls the lifecycle of AI agents.

    RuntimeAgentRegistry stores actual agent objects.
    AgentSpecRegistry stores metadata about agents.
    """

    def __init__(self):
        # Existing runtime registry
        self.registry = RuntimeAgentRegistry()

        # New specification registry
        self.spec_registry = agent_spec_registry

    def register_agent(
        self,
        agent: BaseAgent
    ):
        """
        Register an actual agent instance.
        """

        self.registry.register(agent)

    def get_agent(
        self,
        name: str
    ):
        """
        Retrieve an actual agent by name.
        """

        return self.registry.get(name)

    def list_agents(self):
        """
        List all registered runtime agents.
        """

        return self.registry.list_agents()

    def get_agent_spec(
        self,
        name: str
    ):
        """
        Retrieve the specification of an agent.
        """

        return self.spec_registry.get(name)

    def list_agent_specs(self):
        """
        List all available agent specifications.
        """

        return self.spec_registry.get_all()
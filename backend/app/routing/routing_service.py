from app.agents.router.router_agent import RouterAgent
from app.agents.manager import AgentManager
from app.agents.router.router_schema import RouterDecision


class RoutingService:
    """
    Coordinates routing between the RouterAgent
    and the AgentManager.
    """

    def __init__(self):
        self.router = RouterAgent()
        self.agent_manager = AgentManager()

    def route(
        self,
        user_message: str,
    ) -> RouterDecision:
        """
        Classify the user's message and return
        a validated routing decision.
        """

        decision = self.router.route(
            user_message
        )

        return decision

    def get_agent(
        self,
        decision: RouterDecision,
    ):
        """
        Retrieve the primary agent selected
        by the routing decision.
        """

        if not decision.recommended_agents:
            return self.agent_manager.get_agent(
                "general"
            )

        agent_name = decision.recommended_agents[0]

        agent = self.agent_manager.get_agent(
            agent_name
        )

        if agent is None:
            return self.agent_manager.get_agent(
                "general"
            )

        return agent

    def route_and_get_agent(
        self,
        user_message: str,
    ):
        """
        Route the user message and retrieve
        the selected agent.
        """

        decision = self.route(
            user_message
        )

        agent = self.get_agent(
            decision
        )

        return decision, agent
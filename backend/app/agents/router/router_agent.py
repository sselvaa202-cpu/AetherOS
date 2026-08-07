import json

from app.agents.router.router_prompt import ROUTER_SYSTEM_PROMPT
from app.agents.router.router_schema import RouterDecision
from app.llm.openrouter import OpenRouterProvider
from app.registry.agent_registry import registry


class RouterAgent:
    """
    LLM-based Router Agent.

    Responsible for understanding the user's request
    and selecting the appropriate AetherOS agent.
    """

    def __init__(self):
        self.llm = OpenRouterProvider()

    def build_prompt(
        self,
        user_message: str,
    ) -> str:
        """
        Build the routing prompt.
        """

        agent_information = []

        for agent in registry.get_all():
            agent_information.append(
                {
                    "name": agent.name,
                    "description": agent.description,
                    "supported_tasks": agent.supported_tasks,
                }
            )

        return (
            f"{ROUTER_SYSTEM_PROMPT}\n\n"
            "AVAILABLE AGENT SPECIFICATIONS:\n"
            f"{json.dumps(agent_information, indent=2)}\n\n"
            "USER MESSAGE:\n"
            f"{user_message}\n\n"
            "Return ONLY valid JSON."
        )

    def validate_decision(
        self,
        decision: RouterDecision,
    ) -> RouterDecision:
        """
        Validate that the router selected
        registered AetherOS agents.
        """

        registered_agents = {
            agent.name
            for agent in registry.get_all()
        }

        # Check primary intent
        if decision.intent not in registered_agents:

            return RouterDecision(
                intent="general",
                confidence=0.0,
                reason=(
                    f"Router selected unknown agent "
                    f"'{decision.intent}'."
                ),
                recommended_agents=["general"],
            )

        # Keep only registered recommended agents
        valid_agents = [
            agent
            for agent in decision.recommended_agents
            if agent in registered_agents
        ]

        # No valid agents found
        if not valid_agents:

            return RouterDecision(
                intent="general",
                confidence=0.0,
                reason="Router returned no registered agents.",
                recommended_agents=["general"],
            )

        # Make sure the primary intent is included
        if decision.intent not in valid_agents:
            valid_agents.insert(
                0,
                decision.intent,
            )

        return RouterDecision(
            intent=decision.intent,
            confidence=decision.confidence,
            reason=decision.reason,
            recommended_agents=valid_agents,
        )

    def route(
        self,
        user_message: str,
    ) -> RouterDecision:
        """
        Classify the user's message using the LLM.
        """

        prompt = self.build_prompt(
            user_message
        )

        response = self.llm.generate(
            prompt=prompt,
            max_tokens=300,
        )

        try:

            data = json.loads(response)

            decision = RouterDecision(
                **data
            )

        except Exception as e:

            print("=" * 80)
            print("ROUTER ERROR")
            print(type(e).__name__)
            print(str(e))
            print("RAW ROUTER RESPONSE:")
            print(response)
            print("=" * 80)

            # Safe fallback
            decision = RouterDecision(
                intent="general",
                confidence=0.0,
                reason=(
                    "Router could not parse "
                    "the LLM response."
                ),
                recommended_agents=["general"],
            )

        # Validate against Agent Registry
        return self.validate_decision(
            decision
        )
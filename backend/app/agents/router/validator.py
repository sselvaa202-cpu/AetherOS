from app.agents.router.router_schema import RouterDecision
from app.registry.agent_registry import registry


class RouterValidator:
    """
    Validates the decision produced by the LLM Router.
    """

    FALLBACK_AGENT = "general"

    def validate(
        self,
        decision: RouterDecision,
    ) -> RouterDecision:
        """
        Validate router decision and ensure recommended agents exist.
        """

        # 1. Validate intent

        if not decision.intent:
            return self._fallback(
                "Router returned an empty intent."
            )

        # 2. Validate recommended agents

        if not decision.recommended_agents:
            return self._fallback(
                "Router returned no recommended agents."
            )

        # 3. Check whether agents actually exist

        valid_agents = []

        for agent_name in decision.recommended_agents:

            agent = registry.get(agent_name)

            if agent is not None:
                valid_agents.append(agent_name)

        # 4. No valid agents found

        if not valid_agents:
            return self._fallback(
                "Router recommended agents that are not registered."
            )

        # 5. Validate intent against registered agent

        if registry.get(decision.intent) is None:
            return RouterDecision(
                intent=valid_agents[0],
                confidence=decision.confidence,
                reason=(
                    f"Router intent '{decision.intent}' is not "
                    f"registered. Using recommended agent."
                ),
                recommended_agents=valid_agents,
            )

        # 6. Return cleaned decision

        return RouterDecision(
            intent=decision.intent,
            confidence=decision.confidence,
            reason=decision.reason,
            recommended_agents=valid_agents,
        )

    def _fallback(
        self,
        reason: str,
    ) -> RouterDecision:
        """
        Return a safe fallback decision.
        """

        return RouterDecision(
            intent=self.FALLBACK_AGENT,
            confidence=0.0,
            reason=reason,
            recommended_agents=[
                self.FALLBACK_AGENT
            ],
        )
from app.agents.manager import AgentManager


class Orchestrator:
    """
    Controls the execution of AI agents.
    """

    def __init__(
        self,
        manager: AgentManager,
    ):
        self.manager = manager

    def execute(
        self,
        task: str,
    ):
        """
        Route the task and execute the selected agents.
        """

        # Get Router Agent from Manager
        router = self.manager.get_agent("router")

        if router is None:
            raise ValueError("Router agent is not registered.")

        # Router returns a list of agent names
        selected_agents = router.run(task)

        results = []

        for agent_name in selected_agents:

            agent = self.manager.get_agent(agent_name)

            if agent is None:
                raise ValueError(
                    f"Agent '{agent_name}' is not registered."
                )

            result = agent.run(task)

            results.append(result)

        return {
            "workflow": selected_agents,
            "results": results
        }
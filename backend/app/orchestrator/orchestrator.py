from app.agents.manager import AgentManager
from app.orchestrator.context import WorkflowContext
import time


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

        context = WorkflowContext(task)

        # Get Router Agent from Manager
        router = self.manager.get_agent("router")

        if router is None:
            raise ValueError("Router agent is not registered.")

        # Router returns a list of agent names
        selected_agents = router.run(task)

        results = {}

        # Workflow Start Time
        workflow_start = time.perf_counter()

        for agent_name in selected_agents:

            agent = self.manager.get_agent(agent_name)

            if agent is None:
                raise ValueError(
                    f"Agent '{agent_name}' is not registered."
                )

            # Agent Start Time
            agent_start = time.perf_counter()

            result = agent.run(task, context)

            # Agent End Time
            agent_end = time.perf_counter()

            execution_time = round(
                (agent_end - agent_start) * 1000,
                2
            )

            print(f"\n{agent_name} executed in {execution_time} ms")

            print("\n===== Agent Result =====")
            print(result)
            print("========================")

            results[agent_name] = {
            **result,
            "execution_time_ms": execution_time
            }

            print("\n===== Workflow Context =====")
            print(context.get_all_results())
            print("============================\n")

        # Workflow End Time
        workflow_end = time.perf_counter()

        total_time = round(
            (workflow_end - workflow_start) * 1000,
            2
        )

        print("\n" + "=" * 60)
        print(f"Workflow completed in {total_time} ms")
        print("=" * 60)

        return {
            "workflow": selected_agents,
            "total_execution_time_ms": total_time,
            "results": results
        }
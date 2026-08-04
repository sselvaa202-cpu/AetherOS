from app.agents.manager import AgentManager
from app.orchestrator.context import WorkflowContext
from app.orchestrator.status import AgentStatus
import time



class Orchestrator:
    """
    Controls the execution of AI agents.
    """

    def __init__(self, manager: AgentManager):
        self.manager = manager

    def execute(self, task: str,session_id: str,):
        """
        Route the task and execute the selected agents.
        """

        context = WorkflowContext(task,session_id)

        # Get Router Agent
        router = self.manager.get_agent("router")

        if router is None:
            raise ValueError("Router agent is not registered.")

        # Router returns list of agent names
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


            try:
                # Agent Started
                context.set_status(agent_name, AgentStatus.RUNNING)

                print("\n" + "=" * 60)
                print(f"Agent  : {agent_name}")
                print(f"Status : {AgentStatus.RUNNING.value}")
                print("=" * 60)

                # Start Timer
                agent_start = time.perf_counter()

                result = agent.run(task, context)

                # End Timer
                agent_end = time.perf_counter()

                execution_time = round(
                    (agent_end - agent_start) * 1000,
                    2
                )

                # Save Result
                results[agent_name] = {
                    **result,
                    "execution_time_ms": execution_time
                }

                # Save to Context
                context.set_result(agent_name, result)

                # Completed
                context.set_status(
                    agent_name,
                    AgentStatus.COMPLETED
                )

                print(f"Status : {AgentStatus.COMPLETED.value}")
                print(f"Time   : {execution_time} ms")

            except Exception as e:

                context.set_status(
                    agent_name,
                    AgentStatus.FAILED
                )

                print(f"Status : {AgentStatus.FAILED.value}")
                print(f"Error  : {e}")

                raise

            print("\nWorkflow Status")
            print(context.get_all_status())

            print("\nWorkflow Results")
            print(context.get_all_results())

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
            "status": context.get_all_status(),
            "total_execution_time_ms": total_time,
            "results": results
        }
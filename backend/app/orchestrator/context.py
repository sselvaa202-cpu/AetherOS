from app.orchestrator.message_bus import MessageBus
from app.orchestrator.status import AgentStatus


class WorkflowContext:
    """
    Stores shared workflow data between agents.
    """

    def __init__(self, task: str):
        self.task = task

        # Agent results
        self.results = {}

        # Agent status
        self.status = {}

        # Shared Message Bus
        self.message_bus = MessageBus()


    # Results
    def set_result(
        self,
        agent_name: str,
        result,
    ):
        self.results[agent_name] = result

    def get_result(
        self,
        agent_name: str,
    ):
        return self.results.get(agent_name)

    def get_all_results(self):
        return self.results

    # Status
    def set_status(
        self,
        agent_name: str,
        status: AgentStatus,
    ):
        self.status[agent_name] = status.value

    def get_status(
        self,
        agent_name: str,
    ):
        return self.status.get(agent_name)

    def get_all_status(self):
        return self.status
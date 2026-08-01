from app.orchestrator.status import AgentStatus


class WorkflowContext:
    """
    Shared context passed between all agents.
    """

    def __init__(self, task: str):
        self.task = task

        # Stores outputs from agents
        self.results = {}

        # Stores execution status of agents
        self.status = {}


    # Results
    def set_result(self, agent: str, result):
        self.results[agent] = result

    def get_result(self, agent: str):
        return self.results.get(agent)

    def get_all_results(self):
        return self.results

    # Status
    def set_status(self, agent: str, status: AgentStatus):
        self.status[agent] = status

    def get_status(self, agent: str):
        return self.status.get(agent)

    def get_all_status(self):
        return self.status
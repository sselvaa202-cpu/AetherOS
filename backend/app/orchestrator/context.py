class WorkflowContext:
    """
    Shared context passed between AI agents.
    """

    def __init__(self, task: str):
        self.task = task
        self.results = {}

    def add_result(
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

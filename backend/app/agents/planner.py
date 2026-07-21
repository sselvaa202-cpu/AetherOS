from app.agents.base import BaseAgent


class PlannerAgent(BaseAgent):
    """
    AI Planner Agent.
    Responsible for creating execution plans.
    """

    def __init__(self):
        super().__init__(
            name="planner",
            description="Creates execution plans for user tasks."
        )

    def run(
        self,
        task: str
    ):
        return {
            "agent": self.name,
            "task": task,
            "plan": [
                "Analyze the task",
                "Break the task into smaller steps",
                "Assign required tools or agents",
                "Execute each step",
                "Validate the final result"
            ]
        }
    
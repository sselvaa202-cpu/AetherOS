from app.agents.base import BaseAgent


class PlannerAgent(BaseAgent):
    """
    The first AI agent in AetherOS.
    """

    def __init__(self):
        super().__init__(
            name="planner",
            description="Plans and decomposes user tasks."
        )

    def run(
        self,
        task: str
    ):
        return f"Planning task: {task}"
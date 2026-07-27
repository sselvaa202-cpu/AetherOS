from app.agents.base import BaseAgent


class RouterAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="router",
            description="Routes tasks to the appropriate AI agent."
        )

    def run(self, task: str):

        task_lower = task.lower()

        # Complete software development workflow
        if any(word in task_lower for word in [
            "build",
            "develop",
            "create",
            "website",
            "application",
            "system",
            "platform"
        ]):
            return [
                "planner",
                "research",
                "database",
                "coding",
                "reviewer"
            ]

        # Research tasks
        if any(word in task_lower for word in [
            "research",
            "explain",
            "what is",
            "compare",
            "difference",
            "advantages",
            "disadvantages"
        ]):
            return ["research"]

        # Planning tasks
        if any(word in task_lower for word in [
            "plan",
            "roadmap",
            "architecture"
        ]):
            return ["planner"]

        # Database tasks
        if any(word in task_lower for word in [
            "database",
            "schema",
            "sql",
            "postgres",
            "postgresql",
            "mysql",
            "table",
            "query"
        ]):
            return ["database"]

        # Coding tasks
        if any(word in task_lower for word in [
            "code",
            "python",
            "fastapi",
            "react",
            "api",
            "implement",
            "crud",
            "endpoint"
        ]):
            return ["coding"]

        # Default
        return ["planner"]
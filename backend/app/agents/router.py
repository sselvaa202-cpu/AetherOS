import re

from app.agents.base import BaseAgent


class RouterAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="router",
            description="Routes tasks to the appropriate AI agent."
        )

    def run(self, task: str):

        task_lower = task.lower()
        expression = task.replace(" ", "")

    
        # Mathematical Expression
        if re.fullmatch(r"[0-9+\-*/().]+", expression):
            return ["research"]


        # Planner Keywords
        planner_keywords = [
            "plan",
            "roadmap",
            "architecture",
            "design",
        ]

      
        # Research Keywords
        research_keywords = [
            "research",
            "explain",
            "what is",
            "compare",
            "difference",
            "learn",
        ]


        # Database Keywords
        database_keywords = [
            "database",
            "schema",
            "sql",
            "postgres",
            "postgresql",
            "mysql",
            "table",
            "query",
        ]


        # Coding Keywords
        coding_keywords = [
            "code",
            "python",
            "fastapi",
            "react",
            "api",
            "implement",
            "crud",
            "endpoint",
            "backend",
            "frontend",
        ]


        # Full Software Workflow
        if (
            ("build" in task_lower or "develop" in task_lower)
            and any(
                word in task_lower
                for word in [
                    "website",
                    "application",
                    "system",
                    "platform",
                    "software",
                ]
            )
        ):
            return [
                "planner",
                "research",
                "database",
                "coding",
                "reviewer",
            ]


        # Individual Routing
        if any(word in task_lower for word in planner_keywords):
            return ["planner"]

        if any(word in task_lower for word in research_keywords):
            return ["research"]

        if any(word in task_lower for word in database_keywords):
            return ["database"]

        if any(word in task_lower for word in coding_keywords):
            return ["coding"]

 
        # Default
        return ["planner"]
from app.agents.base import BaseAgent
from app.llm.factory import get_llm
from app.llm.prompts.database import build_database_prompt


class DatabaseAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="database",
            description="Designs databases, writes SQL queries, and optimizes schemas."
        )

    def run(self, task: str):

        llm = get_llm()

        prompt = build_database_prompt(task)

        response = llm.generate(prompt)

        return {
            "agent": self.name,
            "task": task,
            "database": response
        }
from app.agents.base import BaseAgent
from app.llm.factory import get_llm
from app.llm.prompts.database import build_database_prompt


class DatabaseAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="database",
            description="Designs databases, writes SQL queries, and optimizes schemas."
        )

    def run(self, task: str,context=None,):

        llm = get_llm()
        planner_result = ""

        if context:
            planner_result = context.get_result("planner") or ""

        print("\n===== Planner Output =====")
        print(planner_result)
        print("==========================\n")

        prompt = build_database_prompt(
            task,
            planner_result,
        )

        response = llm.generate(prompt,max_tokens=100,)
        if context:
            context.add_result(
                self.name,
                response
            )

        return {
            "agent": self.name,
            "task": task,
            "database": response
        }
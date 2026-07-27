from app.agents.base import BaseAgent
from app.llm.factory import get_llm
from app.llm.prompts.coding import build_coding_prompt


class CodingAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="coding",
            description="Generates, explains, and improves source code."
        )

    def run(self, task: str, context=None,):

        llm = get_llm()

        planner_result = ""
        database_result = ""
        if context:
            planner_result = context.get_result("planner") or ""
            database_result = context.get_result("database") or ""

        print("\n===== Planner Output =====")
        print(planner_result)

        print("\n===== Database Output =====")
        print(database_result)
        print("==========================")

        prompt = build_coding_prompt(
            task,
            planner_result,
            database_result
        )

        response = llm.generate(prompt,max_tokens=700,)

        print("\n===== Coding Agent Response =====")
        print(response)
        print("=================================\n")

        if context:
            context.add_result(
                self.name,
                response
            )

        return {
            "agent": self.name,
            "task": task,
            "code": response
        }
from app.agents.base import BaseAgent
from app.llm.factory import get_llm
from app.llm.prompts.reviewer import build_reviewer_prompt


class ReviewerAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="reviewer",
            description="Reviews outputs from other AI agents and suggests improvements."
        )

    def run(self, task: str, context=None):

        llm = get_llm()

        planner_result = ""
        database_result = ""
        coding_result = ""

        if context:
            planner_result = context.get_result("planner") or ""
            database_result = context.get_result("database") or ""
            coding_result = context.get_result("coding") or ""

            print("\n===== Planner Output =====")
            print(planner_result)

            print("\n===== Database Output =====")
            print(database_result)

            print("\n===== Coding Output =====")
            print(coding_result)

            print("==========================\n")

        prompt = build_reviewer_prompt(
            task,
            planner_result,
            database_result,
            coding_result
        )

        response = llm.generate(prompt,max_tokens=200)

        if context:
            context.add_result(
                self.name,
                response
            )

        return {
            "agent": self.name,
            "task": task,
            "review": response
        }
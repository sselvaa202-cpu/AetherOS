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
        coding_messages = []

        if context:

            planner_data = context.get_result("planner")
            database_data = context.get_result("database")
            coding_data = context.get_result("coding")

            # Extract planner output
            if isinstance(planner_data, dict):
                planner_result = planner_data.get("plan", "")
            else:
                planner_result = planner_data or ""

            # Extract database output
            if isinstance(database_data, dict):
                database_result = database_data.get("database", "")
            else:
                database_result = database_data or ""

            # Extract coding output
            if isinstance(coding_data, dict):
                coding_result = coding_data.get("code", "")
            else:
                coding_result = coding_data or ""

            # Receive messages from Coding Agent
            coding_messages = context.message_bus.receive_messages(
                self.name
            )

            print("\n===== Reviewer Received Messages =====")

            for msg in coding_messages:
                print(f"From    : {msg.sender}")
                print(f"Message : {msg.content}")

            print("======================================\n")

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

        response = llm.generate(
            prompt,
            max_tokens=200
        )

        result = {
            "agent": self.name,
            "task": task,
            "review": response
        }

        if context:
            context.set_result(
                self.name,
                result
            )

        return result
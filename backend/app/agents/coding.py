from app.agents.base import BaseAgent
from app.llm.factory import get_llm
from app.llm.prompts.coding import build_coding_prompt


class CodingAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="coding",
            description="Generates, explains, and improves source code."
        )

    def run(self, task: str, context=None):

        llm = get_llm()

        planner_result = ""
        database_result = ""
        database_messages = []

        if context:
            planner_data = context.get_result("planner")
            database_data = context.get_result("database")

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

            # Receive messages from Database Agent
            database_messages = context.message_bus.receive_messages(
                self.name
            )

        print("\n===== Coding Received Messages =====")

        for msg in database_messages:
            print(f"From    : {msg.sender}")
            print(f"Message : {msg.content}")

        print("====================================\n")

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

        response = llm.generate(
            prompt,
            max_tokens=700,
        )

        print("\n===== Coding Agent Response =====")
        print(response)
        print("=================================\n")

        result = {
            "agent": self.name,
            "task": task,
            "code": response
        }

        if context:
            # Store result
            context.set_result(
                self.name,
                result
            )

            # Send message to Reviewer Agent
            context.message_bus.send_message(
                sender=self.name,
                receiver="reviewer",
                content="Implementation completed. Please review the solution."
            )


        return result
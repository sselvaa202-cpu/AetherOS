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
        planner_messages = []

        if context:
            planner_result = context.get_result("planner") or ""

            # Receive messages sent to Database Agent
            planner_messages = context.message_bus.receive_messages(
                self.name
            )

            print("\n===== Database Received Messages =====")

            for msg in planner_messages:
                print(f"From : {msg.sender}")
                print(f"Message : {msg.content}")

            print("======================================\n")


        print("\n===== Planner Output =====")
        print(planner_result)
        print("==========================\n")

        prompt = build_database_prompt(
            task,
            planner_result,
        )

        response = llm.generate(prompt,max_tokens=250,)

        print("\n===== Database Response =====")
        print(repr(response))
        print("============================\n")

        if context:
            context.set_result(
                self.name,
                response
            )

                # Notify Coding Agent
            context.message_bus.send_message(
                sender=self.name,
                receiver="coding",
                content="Database schema is complete. Start backend implementation."
            )

        return {
            "agent": self.name,
            "task": task,
            "database": response
        }
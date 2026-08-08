from app.agents.base import BaseAgent
from app.llm.factory import get_llm
from app.llm.prompts.planner import build_planner_prompt


class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="planner",
            description="Breaks a task into an execution plan."
        )

    def run(self, task: str,context=None):

        llm = get_llm()

        prompt = build_planner_prompt(task)

        response = llm.generate(prompt,max_tokens=400,)

        print("\n===== Planner Response =====")
        print(repr(response))
        print("============================\n")

        if context:
             # Store planner output
             context.set_result(
                 self.name,
                response
             )

             # Send message to Database Agent
             context.message_bus.send_message(
                sender=self.name,
                receiver="database",
                content="Execution plan is ready. Design the PostgreSQL database schema."
             )


        return {
            "agent": self.name,
            "task": task,
            "plan": response
        }
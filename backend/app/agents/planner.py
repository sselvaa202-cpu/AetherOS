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

        response = llm.generate(prompt,max_tokens=100,)
        if context:
             context.add_result(
                 self.name,
                response
             )

        return {
            "agent": self.name,
            "task": task,
            "plan": response
        }
from app.agents.base import BaseAgent
from app.llm.factory import get_llm
from app.llm.prompts.coding import build_coding_prompt


class CodingAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="coding",
            description="Generates, explains, and improves source code."
        )

    def run(self, task: str):

        llm = get_llm()

        prompt = build_coding_prompt(task)

        response = llm.generate(prompt)

        return {
            "agent": self.name,
            "task": task,
            "code": response
        }
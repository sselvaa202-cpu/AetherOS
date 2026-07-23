from app.agents.base import BaseAgent
from app.llm.factory import get_llm
from app.llm.prompts.research import build_research_prompt


class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="research",
            description="Researches topics and provides detailed information."
        )

    def run(self, task: str):

        llm = get_llm()

        prompt = build_research_prompt(task)

        response = llm.generate(prompt)

        return {
            "agent": self.name,
            "task": task,
            "research": response
        }
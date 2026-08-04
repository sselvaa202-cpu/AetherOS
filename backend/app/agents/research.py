import re

from app.agents.base import BaseAgent
from app.llm.factory import get_llm
from app.llm.prompts.research import build_research_prompt

from app.tools.manager import ToolManager
from app.tools.calculator import CalculatorTool

from app.memory.prompt_builder import build_conversation_prompt


class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="research",
            description="Researches topics and provides detailed information."
        )

    def run(self, task: str, context=None):

        # Get Conversation Memory
        conversation_memory = None

        if context:
            conversation_memory = context.get_memory("conversation")

            if conversation_memory:
                conversation_memory.save(
                    "user",
                    task
                )

        # Tool Manager
        tool_manager = ToolManager()

        tool_manager.register_tool(
            CalculatorTool()
        )

        # Calculator Detection
        expression = task.replace(" ", "")

        if re.fullmatch(r"[0-9+\-*/().]+", expression):

            result = tool_manager.execute(
                "calculator",
                expression
            )

            if conversation_memory:
                conversation_memory.save(
                    "assistant",
                    str(result)
                )

            result_data = {
                "agent": self.name,
                "task": task,
                "research": str(result),
                "tool_used": "calculator",
            }

            if context:
                context.set_result(
                    self.name,
                    result_data
                )

            return result_data

        # LLM
        llm = get_llm()

        history = []

        if conversation_memory:
            history = conversation_memory.get_all()

        conversation_prompt = build_conversation_prompt(
            history,
            task
        )

        prompt = build_research_prompt(
            conversation_prompt
        )

        print("\n===== Prompt Sent To LLM =====")
        print(prompt)
        print("==============================\n")

        response = llm.generate(
            prompt,
            max_tokens=100,
        )

        # Save Assistant Response
        if conversation_memory:
            conversation_memory.save(
                "assistant",
                response
            )

            print("\n===== Conversation Memory =====")
            print(conversation_memory.get_all())
            print("===============================\n")

        result = {
            "agent": self.name,
            "task": task,
            "research": response,
        }

        if context:
            context.set_result(
                self.name,
                result,
            )

        return result
from app.tools.base import BaseTool


class ToolRegistry:
    """
    Stores all registered tools.
    """

    def __init__(self):
        self.tools = {}

    def register(self, tool: BaseTool):
        self.tools[tool.name] = tool

    def unregister(self, name: str):
        self.tools.pop(name, None)

    def get(self, name: str):
        return self.tools.get(name)

    def get_all(self):
        return self.tools

    def exists(self, name: str):
        return name in self.tools
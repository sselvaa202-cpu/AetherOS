from app.tools.registry import ToolRegistry


class ToolManager:
    """
    Manages and executes registered tools.
    """

    def __init__(self):
        self.registry = ToolRegistry()

    def register_tool(self, tool):
        """
        Register a new tool.
        """
        self.registry.register(tool)

    def unregister_tool(self, tool_name: str):
        """
        Remove a registered tool.
        """
        self.registry.unregister(tool_name)

    def get_tool(self, tool_name: str):
        """
        Retrieve a tool by name.
        """
        return self.registry.get(tool_name)

    def execute(self, tool_name: str, *args, **kwargs):
        """
        Execute a registered tool.
        """
        tool = self.get_tool(tool_name)

        if tool is None:
            raise ValueError(
                f"Tool '{tool_name}' is not registered."
            )

        return tool.execute(*args, **kwargs)

    def get_all_tools(self):
        """
        Return all registered tools.
        """
        return self.registry.get_all()
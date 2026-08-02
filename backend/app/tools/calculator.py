from app.tools.base import BaseTool


class CalculatorTool(BaseTool):
    """
    Performs basic mathematical calculations.
    """

    def __init__(self):
        super().__init__(
            name="calculator",
            description="Performs arithmetic calculations."
        )

    def execute(self, expression: str):
        """
        Execute a mathematical expression.
        """

        try:
            result = eval(
                expression,
                {"__builtins__": {}},
                {}
            )

            return result

        except Exception as e:
            return f"Calculation Error: {e}"
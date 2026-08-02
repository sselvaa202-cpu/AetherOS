from app.tools.manager import ToolManager
from app.tools.calculator import CalculatorTool


def main():

    manager = ToolManager()

    # Register Calculator Tool
    manager.register_tool(
        CalculatorTool()
    )

    print("===== Registered Tools =====")
    print(manager.get_all_tools().keys())


if __name__ == "__main__":
    main()
    
from app.agents.manager import AgentManager
from app.agents.coding import CodingAgent


print("=" * 80)
print("AGENT EXECUTION TEST")
print("=" * 80)


manager = AgentManager()

manager.register_agent(
    CodingAgent()
)


print("\nExecuting Coding Agent...")


result = manager.execute_agent(
    name="coding",
    task="Explain Python decorators with a simple example."
)


print("\n===== EXECUTION RESULT =====")
print(result)
print("============================")


print("\n" + "=" * 80)
print("AGENT EXECUTION TEST COMPLETED")
print("=" * 80)
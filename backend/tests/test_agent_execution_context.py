from app.agents.manager import AgentManager
from app.agents.planner import PlannerAgent
from app.orchestrator.context import WorkflowContext


print("=" * 80)
print("AGENT EXECUTION CONTEXT TEST")
print("=" * 80)


# Create manager
manager = AgentManager()

# Register Planner Agent
manager.register_agent(
    PlannerAgent()
)


# Create workflow context
context = WorkflowContext(
    task="Create a simple task management application with users and CRUD operations.",
    session_id="test-session-001",
)


print("\nWorkflow Context Created")
print("Task:", context.task)
print("Session ID:", context.session_id)


# Execute Planner Agent
print("\nExecuting Planner Agent...")

result = manager.execute_agent(
    name="planner",
    task=context.task,
    context=context,
)


print("\n===== PLANNER RESULT =====")
print(result)
print("===========================")


# Check stored result
stored_result = context.get_result("planner")

print("\n===== STORED RESULT =====")
print(stored_result)
print("=========================")


# Check all results
print("\n===== ALL WORKFLOW RESULTS =====")
print(context.get_all_results())
print("================================")


print("\n" + "=" * 80)
print("AGENT EXECUTION CONTEXT TEST COMPLETED")
print("=" * 80)
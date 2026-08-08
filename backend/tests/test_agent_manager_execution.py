from app.agents.manager import AgentManager
from app.agents.coding import CodingAgent
from app.agents.database import DatabaseAgent
from app.agents.planner import PlannerAgent
from app.agents.research import ResearchAgent


print("=" * 80)
print("AGENT MANAGER EXECUTION TEST")
print("=" * 80)


manager = AgentManager()


# Register executable agents
manager.register_agent(CodingAgent())
manager.register_agent(DatabaseAgent())
manager.register_agent(PlannerAgent())
manager.register_agent(ResearchAgent())


print("\nRegistered executable agents:")

for agent in manager.list_agents():
    print(agent.name)


print("\nTotal executable agents:", len(manager.list_agents()))


# Test retrieval
coding_agent = manager.get_agent("coding")

print("\nCoding agent:")
print(coding_agent)


# Test unknown agent
unknown_agent = manager.get_agent("unknown")

print("\nUnknown agent:")
print(unknown_agent)


print("\n" + "=" * 80)
print("AGENT MANAGER EXECUTION TEST COMPLETED")
print("=" * 80)
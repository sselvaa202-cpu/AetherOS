from app.agents.manager import AgentManager


manager = AgentManager()


print("=" * 80)
print("AGENT MANAGER TEST")
print("=" * 80)


agents = manager.list_agents()

print("Registered agents:")
print(agents)

print()
print("Total agents:", len(agents))


coding_agent = manager.get_agent("coding")

print()
print("Coding agent:")
print(coding_agent)


general_agent = manager.get_agent("general")

print()
print("General agent:")
print(general_agent)


unknown_agent = manager.get_agent("unknown")

print()
print("Unknown agent:")
print(unknown_agent)


print("=" * 80)
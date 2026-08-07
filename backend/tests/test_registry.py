from app.registry.agent_registry import registry


print("\n=== Agent Registry Test ===\n")

agents = registry.get_all()

# Test 1: Number of agents
print("Total agents:", len(agents))

assert len(agents) == 15


# Test 2: Agent names
expected_agents = {
    "general",
    "coding",
    "database",
    "research",
    "planner",
    "data_analysis",
    "testing",
    "documentation",
    "customer_support",
    "email",
    "calendar",
    "finance",
    "uiux",
    "voice",
    "devops",
}

actual_agents = {
    agent.name
    for agent in agents
}

assert actual_agents == expected_agents

print("All 15 agents registered: PASS")


# Test 3: Validate specifications
for agent in agents:

    assert agent.name
    assert agent.description
    assert agent.priority
    assert agent.supported_tasks
    assert agent.tools
    assert agent.memory_read is not None
    assert agent.memory_write is not None
    assert agent.status

print("All AgentSpecs are valid: PASS")


# Test 4: Coding Agent
coding = registry.get("coding")

assert coding is not None
assert "github" in coding.tools
assert "python" in coding.tools

print("Coding Agent specification: PASS")


# Test 5: Database Agent
database = registry.get("database")

assert database is not None
assert "postgresql" in database.tools
assert "mysql" in database.tools

print("Database Agent specification: PASS")


# Test 6: General Agent
general = registry.get("general")

assert general is not None
assert "conversation_memory" in general.tools
assert "long_term_memory" in general.tools

print("General Agent specification: PASS")


print("\n=== All Tests Passed ===")
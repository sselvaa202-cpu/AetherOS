from app.agents.router.router_schema import RouterDecision
from app.agents.router.validator import RouterValidator


validator = RouterValidator()


print("=" * 80)
print("ROUTER VALIDATOR TEST")
print("=" * 80)


# TEST 1: Valid decision

decision = RouterDecision(
    intent="coding",
    confidence=0.99,
    reason="Programming request.",
    recommended_agents=["coding"],
)

result = validator.validate(decision)

print("\nTEST 1: Valid coding agent")
print(result)


# TEST 2: Unknown agent

decision = RouterDecision(
    intent="unknown_agent",
    confidence=0.95,
    reason="Unknown request.",
    recommended_agents=["unknown_agent"],
)

result = validator.validate(decision)

print("\nTEST 2: Unknown agent")
print(result)


# TEST 3: Unknown intent but valid recommended agent

decision = RouterDecision(
    intent="something_unknown",
    confidence=0.80,
    reason="Testing fallback.",
    recommended_agents=["database"],
)

result = validator.validate(decision)

print("\nTEST 3: Unknown intent + valid recommendation")
print(result)


# TEST 4: Multiple agents

decision = RouterDecision(
    intent="data_analysis",
    confidence=0.95,
    reason="Data analysis request.",
    recommended_agents=[
        "data_analysis",
        "documentation",
    ],
)

result = validator.validate(decision)

print("\nTEST 4: Multiple valid agents")
print(result)


# TEST 5: Completely invalid agents

decision = RouterDecision(
    intent="something_unknown",
    confidence=0.50,
    reason="Invalid routing.",
    recommended_agents=[
        "fake_agent",
        "another_fake_agent",
    ],
)

result = validator.validate(decision)

print("\nTEST 5: Completely invalid agents")
print(result)


print("\n" + "=" * 80)
print("VALIDATOR TEST COMPLETED")
print("=" * 80)
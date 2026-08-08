from app.agents.router.router_agent import RouterAgent
from app.agents.manager import AgentManager


router = RouterAgent()
manager = AgentManager()


test_messages = [
    "Explain Python decorators",
    "Write a PostgreSQL query to find duplicate users",
    "Research the latest FastAPI features",
    "Analyze this CSV file and find the sales trend",
    "Create a plan for building a web application",
    "My name is Selvaa",
]


print("=" * 80)
print("ROUTER → AGENT MANAGER TEST")
print("=" * 80)


for message in test_messages:

    print()
    print("-" * 80)
    print("USER:", message)

    # Step 1: Router
    decision = router.route(message)

    print()
    print("ROUTER DECISION:")
    print("Intent:", decision.intent)
    print("Confidence:", decision.confidence)
    print("Reason:", decision.reason)
    print(
        "Recommended agents:",
        decision.recommended_agents
    )

    # Step 2: Agent Manager
    agent = manager.get_agent(
        decision.intent
    )

    print()
    print("SELECTED AGENT:")
    print(agent)

    # Step 3: Validate selection
    if agent is None:
        print("STATUS: FAIL")
    else:
        print("STATUS: PASS")


print()
print("=" * 80)
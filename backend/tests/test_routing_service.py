from app.routing.routing_service import RoutingService


service = RoutingService()


print("=" * 80)
print("ROUTING SERVICE TEST")
print("=" * 80)


test_messages = [
    "Explain Python decorators",
    "Write a PostgreSQL query to find duplicate users",
    "Research the latest FastAPI features",
    "Analyze this CSV and find the sales trend",
    "Create a plan for building a web application",
    "My name is Selvaa",
]


for message in test_messages:

    print("\n" + "-" * 80)
    print("USER:", message)

    decision, agent = service.route_and_get_agent(
        message
    )

    print("INTENT:", decision.intent)
    print("CONFIDENCE:", decision.confidence)
    print("REASON:", decision.reason)
    print(
        "RECOMMENDED AGENTS:",
        decision.recommended_agents
    )

    if agent:
        print("SELECTED AGENT:", agent.name)
    else:
        print("SELECTED AGENT: None")


print("\n" + "=" * 80)
print("ROUTING SERVICE TEST COMPLETED")
print("=" * 80)
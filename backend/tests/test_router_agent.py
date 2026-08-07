from app.agents.router.router_agent import RouterAgent


router = RouterAgent()


def test_router(message: str):
    print("\n" + "=" * 80)
    print("USER:", message)

    decision = router.route(message)

    print("INTENT:", decision.intent)
    print("CONFIDENCE:", decision.confidence)
    print("REASON:", decision.reason)
    print("RECOMMENDED AGENTS:", decision.recommended_agents)

    print("=" * 80)


if __name__ == "__main__":

    test_router("Explain Python decorators")

    test_router("Write a PostgreSQL query to find duplicate users")

    test_router("Research the latest FastAPI features")

    test_router("Analyze this CSV file and find the sales trend")

    test_router("Create a plan for building a web application")

    test_router("My name is Selvaa")
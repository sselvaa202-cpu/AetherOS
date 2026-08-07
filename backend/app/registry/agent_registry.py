from app.registry.agent_spec import AgentSpec


class AgentRegistry:
    """
    Central registry for all AetherOS agents.
    """

    def __init__(self):
        self._agents: dict[str, AgentSpec] = {}

    def register(self, agent: AgentSpec):
        self._agents[agent.name] = agent

    def get(self, name: str) -> AgentSpec | None:
        return self._agents.get(name)

    def get_all(self) -> list[AgentSpec]:
        return list(self._agents.values())

    def exists(self, name: str) -> bool:
        return name in self._agents


registry = AgentRegistry()


# GENERAL AGENT

registry.register(
    AgentSpec(
        name="general",
        description="Handles normal conversation and general user interaction.",
        priority="core",
        supported_tasks=[
            "normal conversation",
            "greetings",
            "general questions",
            "casual conversation",
        ],
        tools=[
            "conversation_memory",
            "long_term_memory",
            "llm",
        ],
        memory_read=[
            "conversation",
            "long_term",
        ],
        memory_write=[
            "conversation",
            "long_term",
        ],
        status="active",
    )
)


# CODING AGENT

registry.register(
    AgentSpec(
        name="coding",
        description="Writes, fixes, reviews and explains software.",
        priority="core",
        supported_tasks=[
            "generate code",
            "debug code",
            "refactor code",
            "write unit tests",
            "review code",
            "explain algorithms",
        ],
        tools=[
            "github",
            "vscode",
            "terminal",
            "python",
            "compiler",
            "documentation",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# DATABASE AGENT

registry.register(
    AgentSpec(
        name="database",
        description="Handles SQL, databases and database-related tasks.",
        priority="core",
        supported_tasks=[
            "write sql queries",
            "optimize sql",
            "design database schema",
            "create tables",
            "database analysis",
            "database reports",
        ],
        tools=[
            "postgresql",
            "mysql",
            "sqlite",
            "mongodb",
            "oracle",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# RESEARCH AGENT

registry.register(
    AgentSpec(
        name="research",
        description="Finds, analyzes and summarizes information.",
        priority="core",
        supported_tasks=[
            "web research",
            "search information",
            "read research papers",
            "compare technologies",
            "fact checking",
            "summarize articles",
            "create research reports",
        ],
        tools=[
            "web_search",
            "pdf",
            "academic_api",
            "summarizer",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# PLANNER AGENT

registry.register(
    AgentSpec(
        name="planner",
        description="Creates structured plans, workflows and task breakdowns.",
        priority="core",
        supported_tasks=[
            "create plan",
            "project planning",
            "task breakdown",
            "workflow generation",
            "roadmap creation",
        ],
        tools=[
            "workflow_generator",
            "markdown",
            "mermaid",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# DATA ANALYSIS AGENT

registry.register(
    AgentSpec(
        name="data_analysis",
        description="Analyzes data and discovers useful patterns and insights.",
        priority="specialized",
        supported_tasks=[
            "clean data",
            "analyze data",
            "find trends",
            "calculate statistics",
            "create charts",
            "generate dashboards",
            "predict outcomes",
        ],
        tools=[
            "pandas",
            "numpy",
            "csv",
            "excel",
            "charts",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# TESTING AGENT

registry.register(
    AgentSpec(
        name="testing",
        description="Tests software, APIs and applications for defects and quality.",
        priority="specialized",
        supported_tasks=[
            "functional testing",
            "api testing",
            "ui testing",
            "performance testing",
            "write tests",
            "bug reporting",
        ],
        tools=[
            "pytest",
            "playwright",
            "selenium",
            "postman",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# DOCUMENTATION AGENT

registry.register(
    AgentSpec(
        name="documentation",
        description="Creates and maintains technical and project documentation.",
        priority="specialized",
        supported_tasks=[
            "write documentation",
            "create readme",
            "write api documentation",
            "create user manuals",
            "create technical guides",
            "write code comments",
        ],
        tools=[
            "markdown",
            "readme_generator",
            "api_docs",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# CUSTOMER SUPPORT AGENT

registry.register(
    AgentSpec(
        name="customer_support",
        description="Handles customer questions, support requests and ticket workflows.",
        priority="specialized",
        supported_tasks=[
            "answer customer questions",
            "resolve support tickets",
            "answer faq",
            "product guidance",
            "escalate issues",
        ],
        tools=[
            "faq_search",
            "memory",
            "ticket_handler",
        ],
        memory_read=[
            "conversation",
            "long_term",
        ],
        memory_write=[
            "conversation",
            "long_term",
        ],
        status="active",
    )
)


# EMAIL AGENT

registry.register(
    AgentSpec(
        name="email",
        description="Manages email-related tasks and communication.",
        priority="specialized",
        supported_tasks=[
            "read emails",
            "reply to emails",
            "summarize inbox",
            "categorize emails",
            "draft email",
            "schedule follow up",
        ],
        tools=[
            "gmail",
            "outlook",
            "summarizer",
            "draft_generator",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# CALENDAR AGENT

registry.register(
    AgentSpec(
        name="calendar",
        description="Manages schedules, meetings, appointments and reminders.",
        priority="specialized",
        supported_tasks=[
            "book meeting",
            "find free time",
            "send reminder",
            "cancel meeting",
            "manage appointment",
        ],
        tools=[
            "calendar_api",
            "reminder_engine",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# FINANCE AGENT

registry.register(
    AgentSpec(
        name="finance",
        description="Handles financial calculations, budgets and financial data.",
        priority="specialized",
        supported_tasks=[
            "expense tracking",
            "budget planning",
            "invoice generation",
            "financial analysis",
            "tax calculations",
        ],
        tools=[
            "calculator",
            "budget_engine",
            "csv",
            "excel",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# UI/UX AGENT

registry.register(
    AgentSpec(
        name="uiux",
        description="Designs user interfaces and improves user experience.",
        priority="specialized",
        supported_tasks=[
            "design ui",
            "design ux",
            "create wireframe",
            "suggest color palette",
            "design user flow",
            "accessibility review",
        ],
        tools=[
            "figma",
            "html_preview",
            "color_palette_generator",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# VOICE AGENT

registry.register(
    AgentSpec(
        name="voice",
        description="Handles speech, voice commands and voice-based interaction.",
        priority="specialized",
        supported_tasks=[
            "speech to text",
            "text to speech",
            "voice commands",
            "voice assistant",
            "call automation",
        ],
        tools=[
            "whisper",
            "text_to_speech",
            "speech_to_text",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)


# DEVOPS AGENT

registry.register(
    AgentSpec(
        name="devops",
        description="Handles deployment, infrastructure and application operations.",
        priority="specialized",
        supported_tasks=[
            "ci cd",
            "docker",
            "kubernetes",
            "deployment",
            "server monitoring",
            "infrastructure automation",
        ],
        tools=[
            "docker",
            "kubernetes",
            "github_actions",
            "linux_terminal",
        ],
        memory_read=[
            "conversation",
        ],
        memory_write=[
            "conversation",
        ],
        status="active",
    )
)
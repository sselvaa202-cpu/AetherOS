from fastapi import APIRouter, HTTPException

from app.agents.manager import AgentManager
from app.agents.planner import PlannerAgent
from app.agents.research import ResearchAgent
from app.agents.coding import CodingAgent
from app.agents.database import DatabaseAgent
from app.agents.router import RouterAgent

from app.schemas.agent import (
    AgentRequest,
    TaskRequest,
)
router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)

# Agent Manager
manager = AgentManager()

# Agent Instances
router_agent = RouterAgent()
planner = PlannerAgent()
research = ResearchAgent()
coding = CodingAgent()
database = DatabaseAgent()

# Register all agents
manager.register_agent(router_agent)
planner = PlannerAgent()
manager.register_agent(ResearchAgent())
manager.register_agent(CodingAgent())
manager.register_agent(DatabaseAgent())


# List All Agents
@router.get("/")
def list_agents():

    return {
        "message": "Agent framework initialized",
        "agents": manager.list_agents()
    }

@router.post("/run")
def run_agent(request: AgentRequest):

    agent = manager.get_agent(request.agent_name)

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )

    result = agent.run(request.task)

# Automatic Routing (New Endpoint)
@router.post("/execute")
def execute_task(request: TaskRequest):

    # Ask Router which agent should execute the task
    selected_agent_name = router_agent.run(request.task)

    # Retrieve that agent
    agent = manager.get_agent(selected_agent_name)

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Selected agent not found"
        )

    # Execute task
    return agent.run(request.task)
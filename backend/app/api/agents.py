from fastapi import APIRouter, HTTPException

from app.agents.manager import AgentManager
from app.agents.planner import PlannerAgent
from app.agents.research import ResearchAgent
from app.agents.coding import CodingAgent
from app.agents.database import DatabaseAgent
from app.agents.router import RouterAgent
from app.orchestrator.orchestrator import Orchestrator
from app.agents.reviewer import ReviewerAgent

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
reviewer = ReviewerAgent()

# Register all agents
manager.register_agent(router_agent())
manager.register_agent(PlannerAgent())
manager.register_agent(ResearchAgent())
manager.register_agent(CodingAgent())
manager.register_agent(DatabaseAgent())
manager.register_agent(ReviewerAgent())

# Create Orchestrator
orchestrator = Orchestrator(manager)


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
    
    return result

# Automatic Routing (New Endpoint)
@router.post("/execute")
def execute_task(request: TaskRequest):

    try:
        return orchestrator.execute(request.task,request.session_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

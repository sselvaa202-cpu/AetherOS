from fastapi import APIRouter, HTTPException

from app.agents.manager import AgentManager
from app.agents.planner import PlannerAgent

from app.schemas.agent import (
    AgentRequest,
    AgentResponse,
)
router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)

manager = AgentManager()

planner = PlannerAgent()

manager.register_agent(planner)


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
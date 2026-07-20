from fastapi import APIRouter

from app.agents.manager import AgentManager
from app.agents.planner import PlannerAgent

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
from app.orchestrator.message_bus import MessageBus
from app.orchestrator.status import AgentStatus

from app.memory.session_store import session_manager


class WorkflowContext:
    """
    Stores shared workflow data between agents.
    """

    def __init__(
        self,
        task: str,
        session_id: str,
    ):
        self.task = task
        self.session_id = session_id

        # Agent results
        self.results = {}

        # Agent status
        self.status = {}

        # Shared Message Bus
        self.message_bus = MessageBus()

        # Shared Conversation Memory for this session
        self.conversation_memory = session_manager.get_conversation(
            session_id
        )
        
    # Results
    def set_result(
        self,
        agent_name: str,
        result,
    ):
        self.results[agent_name] = result

    def get_result(
        self,
        agent_name: str,
    ):
        return self.results.get(agent_name)

    def get_all_results(self):
        return self.results
    
    # Status
    def set_status(
        self,
        agent_name: str,
        status: AgentStatus,
    ):
        self.status[agent_name] = status.value

    def get_status(
        self,
        agent_name: str,
    ):
        return self.status.get(agent_name)

    def get_all_status(self):
        return self.status
    
    # Memory
    def get_memory(
        self,
        name: str,
    ):
        """
        Return the requested memory.
        """

        if name == "conversation":
            return self.conversation_memory

        return None

    def get_all_memories(self):
        """
        Return all memories for this workflow.
        """

        return {
            "conversation": self.conversation_memory
        }
from app.orchestrator.message_bus import MessageBus
from app.orchestrator.status import AgentStatus

from app.memory.manager import MemoryManager
from app.memory.conversation import ConversationMemory


class WorkflowContext:
    """
    Stores shared workflow data between agents.
    """

    def __init__(self, task: str):
        self.task = task

        # Agent results
        self.results = {}

        # Agent status
        self.status = {}

        # Shared Message Bus
        self.message_bus = MessageBus()

        # Memory Manager
        self.memory_manager = MemoryManager()

        # Register Conversation Memory
        self.memory_manager.register_memory(
            ConversationMemory()
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
        Return a registered memory instance.
        """
        return self.memory_manager.get_memory(name)

    def get_all_memories(self):
        """
        Return all registered memories.
        """
        return self.memory_manager.get_all_memories()
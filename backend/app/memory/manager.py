from app.memory.base import BaseMemory


class MemoryManager:
    """
    Manages all memory implementations.
    """

    def __init__(self):
        self._memories = {}

    def register_memory(
        self,
        memory: BaseMemory,
    ):
        """
        Register a memory implementation.
        """
        self._memories[memory.name] = memory

    def get_memory(
        self,
        name: str,
    ):
        """
        Get a memory by name.
        """
        return self._memories.get(name)

    def remove_memory(
        self,
        name: str,
    ):
        """
        Remove a registered memory.
        """
        self._memories.pop(name, None)

    def get_all_memories(self):
        """
        Return all registered memories.
        """
        return self._memories
from abc import ABC, abstractmethod


class BaseMemory(ABC):
    """
    Base class for all memory implementations.
    """

    def __init__(
        self,
        name: str,
        description: str,
    ):
        self.name = name
        self.description = description

    @abstractmethod
    def save(self, key: str, value):
        """
        Store a memory item.
        """
        pass

    @abstractmethod
    def get(self, key: str):
        """
        Retrieve a memory item.
        """
        pass

    @abstractmethod
    def delete(self, key: str):
        """
        Delete a memory item.
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clear all memory.
        """
        pass
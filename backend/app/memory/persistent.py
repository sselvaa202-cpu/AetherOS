from abc import ABC, abstractmethod


class PersistentMemory(ABC):
    """
    Base interface for persistent memory storage.
    """

    @abstractmethod
    def save(
        self,
        session_id: str,
        role: str,
        content: str,
    ):
        """
        Save a message.
        """
        pass

    @abstractmethod
    def load(
        self,
        session_id: str,
    ):
        """
        Load all messages for a session.
        """
        pass

    @abstractmethod
    def delete(
        self,
        session_id: str,
    ):
        """
        Delete one session.
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Delete every stored conversation.
        """
        pass
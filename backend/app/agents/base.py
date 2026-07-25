from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Base class for all AI agents.
    """

    def __init__(
        self,
        name: str,
        description: str,
    ):
        self.name = name
        self.description = description

    @abstractmethod
    def run(
        self,
        task: str,
        context=None,
    ):
        """
        Execute the assigned task.
        """
        pass
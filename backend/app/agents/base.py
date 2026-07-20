from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Base class for all AetherOS AI agents.
    """

    def __init__(
        self,
        name: str,
        description: str
    ):
        self.name = name
        self.description = description

    @abstractmethod
    def run(
        self,
        task: str
    ):
        """
        Execute the given task.
        """
        pass
    
from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Base class for all AetherOS tools.
    """

    def __init__(
        self,
        name: str,
        description: str,
    ):
        self.name = name
        self.description = description

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Execute the tool.
        """
        pass
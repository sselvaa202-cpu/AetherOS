from app.memory.base import BaseMemory


class ShortTermMemory(BaseMemory):
    """
    In-memory storage for temporary workflow data.
    """

    def __init__(self):
        super().__init__(
            name="short_term",
            description="Stores temporary workflow information."
        )

        self._storage = {}

    def save(
        self,
        key: str,
        value,
    ):
        self._storage[key] = value

    def get(
        self,
        key: str,
    ):
        return self._storage.get(key)

    def delete(
        self,
        key: str,
    ):
        self._storage.pop(key, None)

    def clear(self):
        self._storage.clear()

    def get_all(self):
        """
        Return all stored items.
        """
        return self._storage
from app.memory.base import BaseMemory


class ConversationMemory(BaseMemory):
    """
    Stores conversation history between the user and the assistant.
    """

    def __init__(
        self,
        max_messages: int = 20,
    ):
        super().__init__(
            name="conversation",
            description="Stores conversation history."
        )

        self.max_messages = max_messages
        self._messages = []

    def save(
        self,
        role: str,
        content: str,
    ):
        """
        Save a conversation message.
        """

        self._messages.append(
            {
                "role": role,
                "content": content,
            }
        )

        # Keep only the latest messages
        if len(self._messages) > self.max_messages:
            self._messages.pop(0)

    def get(
        self,
        index: int,
    ):
        """
        Get a message by index.
        """

        if 0 <= index < len(self._messages):
            return self._messages[index]

        return None

    def get_all(self):
        """
        Return the complete conversation.
        """

        return self._messages

    def delete(
        self,
        index: int,
    ):
        """
        Delete one message.
        """

        if 0 <= index < len(self._messages):
            self._messages.pop(index)

    def clear(self):
        """
        Clear the conversation history.
        """

        self._messages.clear()
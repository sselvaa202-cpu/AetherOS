from app.memory.base import BaseMemory
from app.db.session import SessionLocal
from app.services.conversation_service import ConversationService


class ConversationMemory(BaseMemory):
    """
    Stores conversation history.
    """

    def __init__(
        self,
        session_id: str,
        max_messages: int = 20,
    ):
        super().__init__(
            name="conversation",
            description="Stores conversation history."
        )

        self.session_id = session_id
        self.max_messages = max_messages
        self._messages = []

        # Database
        self.db = SessionLocal()
        self.service = ConversationService(self.db)

        # Load previous conversation from PostgreSQL
        messages = self.service.get_messages(
            self.session_id
        )

        self._messages = [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in messages
        ]

        # Debug (Temporary)
        print("\n===== Loaded Conversation =====")
        print(self._messages)
        print("===============================\n")

    def save(
        self,
        role: str,
        content: str,
    ):
        """
        Save a conversation message.
        """

        # Save in memory
        self._messages.append(
            {
                "role": role,
                "content": content,
            }
        )

        # Save in PostgreSQL
        self.service.save_message(
            session_id=self.session_id,
            role=role,
            content=content,
        )

        # Keep only recent messages in RAM
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
        Return all conversation messages.
        """
        return self._messages

    def delete(
        self,
        index: int,
    ):
        """
        Delete a message.
        """
        if 0 <= index < len(self._messages):
            self._messages.pop(index)

    def clear(self):
        """
        Clear conversation memory.
        """
        self._messages.clear()
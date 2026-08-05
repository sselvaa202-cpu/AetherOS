import uuid

from sqlalchemy.orm import Session

from app.models.conversation import (
    Conversation,
    ConversationMessage,
)


class ConversationService:
    """
    Handles conversation persistence.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_conversation(
        self,
        session_id: str,
    ):
        """
        Return an existing conversation.
        """

        return (
            self.db.query(Conversation)
            .filter(
                Conversation.session_id == session_id
            )
            .first()
        )

    def create_conversation(
        self,
        session_id: str,
    ):
        """
        Create a new conversation.
        """

        conversation = Conversation(
            session_id=session_id
        )

        self.db.add(conversation)
        self.db.commit()
        self.db.refresh(conversation)

        return conversation

    def get_or_create_conversation(
        self,
        session_id: str,
    ):
        """
        Get an existing conversation or create a new one.
        """

        conversation = self.get_conversation(
            session_id
        )

        if conversation:
            return conversation

        return self.create_conversation(
            session_id
        )

    def save_message(
        self,
        session_id: str,
        role: str,
        content: str,
    ):
        """
        Save a conversation message.
        """

        conversation = self.get_or_create_conversation(
            session_id
        )

        message = ConversationMessage(
            conversation_id=conversation.id,
            role=role,
            content=content,
        )

        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)

        return message

    def load_messages(
        self,
        session_id: str,
    ):
        """
        Load all messages for a conversation.
        """

        conversation = self.get_conversation(
            session_id
        )

        if conversation is None:
            return []

        messages = (
            self.db.query(ConversationMessage)
            .filter(
                ConversationMessage.conversation_id == conversation.id
            )
            .order_by(
                ConversationMessage.created_at
            )
            .all()
        )

        return messages
    
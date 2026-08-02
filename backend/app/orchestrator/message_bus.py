from collections import defaultdict

from app.orchestrator.message import Message


class MessageBus:
    """
    Handles communication between agents.
    """

    def __init__(self):
        self.messages = defaultdict(list)

    def send_message(
        self,
        sender: str,
        receiver: str,
        content: str,
    ):
        """
        Send a message to another agent.
        """

        message = Message.create(
            sender=sender,
            receiver=receiver,
            content=content,
        )

        self.messages[receiver].append(message)

    def receive_messages(
        self,
        receiver: str,
    ):
        """
        Receive all messages for an agent.
        """

        msgs = self.messages[receiver]

        self.messages[receiver] = []

        return msgs

    def peek_messages(
        self,
        receiver: str,
    ):
        """
        View messages without removing them.
        """

        return self.messages[receiver]

    def clear(self):
        """
        Remove every message.
        """

        self.messages.clear()

    def get_all_messages(self):
        """
        Return every stored message.
        """

        return dict(self.messages)
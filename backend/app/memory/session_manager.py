from app.memory.conversation import ConversationMemory


class SessionManager:
    """
    Stores one ConversationMemory per session.
    """

    def __init__(self):
        self.sessions = {}

    def get_conversation(self, session_id: str):
        """
        Return the ConversationMemory for a session.
        Create one if it doesn't exist.
        """

        if session_id not in self.sessions:
            self.sessions[session_id] = ConversationMemory()

        return self.sessions[session_id]

    def delete_session(self, session_id: str):
        """
        Delete a session.
        """

        self.sessions.pop(session_id, None)

    def clear(self):
        """
        Remove all sessions.
        """

        self.sessions.clear()

    def get_all_sessions(self):
        """
        Return all active sessions.
        """

        return self.sessions
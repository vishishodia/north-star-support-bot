import uuid
from app.models import ConversationState


class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self):
        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {
            "state": ConversationState.MAIN_MENU,
            "history": [],
            "activity": None,
            "weather": None,
            "budget": None,
        }

        return session_id

    def get_session(self, session_id):
        return self.sessions.get(session_id)


session_manager = SessionManager()
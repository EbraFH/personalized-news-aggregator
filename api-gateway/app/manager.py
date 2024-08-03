from app.engine import GatewayEngine

class GatewayManager:
    """Manager class for handling API gateway operations."""

    def __init__(self):
        self.engine = GatewayEngine()

    def register_user(self, email, preferences):
        """Register a new user."""
        return self.engine.register_user(email, preferences)

    def fetch_and_summarize_news(self, email):
        """Fetch and summarize news based on user preferences."""
        return self.engine.fetch_and_summarize_news(email)
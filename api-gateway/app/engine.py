from app.accessor import GatewayAccessor

class GatewayEngine:
    """Engine class for handling the core logic of API gateway operations."""

    def __init__(self):
        self.accessor = GatewayAccessor()

    def register_user(self, email, preferences):
        """Register a new user using the accessor."""
        return self.accessor.register_user(email, preferences)

    def fetch_and_summarize_news(self, email):
        """Fetch and summarize news based on user preferences using the accessor."""
        return self.accessor.fetch_and_summarize_news(email)
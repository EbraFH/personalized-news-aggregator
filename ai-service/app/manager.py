from app.engine import AIEngine

class AIManager:
    """
    Manager class for handling AI-related operations.
    """

    def __init__(self):
        self.ai_engine = AIEngine()

    def generate_summary(self, articles):
        """
        Generate a summary for the given news articles.
        """
        return self.ai_engine.generate_summary(articles)

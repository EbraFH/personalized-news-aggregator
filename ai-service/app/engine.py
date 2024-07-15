from app.accessor import AIAccessor

class AIEngine:
    """
    Engine class for handling the core logic of AI processing.
    """

    def __init__(self):
        self.ai_accessor = AIAccessor()

    def generate_summary(self, articles):
        """
        Generate a summary for the given news articles using the accessor.
        """
        return self.ai_accessor.generate_summary(articles)

from app.accessor import AIAccessor

class AIEngine:
    """Engine class for handling the core logic of AI processing."""

    def __init__(self):
        self.ai_accessor = AIAccessor()

    def generate_summary(self, articles):
        """Generate summaries for the given news articles using the accessor."""
        return self.ai_accessor.generate_summary(articles)

    def generate_summary_with_kernel(self, articles):
        """Generate summaries for the given news articles using Semantic Kernel."""
        return self.ai_accessor.generate_summary_with_kernel(articles)
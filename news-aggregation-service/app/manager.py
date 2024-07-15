from app.engine import NewsEngine

class NewsManager:
    """
    Manager class for news operations.
    """

    def __init__(self):
        self.news_engine = NewsEngine()

    def aggregate_news(self, preferences):
        """
        Aggregate news based on user preferences.
        """
        return self.news_engine.aggregate_news(preferences)

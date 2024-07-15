from app.accessor import NewsAccessor

class NewsEngine:
    """
    Engine class for news business logic.
    """

    def __init__(self):
        self.news_accessor = NewsAccessor()

    def aggregate_news(self, preferences):
        """
        Aggregate news based on user preferences.
        """
        return self.news_accessor.fetch_news(preferences)

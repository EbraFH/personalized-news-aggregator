from app.accessor import NewsAccessor, TextSummarizer

class NewsEngine:
    """Engine class to encapsulate business logic for news aggregation and summarization."""

    def __init__(self):
        self.news_accessor = NewsAccessor()
        self.text_summarizer = TextSummarizer()

    def get_summarized_news(self, preferences):
        """Fetch and summarize news based on preferences."""
        news = self.news_accessor.fetch_news(preferences)
        summaries = [self.text_summarizer.summarize_text(article['description']) 
                     for article in news['results']]
        return summaries
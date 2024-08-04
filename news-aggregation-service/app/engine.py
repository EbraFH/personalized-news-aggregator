from app.accessor import NewsAccessor, TextSummarizer
import logging

class NewsEngine:
    """Engine class to encapsulate business logic for news aggregation and summarization."""

    def __init__(self):
        self.news_accessor = NewsAccessor()
        self.text_summarizer = TextSummarizer()

    def get_summarized_news(self, preferences):
        """Fetch and summarize news based on preferences."""
        try:
            news = self.news_accessor.fetch_news(preferences)
            summaries = [self.text_summarizer.summarize_text(article['description']) 
                         for article in news['results']]
            return summaries
        except Exception as e:
            logging.error(f"Error in get_summarized_news: {str(e)}")
            raise
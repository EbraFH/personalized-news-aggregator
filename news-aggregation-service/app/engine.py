from app.accessor import NewsAccessor, TextSummarizer

class NewsEngine:
    """
    Engine class to encapsulate business logic for news aggregation and summarization.
    """
    @staticmethod
    def get_summarized_news(preferences):
        """
        Fetch and summarize news based on preferences.
        """
        news = NewsAccessor().fetch_news(preferences)
        summaries = [TextSummarizer.summarize_text(article['description']) for article in news['results']]
        return summaries

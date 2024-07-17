import os
import requests
import redis

class NewsAccessor:
    """
    Accessor class to interact with the NewsData.io API for fetching news.
    """

    def __init__(self):
        self.redis_host = os.getenv('REDIS_HOST')
        self.redis_port = os.getenv('REDIS_PORT')
        self.redis_client = redis.StrictRedis(host=self.redis_host, port=self.redis_port, db=0)

    def fetch_news(self, preferences):
        """
        Fetch news based on user preferences using NewsData.io API.
        """
        cached_news = self.redis_client.get(preferences)
        if cached_news:
            return cached_news

        api_key = os.getenv('NEWS_API_KEY')
        url = 'https://newsdata.io/api/1/news'
        params = {
            'apikey': api_key,
            'category': preferences
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            news = response.json()
            self.redis_client.set(preferences, news, ex=3600)  # Cache for 1 hour
            return news
        else:
            response.raise_for_status()

class TextSummarizer:
    """
    Summarizer class to generate concise summaries using Gemini Free Tier API.
    """
    @staticmethod
    def summarize_text(text):
        """
        Generate a concise summary using Gemini Free Tier API.
        """
        api_key = os.getenv('GEMINI_API_KEY')
        url = 'https://api.gemini.com/v1/ai/summarize'
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {'text': text}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()['summary']
        else:
            response.raise_for_status()
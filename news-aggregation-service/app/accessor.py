import os
import requests
import redis
import json
import logging

class NewsAccessor:
    """Accessor class to interact with the NewsData.io API for fetching news."""

    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host=os.getenv('REDIS_HOST'),
            port=os.getenv('REDIS_PORT'),
            db=0
        )
        self.api_key = os.getenv('NEWS_API_KEY')
        self.base_url = 'https://newsdata.io/api/1/news'

    def fetch_news(self, preferences):
        """Fetch news based on user preferences using NewsData.io API."""
        cached_news = self.redis_client.get(preferences)
        if cached_news:
            return json.loads(cached_news)

        params = {
            'apikey': self.api_key,
            'category': preferences
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            news = response.json()
            self.redis_client.set(preferences, json.dumps(news), ex=3600)  # Cache for 1 hour
            return news
        except requests.RequestException as e:
            logging.error(f"Error fetching news: {str(e)}")
            raise

class TextSummarizer:
    """Summarizer class to generate concise summaries using Gemini Free Tier API."""

    @staticmethod
    def summarize_text(text):
        """Generate a concise summary using Gemini Free Tier API."""
        api_key = os.getenv('GEMINI_API_KEY')
        url = 'https://api.gemini.com/v1/ai/summarize'
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {'text': text}
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()['summary']
        except requests.RequestException as e:
            logging.error(f"Error summarizing text: {str(e)}")
            raise
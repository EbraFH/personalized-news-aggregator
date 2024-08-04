import os
import requests
import redis
import json
import logging
from requests.exceptions import RequestException

class NewsAccessor:
    """Accessor class to interact with the NewsData.io API for fetching news."""

    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host=os.getenv('REDIS_HOST'),
            port=os.getenv('REDIS_PORT'),
            db=0,
            decode_responses=True
        )
        self.api_key = os.getenv('NEWS_API_KEY')
        self.base_url = 'https://newsdata.io/api/1/news'

    def fetch_news(self, preferences):
        """Fetch news based on user preferences using NewsData.io API."""
        cache_key = f"news:{preferences}"
        cached_news = self.redis_client.get(cache_key)
        if cached_news:
            return json.loads(cached_news)

        params = {
            'apikey': self.api_key,
            'category': preferences,
            'language': 'en'  # Add language parameter for English news
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            news = response.json()
            self.redis_client.setex(cache_key, 3600, json.dumps(news))  # Cache for 1 hour
            return news
        except RequestException as e:
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
            response = requests.post(url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()['summary']
        except RequestException as e:
            logging.error(f"Error summarizing text: {str(e)}")
            raise
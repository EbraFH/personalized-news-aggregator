import requests

class NewsAccessor:
    """
    Accessor class for fetching news.
    """

    NEWS_API_URL = 'https://newsdata.io/api/1/news?apikey=YOUR_API_KEY&q='

    def fetch_news(self, preferences):
        """
        Fetch news based on user preferences.
        """
        response = requests.get(f"{self.NEWS_API_URL}{preferences}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

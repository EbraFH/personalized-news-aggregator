from flask import request, jsonify
from app import app
from app.manager import NewsManager
import requests

@app.route('/api/news', methods=['POST'])
def get_news():
    """
    Fetch and aggregate news based on user preferences.
    """
    try:
        data = request.get_json()
        preferences = data.get('preferences', '')
        news_manager = NewsManager()
        news_summary = news_manager.aggregate_news(preferences)

        # Publish an event to the pub/sub component
        pubsub_url = "http://localhost:3500/v1.0/publish/pubsub/news-aggregated"
        event_data = {"preferences": preferences, "news_summary": news_summary}
        requests.post(pubsub_url, json=event_data)
        
        return jsonify({"news_summary": news_summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

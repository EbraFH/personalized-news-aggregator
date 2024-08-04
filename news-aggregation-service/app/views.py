from flask import Blueprint, request, jsonify
import requests
from app.manager import NewsManager

bp = Blueprint('views', __name__)

@bp.route('/api/news', methods=['POST'])
def get_news():
    """Fetch and aggregate news based on user preferences."""
    try:
        data = request.get_json()
        preferences = data.get('preferences')
        
        if not preferences:
            return jsonify({"error": "Preferences are required"}), 400
        
        news_manager = NewsManager()
        news_summary = news_manager.aggregate_news(preferences)

        # Publish an event to the pub/sub component
        pubsub_url = "http://localhost:3500/v1.0/publish/pubsub/news-aggregated"
        event_data = {"preferences": preferences, "news_summary": news_summary}
        pubsub_response = requests.post(pubsub_url, json=event_data)
        pubsub_response.raise_for_status()
        
        return jsonify({"news_summary": news_summary}), 200
    except requests.RequestException as e:
        return jsonify({"error": f"Error publishing event: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error aggregating news: {str(e)}"}), 500
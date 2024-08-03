from flask import Blueprint, request, jsonify
import requests
from app.manager import AIManager

bp = Blueprint('views', __name__)

@bp.route('/api/generate_summary', methods=['POST'])
def generate_summary():
    """Generate a summary for the given news articles."""
    try:
        data = request.get_json()
        articles = data.get('articles')
        if not articles:
            return jsonify({"error": "Articles are required"}), 400
        
        ai_manager = AIManager()
        summary = ai_manager.generate_summary_with_kernel(articles)
        
        # Publish an event to the pub/sub component
        pubsub_url = "http://localhost:3500/v1.0/publish/pubsub/summary-generated"
        event_data = {"articles": articles, "summary": summary}
        requests.post(pubsub_url, json=event_data)
        
        return jsonify({"summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
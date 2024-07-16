from flask import request, jsonify
from app import app
from app.manager import AIManager
import requests

@app.route('/api/generate_summary', methods=['POST'])
def generate_summary():
    """
    Generate a summary for the given news articles.
    """
    try:
        data = request.get_json()
        articles = data.get('articles')
        if not articles:
            raise ValueError("Articles are required")
        
        ai_manager = AIManager()
        summary = ai_manager.generate_summary(articles)
        
        # Publish an event to the pub/sub component
        pubsub_url = "http://localhost:3500/v1.0/publish/pubsub/summary-generated"
        event_data = {"articles": articles, "summary": summary}
        requests.post(pubsub_url, json=event_data)
        
        return jsonify({"summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

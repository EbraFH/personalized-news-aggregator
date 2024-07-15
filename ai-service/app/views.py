from flask import request, jsonify
from app import app
from app.manager import AIManager

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
        
        return jsonify({"summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

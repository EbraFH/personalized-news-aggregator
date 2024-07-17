from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app import app
from app.manager import GatewayManager

@app.route('/api/register', methods=['POST'])
def register():
    """
    Register a new user.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        preferences = data.get('preferences')
        
        if not email or not preferences:
            raise ValueError("Email and preferences are required")
        
        gateway_manager = GatewayManager()
        response = gateway_manager.register_user(email, preferences)
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/news', methods=['POST'])
@jwt_required()
def fetch_news():
    """
    Fetch and summarize news based on user preferences.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        
        if not email:
            raise ValueError("Email is required")
        
        gateway_manager = GatewayManager()
        response = gateway_manager.fetch_and_summarize_news(email)
        
        return jsonify(response), 202
    except Exception as e:
        return jsonify({"error": str(e)}), 400

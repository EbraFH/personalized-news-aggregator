from flask import request, jsonify
from app import app
from app.manager import UserManager
import requests

@app.route('/api/register', methods=['POST'])
def register_user():
    """
    Register a new user.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        preferences = data.get('preferences', '')
        if not email:
            raise ValueError("Email is required")
        
        user_manager = UserManager()
        user = user_manager.create_user(email, preferences)
        
        # Publish an event to the pub/sub component
        pubsub_url = "http://localhost:3500/v1.0/publish/pubsub/user-registered"
        event_data = {"email": email, "preferences": preferences}
        requests.post(pubsub_url, json=event_data)
        
        return jsonify({"message": "User registered successfully", "user_id": user.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/login', methods=['POST'])
def login_user():
    """
    Login a user.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        if not email:
            raise ValueError("Email is required")
        
        user_manager = UserManager()
        user = user_manager.get_user_by_email(email)
        if user:
            return jsonify({"message": "Login successful", "user_id": user.id}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/preferences', methods=['POST'])
def save_preferences():
    """
    Save user preferences.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        preferences = data.get('preferences')
        if not email or not preferences:
            raise ValueError("Email and preferences are required")
        
        user_manager = UserManager()
        user = user_manager.update_preferences(email, preferences)
        
        return jsonify({"message": "Preferences updated successfully", "user_id": user.id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

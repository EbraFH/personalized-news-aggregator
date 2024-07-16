from flask import request, jsonify
from app import app
from app.manager import UserManager
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
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
            access_token = create_access_token(identity=email)
            return jsonify({"message": "Login successful", "access_token": access_token}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/preferences', methods=['POST'])
@jwt_required()
def save_preferences():
    """
    Save user preferences.
    """
    data = request.get_json()
    try:
        current_user = get_jwt_identity()
        preferences = data.get('preferences', '')
        user_manager = UserManager()
        user = user_manager.get_user_by_email(current_user)
        user.preferences = preferences
        user_manager.update_user(user)
        
        return jsonify({"message": "Preferences updated successfully", "preferences": preferences}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

from flask import request, jsonify
from app import app
from app.manager import UserManager
import requests
import os

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
    data = request.get_json()
    try:
        preferences = UserManager.save_preferences(data)
        return jsonify(preferences), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/news-summaries', methods=['GET'])
def get_news_summaries():
    """
    Fetch news summaries based on user preferences.
    """
    try:
        summaries = UserManager.get_news_summaries()
        return jsonify(summaries), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/preferences', methods=['PUT'])
def update_preferences():
    """
    Update user preferences.
    """
    data = request.get_json()
    email = data.get('email')
    preferences = data.get('preferences')
    try:
        user = UserManager.update_preferences(email, preferences)
        return jsonify({'message': 'Preferences updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400 

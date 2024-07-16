from flask import request, jsonify
from app import app, db
from app.manager import UserManager

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

@app.route('/api/preferences', methods=['PUT'])
def update_preferences():
    """
    Update user preferences.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        preferences = data.get('preferences')
        if not email:
            raise ValueError("Email is required")

        user_manager = UserManager()
        user = user_manager.get_user_by_email(email)
        if not user:
            return jsonify({"error": "User not found"}), 404

        user.preferences = preferences
        db.session.commit()
        
        return jsonify({'message': 'Preferences updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

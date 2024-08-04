from flask import Blueprint, request, jsonify
from app.manager import EmailManager

bp = Blueprint('views', __name__)

@bp.route('/api/send_email', methods=['POST'])
def send_email():
    """Send an email with the news summary."""
    try:
        data = request.get_json()
        email = data.get('email')
        summary = data.get('summary', '')
        
        if not email:
            return jsonify({"error": "Email is required"}), 400
        
        if not summary:
            return jsonify({"error": "Summary is required"}), 400
        
        EmailManager.send_email(email, summary)
        
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send email: {str(e)}"}), 500
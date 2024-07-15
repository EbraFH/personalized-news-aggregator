from flask import request, jsonify
from app import app
from app.manager import EmailManager

@app.route('/api/send_email', methods=['POST'])
def send_email():
    """
    Send an email with the news summary.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        summary = data.get('summary', '')
        if not email:
            raise ValueError("Email is required")
        
        email_manager = EmailManager()
        email_manager.send_email(email, summary)
        
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Import views to register routes
    from app import views
    app.register_blueprint(views.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5003)
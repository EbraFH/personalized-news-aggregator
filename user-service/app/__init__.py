import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Enable CORS for all routes
    CORS(app)

    # Configure JWT
    JWTManager(app)

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Initialize database
    db = SQLAlchemy(app)

    # Import views to register routes
    from app import views
    app.register_blueprint(views.bp)

    return app, db

if __name__ == '__main__':
    app, _ = create_app()
    app.run(host='0.0.0.0', port=5000)
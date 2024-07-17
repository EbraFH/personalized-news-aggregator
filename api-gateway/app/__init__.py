from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import logging, os

# Enhance the API Gateway with authorization and define its role more clearly
from flask_jwt_extended import JWTManager

# Load environment variables from .env file
load_dotenv()

# Initialize the app
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Import views to register routes
import app.views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

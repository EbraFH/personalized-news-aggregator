from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Initialize the app
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.INFO)

# Import views to register routes
import app.views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

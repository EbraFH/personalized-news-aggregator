from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Import views to register routes
import app.views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
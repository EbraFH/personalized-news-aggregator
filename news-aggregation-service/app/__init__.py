from flask import Flask

app = Flask(__name__)

# Import views to register routes
import app.views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

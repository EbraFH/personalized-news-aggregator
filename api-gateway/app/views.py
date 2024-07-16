from fastapi import FastAPI, Request
import requests
from flask_jwt_extended import jwt_required

@app.route('/api/register', methods=['POST'])
def register():
    """
    Register a new user.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        preferences = data.get('preferences')
        
        if not email or not preferences:
            raise ValueError("Email and preferences are required")
        
        gateway_manager = GatewayManager()
        response = gateway_manager.register_user(email, preferences)
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/news', methods=['POST'])
@jwt_required()
def fetch_news():
    """
    Fetch and summarize news based on user preferences.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        
        if not email:
            raise ValueError("Email is required")
        
        gateway_manager = GatewayManager()
        response = gateway_manager.fetch_and_summarize_news(email)
        
        return jsonify(response), 202
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    
app = FastAPI()

@app.post("/api/register")
async def register_user(request: Request):
    data = await request.json()
    email = data.get('email')
    preferences = data.get('preferences')

    if not email or not preferences:
        return {"error": "Email and preferences are required"}

    response = requests.post("http://user-service:5001/api/register", json={"email": email, "preferences": preferences})
    return response.json()

@app.post("/api/login")
async def login_user(request: Request):
    data = await request.json()
    email = data.get('email')

    if not email:
        return {"error": "Email is required"}

    response = requests.post("http://user-service:5001/api/login", json={"email": email})
    return response.json()

@app.post("/api/news")
async def fetch_news(request: Request):
    data = await request.json()
    email = data.get('email')

    if not email:
        return {"error": "Email is required"}

    response = requests.post("http://news-aggregation-service:5002/api/news", json={"email": email})
    return response.json()

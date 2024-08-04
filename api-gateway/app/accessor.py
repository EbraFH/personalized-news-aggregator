import requests
import logging

class GatewayAccessor:
    """Accessor class for interacting with other services."""

    def register_user(self, email, preferences):
        """Register a new user by calling the user service."""
        url = "http://localhost:3500/v1.0/invoke/user-service/method/api/register"
        data = {"email": email, "preferences": preferences}
        
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error registering user: {str(e)}")
            raise

    def fetch_and_summarize_news(self, email):
        """Fetch and summarize news based on user preferences."""
        news_url = "http://localhost:3500/v1.0/invoke/news-aggregation-service/method/api/news"
        ai_url = "http://localhost:3500/v1.0/invoke/ai-service/method/api/generate_summary"
        email_url = "http://localhost:3500/v1.0/invoke/email-service/method/api/send_email"

        try:
            news_response = requests.post(news_url, json={"email": email})
            news_response.raise_for_status()
            articles = news_response.json().get("news_summary")
            
            ai_response = requests.post(ai_url, json={"articles": articles})
            ai_response.raise_for_status()
            summary = ai_response.json().get("summary")
            
            email_response = requests.post(email_url, json={"email": email, "summary": summary})
            email_response.raise_for_status()
            
            return {"status": "News summary sent"}
        except requests.RequestException as e:
            logging.error(f"Error in fetch_and_summarize_news: {str(e)}")
            raise
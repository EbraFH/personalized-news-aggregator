import requests

class GatewayAccessor:
    """
    Accessor class for interacting with other services.
    """

    def register_user(self, email, preferences):
        """
        Register a new user by calling the user service.
        """
        url = "http://user-service:5001/api/register"
        data = {"email": email, "preferences": preferences}
        
        response = requests.post(url, json=data)
        response.raise_for_status()
        
        return response.json()

    def fetch_and_summarize_news(self, email):
        """
        Fetch and summarize news based on user preferences by calling the news aggregation service and AI service.
        """
        news_url = "http://news-aggregation-service:5002/api/fetch_news"
        ai_url = "http://ai-service:5003/api/generate_summary"
        email_url = "http://email-service:5004/api/send_email"

        news_response = requests.post(news_url, json={"email": email})
        news_response.raise_for_status()
        articles = news_response.json().get("articles")
        
        ai_response = requests.post(ai_url, json={"articles": articles})
        ai_response.raise_for_status()
        summary = ai_response.json().get("summary")
        
        email_response = requests.post(email_url, json={"email": email, "summary": summary})
        email_response.raise_for_status()
        
        return {"status": "News summary sent"}

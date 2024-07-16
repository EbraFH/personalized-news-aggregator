import requests
import os

class AIAccessor:
    """
    Accessor class for interacting with the external AI API to generate summaries.
    """

    @staticmethod
    def generate_summary(articles):
        """
        Generate a summary for the given news articles using the Gemini Free Tier API.
        """
        try:
            api_key = os.getenv('GEMINI_API_KEY')
            url = 'https://api.gemini.com/v1/ai/summarize'
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }
            data = {'articles': articles}
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json().get("summary")
        except Exception as e:
            raise Exception(f"Failed to generate summary: {str(e)}")

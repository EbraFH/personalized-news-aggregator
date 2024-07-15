import requests

class AIAccessor:
    """
    Accessor class for interacting with the external AI API to generate summaries.
    """

    def generate_summary(self, articles):
        """
        Generate a summary for the given news articles using the Gemini Free Tier API.
        """
        try:
            url = "https://api.gemini.com/summarize"
            headers = {"Content-Type": "application/json"}
            data = {"articles": articles}
            
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            
            return response.json().get("summary")
        except Exception as e:
            raise Exception(f"Failed to generate summary: {str(e)}")

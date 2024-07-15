import unittest
from app.manager import GatewayManager

class APIGatewayTest(unittest.TestCase):
    """
    Unit tests for the API gateway.
    """

    def setUp(self):
        self.gateway_manager = GatewayManager()

    def test_register_user(self):
        """
        Test user registration.
        """
        email = "test@example.com"
        preferences = {"categories": ["technology", "science"]}
        try:
            response = self.gateway_manager.register_user(email, preferences)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

    def test_fetch_and_summarize_news(self):
        """
        Test fetching and summarizing news.
        """
        email = "test@example.com"
        try:
            response = self.gateway_manager.fetch_and_summarize_news(email)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()

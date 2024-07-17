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
            response = None
        
        self.assertTrue(success)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        self.assertIn("message", response)
        self.assertEqual(response["message"], "User registered successfully")

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
            response = None
        
        self.assertTrue(success)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        self.assertIn("status", response)
        self.assertEqual(response["status"], "News summary sent")

if __name__ == '__main__':
    unittest.main()

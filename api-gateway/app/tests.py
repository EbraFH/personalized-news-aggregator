import unittest
from unittest.mock import patch
from app.manager import GatewayManager

class APIGatewayTest(unittest.TestCase):
    """Unit tests for the API gateway."""

    def setUp(self):
        self.gateway_manager = GatewayManager()

    @patch('app.accessor.GatewayAccessor.register_user')
    def test_register_user(self, mock_register):
        """Test user registration."""
        mock_register.return_value = {"message": "User registered successfully"}
        
        email = "test@example.com"
        preferences = {"categories": ["technology", "science"]}
        response = self.gateway_manager.register_user(email, preferences)
        
        self.assertIsInstance(response, dict)
        self.assertIn("message", response)
        self.assertEqual(response["message"], "User registered successfully")

    @patch('app.accessor.GatewayAccessor.fetch_and_summarize_news')
    def test_fetch_and_summarize_news(self, mock_fetch):
        """Test fetching and summarizing news."""
        mock_fetch.return_value = {"status": "News summary sent"}
        
        email = "test@example.com"
        response = self.gateway_manager.fetch_and_summarize_news(email)
        
        self.assertIsInstance(response, dict)
        self.assertIn("status", response)
        self.assertEqual(response["status"], "News summary sent")

if __name__ == '__main__':
    unittest.main()
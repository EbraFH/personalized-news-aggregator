import unittest
from unittest.mock import patch
from app.manager import EmailManager

class EmailServiceTest(unittest.TestCase):
    """Unit tests for the email service."""

    @patch('app.accessor.EmailAccessor.send_email')
    def test_send_email(self, mock_send_email):
        """Test sending an email."""
        email = "test@example.com"
        summary = "This is a test summary."
        
        EmailManager.send_email(email, summary)
        
        mock_send_email.assert_called_once_with(email, summary)

if __name__ == '__main__':
    unittest.main()
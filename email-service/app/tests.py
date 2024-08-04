import unittest
from unittest.mock import patch
from app.manager import EmailManager

class EmailServiceTest(unittest.TestCase):
    """Unit tests for the email service."""

    @patch('app.accessor.EmailAccessor.send_email')
    def test_send_email_success(self, mock_send_email):
        """Test successful email sending."""
        email = "test@example.com"
        summary = "This is a test summary."
        
        EmailManager.send_email(email, summary)
        
        mock_send_email.assert_called_once_with(email, summary)

    @patch('app.accessor.EmailAccessor.send_email')
    def test_send_email_failure(self, mock_send_email):
        """Test email sending failure."""
        email = "test@example.com"
        summary = "This is a test summary."
        mock_send_email.side_effect = Exception("Failed to send email")
        
        with self.assertRaises(Exception):
            EmailManager.send_email(email, summary)

if __name__ == '__main__':
    unittest.main()
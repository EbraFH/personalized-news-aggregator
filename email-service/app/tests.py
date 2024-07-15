import unittest
from app.manager import EmailManager

class EmailServiceTest(unittest.TestCase):
    """
    Unit tests for the email service.
    """

    def setUp(self):
        self.email_manager = EmailManager()

    def test_send_email(self):
        """
        Test sending an email.
        """
        try:
            self.email_manager.send_email("test@example.com", "This is a test summary.")
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()

from app.engine import EmailEngine

class EmailManager:
    """
    Manager class for handling email-related operations.
    """

    def __init__(self):
        self.email_engine = EmailEngine()

    def send_email(self, email, summary):
        """
        Send an email with the given summary.
        """
        self.email_engine.send_email(email, summary)

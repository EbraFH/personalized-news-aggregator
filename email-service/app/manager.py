from app.engine import EmailEngine

class EmailManager:
    """Manager class for handling email-related operations."""

    @staticmethod
    def send_email(email, summary):
        """Send an email with the given summary."""
        EmailEngine.send_email(email, summary)
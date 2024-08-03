from app.accessor import EmailAccessor

class EmailEngine:
    """Engine class to encapsulate business logic for email sending operations."""

    @staticmethod
    def send_email(email, summary):
        """Send an email using the accessor class."""
        EmailAccessor.send_email(email, summary)
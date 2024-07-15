from app.accessor import EmailAccessor

class EmailEngine:
    """
    Engine class for handling the core logic of sending emails.
    """

    def __init__(self):
        self.email_accessor = EmailAccessor()

    def send_email(self, email, summary):
        """
        Send an email with the given summary using the accessor.
        """
        self.email_accessor.send_email(email, summary)

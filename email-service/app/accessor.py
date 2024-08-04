import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import logging

class EmailAccessor:
    """Accessor class for sending emails using an SMTP server."""

    @staticmethod
    def send_email(email, summary):
        """Send an email with the given summary."""
        sender_email = os.getenv('EMAIL_USERNAME')
        sender_password = os.getenv('EMAIL_PASSWORD')
        email_host = os.getenv('EMAIL_HOST')
        email_port = os.getenv('EMAIL_PORT')
        subject = "Your News Summary"
        body = f"Here is your news summary:\n\n{summary}"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(email_host, int(email_port)) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())
            logging.info(f"Email sent successfully to {email}")
        except smtplib.SMTPException as e:
            logging.error(f"SMTP error occurred: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error occurred while sending email: {str(e)}")
            raise
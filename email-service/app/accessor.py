import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailAccessor:
    """
    Accessor class for sending emails using an SMTP server.
    """

    def send_email(self, email, summary):
        """
        Send an email with the given summary.
        """
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        subject = "Your News Summary"
        body = f"Here is your news summary:\n\n{summary}"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")

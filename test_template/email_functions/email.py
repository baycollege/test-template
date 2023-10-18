import smtplib
from email.message import EmailMessage


class EmailUsers:

    def __init__(self, to: str, sender: str) -> None:
        self.to = to
        self.sender = sender
        self.msg = ''
        self.subject = ''

    def create_message(self, msg: str) -> None:

        self.msg = msg

    def create_subject(self, subject: str) -> None:

        self.subject = subject

    def _create_email(self) -> EmailMessage:

        email = EmailMessage()

        email['Subject'] = self.subject
        email['From'] = self.sender
        email['To'] = self.to
        email.set_content(self.msg)

        return email

    def send_email(self):

        email = self._create_email()
        conn = smtplib.SMTP('mail.baycollege.edu')
        conn.send_message(email)
        conn.close()

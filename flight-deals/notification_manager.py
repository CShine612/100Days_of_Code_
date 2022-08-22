import smtplib
from twilio.rest import Client
import config


# twillo text variant
class NotificationManager:
    def __init__(self):
        self.connection = None
        self.client = Client(config.account_sid, config.auth_token)

    def send_text(self, text):
        message = self.client.messages \
            .create(body=text,
                    from_="+16065175616",
                    to=config.PHONE_NUMBER)
        print(message.sid)

    def send_email(self, text, recipient_email, recipient_name):
        self.connection = smtplib.SMTP("smtp.gmail.com")
        text = text.replace("€", "E")
        self.connection.starttls()
        self.connection.login(config.my_email, config.my_email_pass)
        self.connection.sendmail(config.my_email,
                                 recipient_email,
                                 msg=f"Cheap Flights Found!\n\n{recipient_name},\n{text}\n")
        self.connection.quit()

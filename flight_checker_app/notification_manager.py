from twilio.rest import Client
account_sid = "Your twilio account sid"
auth_token = 'Your twilio auth token'

class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)


    def send_message(self, text):
        self.message = self.client.messages \
            .create(
            to='Recipient number',
            body=text,
            from_='Your phone number')
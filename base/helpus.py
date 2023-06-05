from twilio.rest import Client


class Feedbackhandler:
    phone_number = None
    message = None

    def __init__(self,phone_number, message):
        self.phone_number = phone_number
        self.message = message
    
    

    def send_feedback(self):
        account_sid = "AC53487abebac2e0f385e39fb19715ee42"
        auth_token = "40268a768d854bbde75860da4dff8138"
        client = Client(account_sid, auth_token)
        print('------------3333333333333')
        message = client.messages.create(
            body= f'Your Query has been reqistered successfully.',
            from_="+12545664631",
            to=self.phone_number
        )
        print(message.sid)
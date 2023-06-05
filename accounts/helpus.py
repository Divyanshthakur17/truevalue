from twilio.rest import Client


class Msghandler:
    phone_number = None
    otp = None

    def __init__(self,phone_number, otp):
        self.phone_number = phone_number
        self.otp = otp

    def send_otp(self):
        account_sid = "AC53487abebac2e0f385e39fb19715ee42"
        auth_token = "40268a768d854bbde75860da4dff8138"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Your OTP is : {self.otp}",
            from_="+12545664631",
            to=self.phone_number
        )
        print(message.sid)
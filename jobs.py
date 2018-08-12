import urllib.parse
from flask import current_app
from twilio.rest import Client

from application import application


def call_phone(number, message):
    with application.app_context():
        account_sid = current_app.config['TWILIO_ACCOUNT_SID']
        auth_token = current_app.config['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        cleaned_message = urllib.parse.quote(message)
        url = "http://twimlets.com/message?Message%5B0%5D={}".format(
                cleaned_message)
        client.calls.create(
            to=number,
            from_="+12027602953",
            url=url)


def concat_two(a, b):
    print(str(a) + ' ' + str(b))

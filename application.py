import os
from flask import Flask
from flask_apscheduler import APScheduler


class Config(object):
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = 'UTC'
    TWILIO_ACCOUNT_SID =  os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN =  os.environ.get('TWILIO_AUTH_TOKEN')


application = Flask(__name__)
application.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(application)
scheduler.start()


@application.route('/', methods=['GET'])
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    application.run()

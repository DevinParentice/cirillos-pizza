from cirillos import mail
from flask_mail import Message
from dotenv import load_dotenv
import os

load_dotenv()


def send_email(form):
    msg = Message(form.subject.data, sender=form.email.data,
                  recipients=[os.getenv('MAIL_USERNAME')])
    msg.body = """
			From: %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
    mail.send(msg)

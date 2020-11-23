from flask.templating import render_template
from cirillos import mail
from flask_mail import Message
from dotenv import load_dotenv
import os

load_dotenv()


def send_email(form):
    msg = Message(form.subject.data, sender=form.email.data,
                  recipients=[os.getenv('MAIL_USERNAME')])
    msg.html = render_template('email.html', form=form)
    mail.send(msg)

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange
import random


class ContactForm(FlaskForm):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    total = num_1 + num_2

    name = StringField('Name',
                       validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    subject = StringField('Subject',
                          validators=[DataRequired()])
    message = TextAreaField('Message',
                            validators=[DataRequired(), Length(min=5, max=1200, message='Your message is too long or too short. Please try again.')])
    spam = DecimalField(f'Spam Protection: What is {num_1} + {num_2}?',
                        validators=[DataRequired(), NumberRange(min=total, max=total, message='Spam validation failed. Please try again.')])
    submit = SubmitField("Send")

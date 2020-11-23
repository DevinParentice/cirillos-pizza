from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class ContactForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    subject = StringField('Subject',
                          validators=[DataRequired()])
    message = TextAreaField('Message',
                            validators=[DataRequired(), Length(min=5, max=1200, message='Your message is too long or too short. Please try again.')])
    spam = DecimalField('Spam Protection: What is 2 + 5?',
                        validators=[DataRequired(), NumberRange(min=7, max=7, message='Spam validation failed. Please try again.')])
    submit = SubmitField("Send")

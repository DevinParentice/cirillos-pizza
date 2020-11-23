from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    subject = StringField('Subject',
                          validators=[DataRequired()])
    message = TextAreaField('Message',
                            validators=[DataRequired(), Length(min=5, max=240)])
    submit = SubmitField("Send")

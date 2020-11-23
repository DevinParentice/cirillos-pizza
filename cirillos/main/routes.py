from flask.helpers import url_for
from cirillos.main.form import ContactForm
from flask import render_template, Blueprint, redirect, flash
from cirillos.main.utils import send_email

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/menu')
def menu():
    return render_template('menu.html')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        send_email(form)
        flash('We have received your email! We will get back to you as soon as possible.', 'success')
        return redirect(url_for('main.home'))
    return render_template('contact.html', form=form)

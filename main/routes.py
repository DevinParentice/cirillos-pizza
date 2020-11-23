from flask import render_template, Blueprint, redirect, url_for

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/menu')
def menu():
    return render_template('menu.html')

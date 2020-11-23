from flask import Flask
from flask_mail import Mail
from cirillos.config import Config

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)

    from cirillos.main.routes import main
    app.register_blueprint(main)

    return app

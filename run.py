from main.routes import main
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)

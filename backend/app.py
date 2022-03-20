from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)

@app.route('/')
def my_app():
    return 'First Flask application!'
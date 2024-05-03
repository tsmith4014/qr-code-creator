#__init__.py file is used to initialize the app and load the routes
# app/__init__.py
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    from .routes import init_app
    init_app(app)

    return app

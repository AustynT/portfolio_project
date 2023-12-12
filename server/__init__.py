from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS  # Import Flask-CORS
from dotenv import load_dotenv

import os

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

load_dotenv()


def create_app():
    """
    Creates a Flask application using the app factory pattern.

    Returns:
        Flask: The Flask application.
    """
    app = Flask(__name__)

    # Load configuration from environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')

    # Initialize extensions with app
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    from .api import register_routes
    register_routes(app)
    # Enable CORS
    CORS(app)  # Add this line to enable Flask-CORS

    # Import and register blueprints

    app.config['DEBUG'] = True

    return app

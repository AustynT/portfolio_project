from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS  # Import Flask-CORS
from dotenv import load_dotenv

import os

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()


def create_app() -> Flask:
    """
    Creates a Flask app using the app factory pattern.
    """
    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')
    app.debug = os.getenv('FLASK_ENV') == 'development'

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    from .api import register_routes
    register_routes(app)

    # Configure CORS
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True,
         allow_headers=["Content-Type", "Access-Control-Allow-Headers", "Authorization", "X-Requested-With"])

    @app.after_request
    def add_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Access-Control-Allow-Headers,Authorization,X-Requested-With'
        return response

    return app

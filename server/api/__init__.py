from flask import Flask
from . import api_classes
from .. import app


def register_api_routes(app):
    # Register API routes here using the app object
    # For example:
    app.add_url_rule(
        '/api/users', view_func=api_classes.UsersAPI.as_view('users_api'))


# Call the function with the app object
register_api_routes(app)

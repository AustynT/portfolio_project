from datetime import timedelta
from typing import Literal
from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError

from server import db

from server.models.user_model import UserModel
from server.schemas.auth_schema import AuthSchema
from server.resources.tokens.jwt_token_resouce import JwtTokenResouce


class AuthApi:
    """
    API class for handling authentication-related endpoints.

    Attributes:
        bp_auth (flask.Blueprint): The Flask blueprint for authentication endpoints.
        request_schema (AuthSchema): The schema for validating and deserializing request data.
        response_schema (AuthSchema): The schema for serializing response data.

    Methods:
        register(): Registers a new user.
        login(): Authenticates a user and returns JWT tokens if the credentials are valid.
        create_tokens(user_id): Creates access and refresh tokens for the given user ID.
    """

    def __init__(self) -> None:
        self.bp_auth = Blueprint('auth', __name__, url_prefix='/auth')
        self.bp_auth.add_url_rule(
            '/register', 'register', self.register, methods=['POST'])
        self.bp_auth.add_url_rule(
            '/login', 'login', self.login, methods=['POST'])
        self.request_schema = AuthSchema().get_request_schemas()
        self.response_schema = AuthSchema().get_response_schemas()

    def register(self) -> tuple[Response, Literal[400]] | tuple[Response, Literal[409]] | Response:
        """
        Registers a new user.

        Returns:
            If the registration is successful, returns a JSON response with a success message.
            If the registration fails due to validation errors or an existing user, returns a JSON response with an error message.
        """
        try:
            # Validate and deserialize input
            data = self.request_schema['register'].load(request.get_json())
        except ValidationError as err:
            return jsonify(err.messages), 400

        # Check if the user already exists
        if UserModel.query.filter_by(username=data['username']).first():
            return jsonify({"message": "User already exists"}), 409

        # Create a new User instance
        user = UserModel(username=data['username'],
                         email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()

        access_token, refresh_token = self.token_resource.create_access_token(
            user.id)
        return jsonify(self.response_schema['register'].dump({
            "id": user.id,
            "email": user.email,
            "jwt_token": access_token,
            "fresh_jwt_token": refresh_token
        }))

    def login(self) -> tuple[Response, Literal[400]] | Response | None:
        """
        Authenticates a user and returns JWT tokens if the credentials are valid.

        Returns:
            If the credentials are valid, returns a JSON response containing the access token and refresh token.
            If the credentials are invalid, returns a JSON response with a message indicating invalid credentials.
        """
        try:
            # Validate and deserialize input
            data = self.request_schema['login'].load(request.get_json())
        except ValidationError as err:
            return jsonify(err.messages), 400

        # Authenticate user
        user = UserModel.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):

            access_token, refresh_token = self.create_tokens(user.id)
            return jsonify(self.response_schema['login'].dump({
                "id": user.id,
                "email": user.email,
                "jwt_token": access_token,
                "fresh_jwt_token": refresh_token
            }), 200)

    def create_access_tokens(self, user_id: int) -> tuple[str, str]:
        """
        Creates access and refresh tokens for the given user ID.

        Args:
            user_id (int): The ID of the user to create tokens for.

        Returns:
            tuple[str, str]: The access token and refresh token.
        """
        token_resource = JwtTokenResouce()
        expire_date: timedelta = token_resource.create_expiration_date(
            amount=1)
        access_token = token_resource.create_access_token(
            user_id, expire_date)

        return access_token

    def create_refresh_tokens(self, user_id: int) -> tuple[str, str]:
        """
        Creates access and refresh tokens for the given user ID.

        Args:
            user_id (int): The ID of the user to create tokens for.

        Returns:
            tuple[str, str]: The access token and refresh token.
        """
        token_resource = JwtTokenResouce()
        expire_date: timedelta = token_resource.create_expiration_date(
            amount=30)
        refresh_token = token_resource.create_refresh_token(
            user_id, expire_date)

        return refresh_token

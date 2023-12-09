from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.user_model import UserModel
from server.schemas.user_schema import UserSchema


class UsersApi:
    """
    API class for managing users.
    """

    def __init__(self):
        self.bp_user = Blueprint('users', __name__, url_prefix='/user')
        self.bp_user.route(
            '/', methods=['GET'])(jwt_required()(self.get_users))
        self.bp_user.route(
            '/<int:user_id>', methods=['GET'])(self.get_user_by_id)
        self.bp_user.route(
            '/', methods=['POST'])(jwt_required()(self.create_user))
        self.bp_user.route(
            '/<int:user_id>', methods=['PUT'])(jwt_required()(self.update_user))
        self.bp_user.route(
            '/<int:user_id>', methods=['DELETE'])(jwt_required()(self.delete_user))

        self.request_schema = UserSchema().get_request_schemas()
        self.response_schema = UserSchema().get_response_schemas()

    def get_users(self):
        """
        Get all users.

        Returns:
            A JSON response containing the serialized users.
        """
        users = UserModel.get_all()
        return jsonify([user.serialize() for user in users])

    def get_user_by_id(self, user_id):
        """
        Get a user by its ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            A JSON response containing the serialized user if found, or a JSON response with an error message and status code 404 if not found.
        """
        user = UserModel.get_by_id(user_id)
        if user:
            return jsonify(user.serialize())
        else:
            return jsonify({"message": "User not found"}), 404

    def create_user(self):
        """
        Creates a new user.

        Returns:
            A JSON response containing the created user's information.
        """
        data = self.request_schema['create']
        user = UserModel.create(**data)

        return jsonify(self.response_schema['create'].dump({
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "password": user.password
        })), 201

    def update_user(self, user_id):
        """
        Update a user by its ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            A JSON response containing the serialized user if found, or a JSON response with an error message and status code 404 if not found.
        """
        user = UserModel.get_by_id(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404

        data = self.request_schema['update'].load(request.get_json())

        user.update(**data)

        return jsonify(self.response_schema['update'].dump({
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "password": user.password
        })), 200

    def delete_user(self, user_id):
        """
        Delete a user by its ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            A JSON response with a message indicating the user was deleted if found, or a JSON response with an error message and status code 404 if not found.
        """
        user = UserModel.get_by_id(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404

        user.delete()

        return jsonify({"message": "User deleted"}), 200

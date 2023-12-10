from typing import Literal
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.user_info_model import UserInfoModel
from server.schemas.user_info_schema import UserInfoSchema


class UserInfoApi:
    """
    API class for managing user info.
    """

    def __init__(self):
        self.bp_user_info = Blueprint(
            'user_info', __name__, url_prefix='/user_info')
        self.bp_user_info.route(
            '/', methods=['GET'])(jwt_required()(self.get_user_info))
        self.bp_user_info.route(
            '/<int:user_id>', methods=['GET'])(self.get_user_info_by_id)
        self.bp_user_info.route(
            '/', methods=['POST'])(jwt_required()(self.create_user_info))
        self.bp_user_info.route(
            '/<int:user_id>', methods=['PUT'])(jwt_required()(self.update_user_info))
        self.bp_user_info.route(
            '/<int:user_id>', methods=['DELETE'])(jwt_required()(self.delete_user_info))

        self.request_schema = UserInfoSchema().get_request_schemas()
        self.response_schema = UserInfoSchema().get_response_schemas()
        self.model = UserInfoModel()

    def get_user_info(self):
        """
        Get all user info.

        Returns:
            A JSON response containing the serialized user info.
        """
        user_info = self.model.get_all_user_info()
        return jsonify([user_info.serialize() for user_info in user_info])

    def get_user_info_by_id(self, user_id) -> Response | tuple[Response, Literal[404]]:
        """
        Get a user info by its ID.

        Args:
            user_id (int): The ID of the user info.

        Returns:
            A JSON response containing the serialized user info if found, or a JSON response with an error message and status code 404 if not found.
        """
        user_info_instance = self.model.get_user_info_by_id(user_id)
        if user_info_instance:
            return jsonify(user_info_instance.serialize())
        else:
            return jsonify({"message": "User Info not found"}), 404

    def create_user_info(self) -> tuple[Response, Literal[201]] | tuple[Response, Literal[400]]:
        """
        Creates a new user info.

        Returns:
            A JSON response containing the created user info's information.
        """
        user_info = request.get_json()
        user_info_instance = self.model.create_user_info(user_info)
        if user_info_instance:
            return jsonify(user_info_instance.serialize()), 201
        else:
            return jsonify({"message": "User Info already exists"}), 400

    def update_user_info(self, user_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[400]]:
        """
        Updates a user info.

        Args:
            user_id (int): The ID of the user info.

        Returns:
            A JSON response containing the updated user info's information if successful, or a JSON response with an error message and status code 400 if unsuccessful.
        """
        user_info = request.get_json()
        user_info_instance = self.model.update_user_info(user_id, user_info)
        if user_info_instance:
            return jsonify(user_info_instance.serialize()), 200
        else:
            return jsonify({"message": "User Info not found"}), 400

    def delete_user_info(self, user_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[404]]:
        """
        Deletes a user info.

        Args:
            user_id (int): The ID of the user info.

        Returns:
            A JSON response containing the deleted user info's information if successful, or a JSON response with an error message and status code 404 if unsuccessful.
        """
        user_info_instance = self.model.delete_user_info(user_id)
        if user_info_instance:
            return jsonify(user_info_instance.serialize()), 200
        else:
            return jsonify({"message": "User Info not found"}), 404

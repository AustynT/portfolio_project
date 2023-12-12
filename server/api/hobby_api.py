from typing import Literal
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.hobby_model import HobbyModel
from server.schemas.hobby_schema import HobbySchema


class HobbyApi:
    """
    API class for managing hobbies.
    """

    def __init__(self) -> None:
        self.bp_hobby = Blueprint('hobbies', __name__, url_prefix='/hobbies')
        self.bp_hobby.route(
            '/', methods=['GET'])(self.get_hobbies)
        self.bp_hobby.route(
            '/', methods=['POST'])(jwt_required())(self.create_hobby)
        self.bp_hobby.route('/<int:hobby_id>',
                            methods=['GET'], endpoint="get_hobby_by_id")(self.get_hobby_by_id)
        self.bp_hobby.route('/<int:hobby_id>',
                            methods=['PUT'], endpoint="update_hobby")(jwt_required())(self.update_hobby)
        self.bp_hobby.route('/<int:hobby_id>',
                            methods=['DELETE'],  endpoint="delete_hobby")(jwt_required()(self.delete_hobby))

        self.request_schema: dict[str, HobbySchema] = HobbySchema
        self.response_schema: dict[str, HobbySchema] = HobbySchema
        self.model = HobbyModel()

    def get_hobbies(self) -> Response:
        """
        Get all hobbies.

        Returns:
            A JSON response containing the serialized hobbies.
        """
        hobbies = self.model.get_all_hobbies()
        return jsonify([hobby.serialize() for hobby in hobbies])

    def get_hobby_by_id(self, hobby_id) -> Response | tuple[Response, Literal[404]]:
        """
        Get a hobby by its ID.

        Args:
            hobby_id (int): The ID of the hobby.

            Returns:
                A JSON response containing the serialized hobby if found, or a JSON response with an error message and status code 404 if not found.
        """
        hobby_instance = self.model.get_hobby_by_id(hobby_id)
        if hobby_instance:
            return jsonify(hobby_instance.serialize())
        else:
            return jsonify({"message": "Hobby not found"}), 404

    def create_hobby(self) -> tuple[Response, Literal[201]] | tuple[Response, Literal[500]]:
        """
        Creates a new hobby.

        Returns:
            A JSON response containing the serialized hobby if successful, or a JSON response with an error message and status code 500 if unsuccessful.
        """
        hobby_data = request.get_json()
        hobby = self.model.create_hobby(hobby_data)
        if hobby:
            return jsonify(hobby.serialize()), 201
        else:
            return jsonify({"message": "Internal server error"}), 500

    def update_hobby(self, hobby_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[404]]:
        """
        Updates a hobby.

        Args:
            hobby_id (int): The ID of the hobby.

        Returns:
            A JSON response containing the serialized hobby if successful, or a JSON response with an error message and status code 404 if unsuccessful.
        """
        hobby_data = request.get_json()
        hobby = self.model.update_hobby(hobby_id, hobby_data)
        if hobby:
            return jsonify(hobby.serialize()), 200
        else:
            return jsonify({"message": "Hobby not found"}), 404

    def delete_hobby(self, hobby_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[404]]:
        """
        Deletes a hobby.

        Args:
            hobby_id (int): The ID of the hobby.

        Returns:
            A JSON response containing the serialized hobby if successful, or a JSON response with an error message and status code 404 if unsuccessful.
        """
        hobby = self.model.delete_hobby(hobby_id)
        if hobby:
            return jsonify(hobby.serialize()), 200
        else:
            return jsonify({"message": "Hobby not found"}), 404

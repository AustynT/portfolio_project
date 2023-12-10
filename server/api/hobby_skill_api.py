from typing import Literal
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.type_model import TypeModel
from server.schemas.type_schema import TypeSchema


class HobbySkillApi:
    """
    API class for managing hobby skills.
    """

    def __init__(self) -> None:
        self.bp_hobby_skill = Blueprint(
            'hobby_skill', __name__, url_prefix='/hobby_skill')
        self.bp_hobby_skill.route(
            '/', methods=['GET'])(self.get_hobby_skills)
        self.bp_hobby_skill.route('/<int:hobby_skill_id>',
                                  methods=['GET'])(self.get_hobby_skill_by_id)
        self.bp_hobby_skill.route(
            '/', methods=['POST'])(jwt_required())(self.create_hobby_skill)
        self.bp_hobby_skill.route('/<int:hobby_skill_id>',
                                  methods=['PUT'])(jwt_required())(self.update_hobby_skill)
        self.bp_hobby_skill.route(
            '/<int:hobby_skill_id>', methods=['DELETE'])(jwt_required()(self.delete_hobby_skill))

        self.request_schema: dict[str, TypeSchema] = TypeSchema(
        ).get_request_schemas()
        self.response_schema: dict[str, TypeSchema] = TypeSchema(
        ).get_response_schemas()
        self.model = TypeModel

    def get_hobby_skills(self) -> Response:
        """
        Get all hobby skills.

        Returns:
            A JSON response containing the serialized hobby skills.
        """
        hobby_skills = self.model.query.all()
        return jsonify([hobby_skill.serialize() for hobby_skill in hobby_skills])

    def get_hobby_skill_by_id(self, hobby_skill_id) -> Response | tuple[Response, Literal[404]]:
        """
        Get a hobby skill by its ID.

        Args:
            hobby_skill_id (int): The ID of the hobby skill.

        Returns:
            A JSON response containing the serialized hobby skill if found, or a JSON response with an error message and status code 404 if not found.
        """
        hobby_skill_instance = self.model.query.get(hobby_skill_id)
        if hobby_skill_instance:
            return jsonify(hobby_skill_instance.serialize())
        else:
            return jsonify({"message": "Hobby skill not found"}), 404

    def create_hobby_skill(self) -> tuple[Response, Literal[201]] | tuple[Response, Literal[500]]:
        """
        Creates a new hobby skill.

        Returns:
            A JSON response containing the serialized hobby skill if successful, or a JSON response with an error message and status code 500 if unsuccessful.
        """
        hobby_skill_data = request.get_json()
        if self.request_schema['create'].validate(hobby_skill_data):
            hobby_skill = self.model.create_hobby_skill(hobby_skill_data)
            return jsonify(hobby_skill.serialize()), 201

        return jsonify({"message": "Invalid request data"}), 400

    def update_hobby_skill(self, hobby_skill_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[400]]:
        """
        Updates a hobby skill.

        Args:
            hobby_skill_id (int): The ID of the hobby skill.

        Returns:
            A JSON response containing the serialized hobby skill if successful, or a JSON response with an error message and status code 400 if unsuccessful.
        """
        hobby_skill_data = request.get_json()
        if self.request_schema['update'].validate(hobby_skill_data):
            hobby_skill = self.model.update_hobby_skill(
                hobby_skill_id, hobby_skill_data)
            return jsonify(hobby_skill.serialize()), 200

        return jsonify({"message": "Invalid request data"}), 400

    def delete_hobby_skill(self, hobby_skill_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[404]]:
        """
        Deletes a hobby skill.

        Args:
            hobby_skill_id (int): The ID of the hobby skill.

        Returns:
            A JSON response with an error message and status code 404 if the hobby skill was not found, or a JSON response with an error message and status code 500 if the hobby skill could not be deleted, or a JSON response with a success message and status code 200 if the hobby skill was deleted successfully.
        """
        hobby_skill = self.model.query.get(hobby_skill_id)
        if hobby_skill:
            hobby_skill.delete()
            return jsonify({"message": "Hobby skill deleted"}), 200

        return jsonify({"message": "Hobby skill not found"}), 404

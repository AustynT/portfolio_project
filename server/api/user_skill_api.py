from typing import Literal
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.user_skill_model import UserSkillModel
from server.schemas.user_skill_schmea import UserSkillSchema


class UserSkillApi:
    """
    API class for managing user skills.
    """

    def __init__(self):
        self.bp_user_skill = Blueprint(
            'user_skill', __name__, url_prefix='/user_skill')
        self.bp_user_skill.route('/', methods=['GET'])(self.get_user_skills)
        self.bp_user_skill.route(
            '/<int:user_skill_id>', methods=['GET'])(self.get_user_skill_by_id)
        self.bp_user_skill.route(
            '/', methods=['POST'])(jwt_required()(self.create_user_skill))
        self.bp_user_skill.route(
            '/<int:user_skill_id>', methods=['PUT'])(jwt_required()(self.update_user_skill))
        self.bp_user_skill.route(
            '/<int:user_skill_id>', methods=['DELETE'])(jwt_required()(self.delete_user_skill))

        self.request_schema = UserSkillSchema().get_request_schemas()
        self.response_schema = UserSkillSchema().get_response_schemas()
        self.model = UserSkillModel()

    def get_user_skills(self) -> Response:
        """
        Get all user skills.

        Returns:
            A JSON response containing the serialized user skills.
        """
        user_skills = self.model.get_all_user_skills()
        return jsonify([user_skill.serialize() for user_skill in user_skills])

    def get_user_skill_by_id(self, user_skill_id) -> Response | tuple[Response, Literal[404]]:
        """
        Get a user skill by its ID.

        Args:
            user_skill_id (int): The ID of the user skill.

        Returns:
            A JSON response containing the serialized user skill if found, or a JSON response with an error message and status code 404 if not found.
        """
        user_skill_instance = self.model.get_user_skill_by_id(user_skill_id)
        if user_skill_instance:
            return jsonify(user_skill_instance.serialize())
        else:
            return jsonify({"message": "User Skill not found"}), 404

    def create_user_skill(self) -> tuple[Response, Literal[201]] | tuple[Response, Literal[400]]:
        """
        Creates a new user skill.

        Returns:
            A JSON response containing the serialized user skill if successful, or a JSON response with an error message and status code 400 if not successful.
        """
        try:
            request_data = request.get_json()
            user_skill = self.model.create_user_skill(request_data)
            return jsonify(user_skill.serialize()), 201
        except Exception as e:
            return jsonify({"message": str(e)}), 400

    def update_user_skill(self, user_skill_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[400]]:
        """
        Updates a user skill.

        Args:
            user_skill_id (int): The ID of the user skill.

        Returns:
            A JSON response containing the serialized user skill if successful, or a JSON response with an error message and status code 400 if not successful.
        """
        try:
            request_data = request.get_json()
            user_skill = self.model.update_user_skill(
                user_skill_id, request_data)
            return jsonify(user_skill.serialize()), 200
        except Exception as e:
            return jsonify({"message": str(e)}), 400

    def delete_user_skill(self, user_skill_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[404]]:
        """
        Deletes a user skill.

        Args:
            user_skill_id (int): The ID of the user skill.

        Returns:
            A JSON response containing the serialized user skill if successful, or a JSON response with an error message and status code 404 if not successful.
        """
        try:
            user_skill = self.model.delete_user_skill(user_skill_id)
            return jsonify(user_skill.serialize()), 200
        except Exception as e:
            return jsonify({"message": str(e)}), 404

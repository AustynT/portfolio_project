from typing import Literal
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.skill_model import SkillModel
from server.schemas.skill_schema import SkillSchema


class SkillApi:
    """
    API class for managing skills.
    """

    def __init__(self):
        self.bp_skill = Blueprint('skill', __name__, url_prefix='/skill')
        self.bp_skill.route(
            '/', methods=['GET'])(self.get_skills)
        self.bp_skill.route('/<int:skill_id>',
                            methods=['GET'])(self.get_skill_by_id)
        self.bp_skill.route(
            '/', methods=['POST'])(jwt_required())(self.create_skill)
        self.bp_skill.route('/<int:skill_id>',
                            methods=['PUT'])(jwt_required())(self.update_skill)
        self.bp_skill.route(
            '/<int:skill_id>', methods=['DELETE'])(jwt_required()(self.delete_skill))

        self.request_schema = SkillSchema().get_request_schemas()
        self.response_schema = SkillSchema().get_response_schemas()
        self.model = SkillModel()

    def get_skills(self):
        """
        Get all skills.

        Returns:
            A JSON response containing the serialized skills.
        """
        skills = self.model.get_all_skills()
        return jsonify([skill.serialize() for skill in skills])

    def get_skill_by_id(self, skill_id):
        """
        Get a skill by its ID.

        Args:
            skill_id (int): The ID of the skill.

        Returns:
            A JSON response containing the serialized skill if found, or a JSON response with an error message and status code 404 if not found.
        """
        skill_instance = self.model.get_skill_by_id(skill_id)
        if skill_instance:
            return jsonify(skill_instance.serialize())
        else:
            return jsonify({"message": "Skill not found"}), 404

    def create_skill(self):
        """
        Creates a new skill.

        Returns:
            A JSON response containing the serialized skill if successful, or a JSON response with an error message and status code 500 if unsuccessful.
        """
        request_data = request.get_json()
        if self.request_schema['create'].validate(request_data):
            skill = self.model.create_skill(request_data)
            return jsonify(skill.serialize()), 201
        else:
            return jsonify({"message": "Invalid request data"}), 400

    def update_skill(self, skill_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[400]]:
        """
        Updates a skill.

        Args:
            skill_id (int): The ID of the skill.

        Returns:
            A JSON response containing the serialized skill if successful, or a JSON response with an error message and status code 500 if unsuccessful.
        """
        request_data = request.get_json()
        if self.request_schema['update'].validate(request_data):
            skill = self.model.update_skill(skill_id, request_data)
            return jsonify(skill.serialize()), 200
        else:
            return jsonify({"message": "Invalid request data"}), 400

    def delete_skill(self, skill_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[404]]:
        """
        Deletes a skill.

        Args:
            skill_id (int): The ID of the skill.

        Returns:
            A JSON response with an error message and status code 404 if the skill is not found, or a JSON response with an error message and status code 500 if unsuccessful.
        """
        skill = self.model.delete_skill(skill_id)
        if skill:
            return jsonify({"message": "Skill deleted"}), 200
        else:
            return jsonify({"message": "Skill not found"}), 404

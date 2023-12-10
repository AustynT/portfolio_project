from typing import Literal
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.project_skill_model import ProjectSkillModel
from server.schemas.project_skill_schema import ProjectSkillSchema


class ProjectSkillApi:
    """
    API class for managing project skills.
    """

    def __init__(self):
        self.bp_project_skill = Blueprint(
            'project_skill', __name__, url_prefix='/project_skill')
        self.bp_project_skill.route(
            '/', methods=['GET'])(self.get_project_skills)
        self.bp_project_skill.route(
            '/<int:project_skill_id>', methods=['GET'])(self.get_project_skill_by_id)
        self.bp_project_skill.route(
            '/', methods=['POST'])(jwt_required())(self.create_project_skill)
        self.bp_project_skill.route(
            '/<int:project_skill_id>', methods=['PUT'])(jwt_required())(self.update_project_skill)
        self.bp_project_skill.route(
            '/<int:project_skill_id>', methods=['DELETE'])(jwt_required()(self.delete_project_skill))

        self.request_schema = ProjectSkillSchema().get_request_schemas()
        self.response_schema = ProjectSkillSchema().get_response_schemas()
        self.model = ProjectSkillModel()

    def get_project_skills(self) -> Response:
        """
        Get all project skills.

        Returns:
            A JSON response containing the serialized project skills.
        """
        project_skills = self.model.get_all_project_skills()
        return jsonify([project_skill.serialize() for project_skill in project_skills])

    def get_project_skill_by_id(self, project_skill_id) -> Response | tuple[Response, Literal[404]]:
        """
        Get a project skill by its ID.

        Args:
            project_skill_id (int): The ID of the project skill.

        Returns:
            A JSON response containing the serialized project skill if found, or a JSON response with an error message and status code 404 if not found.
        """
        project_skill_instance = self.model.get_project_skill_by_id(
            project_skill_id)
        if project_skill_instance:
            return jsonify(project_skill_instance.serialize())
        else:
            return jsonify({"message": "Project Skill not found"}), 404

    def create_project_skill(self) -> tuple[Response, Literal[201]] | tuple[Response, Literal[400]]:
        """
        Creates a new project skill.

        Returns:
            A JSON response containing the serialized project skill if successful, or a JSON response with an error message and status code 500 if unsuccessful.
        """
        request_data = request.get_json()
        if self.request_schema['create'].validate(request_data):
            project_skill = self.model.create_project_skill(request_data)
            return jsonify(project_skill.serialize()), 201
        else:
            return jsonify({"message": "Invalid request data"}), 400

    def update_project_skill(self, project_skill_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[400]]:
        """
        Updates a project skill.

        Args:
            project_skill_id (int): The ID of the project skill.

        Returns:
            A JSON response containing the serialized project skill if successful, or a JSON response with an error message and status code 500 if unsuccessful.
        """
        request_data = request.get_json()
        if self.request_schema['update'].validate(request_data):
            project_skill = self.model.update_project_skill(
                project_skill_id, request_data)
            return jsonify(project_skill.serialize()), 200
        else:
            return jsonify({"message": "Invalid request data"}), 400

    def delete_project_skill(self, project_skill_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[404]]:
        """
        Deletes a project skill.

        Args:
            project_skill_id (int): The ID of the project skill.

        Returns:
            A JSON response with an empty object and status code 204 if successful, or a JSON response with an error message and status code 404 if unsuccessful.
        """
        project_skill = self.model.delete_project_skill(project_skill_id)
        if project_skill:
            return jsonify({}), 204
        else:
            return jsonify({"message": "Project Skill not found"}), 404

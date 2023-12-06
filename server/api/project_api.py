from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.project_model import ProjectModel
from server.schemas.user_schema import UserSchema as ProjectSchema


class ProjectsApi:
    """ 
    API class for managing projects.
    """

    def __init__(self):
        self.bp_project = Blueprint('project', __name__, url_prefix='/project')
        self.bp_project.route(
            '/', methods=['GET'])(jwt_required()(self.get_projects))
        self.bp_project.route('/<int:project_id>',
                              methods=['GET'])(self.get_project_by_id)
        self.bp_project.route(
            '/', methods=['POST'])(jwt_required()(self.create_project))
        self.bp_project.route('/<int:project_id>',
                              methods=['PUT'])(jwt_required()(self.update_project))
        self.bp_project.route(
            '/<int:project_id>', methods=['DELETE'])(jwt_required()(self.delete_project))
        self.request_schema = ProjectSchema().get_request_schemas()
        self.response_schema = ProjectSchema().get_response_schemas()

    def get_projects(self):
        """
        Get all projects.

        Returns:
            A JSON response containing the serialized projects.
        """
        projects = ProjectModel.query.all()
        return jsonify([project.serialize() for project in projects])

    def get_project_by_id(self, project_id):
        """
        Get a project by its ID.

        Args:
            project_id (int): The ID of the project.

        Returns:
            A JSON response containing the serialized project if found, or a JSON response with an error message and status code 404 if not found.
        """
        project = ProjectModel.query.get(project_id)
        if project:
            return jsonify(project.serialize())
        else:
            return jsonify({"message": "Project not found"}), 404

    def create_project(self):
        # Add logic for creating a project with JWT authentication
        pass

    def update_project(self, project_id):
        # Add logic for updating a project with JWT authentication
        pass

    def delete_project(self, project_id):
        # Add logic for deleting a project with JWT authentication
        pass

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.user_model import UserModel
from server.schemas.user_schemas import UserSchema


class ProjectsApi:
    """
    API class for managing projects.
    """

    def __init__(self):
        self.bp_project = Blueprint('project', __name__, url_prefix='/project')
        self.bp_project.route(
            '/', methods=['GET'])(jwt_required()(self.get_users))
        self.bp_project.route('/<int:user_ids>',
                              methods=['GET'])(self.get_user_by_id)
        self.bp_project.route(
            '/', methods=['POST'])(jwt_required()(self.create_user))
        self.bp_project.route('/<int:user_ids>',
                              methods=['PUT'])(jwt_required()(self.update_user))
        self.bp_project.route(
            '/<int:user_ids>', methods=['DELETE'])(jwt_required()(self.delete_user))

        self.request_schema = UserSchema().get_request_schemas()
        self.response_schema = UserSchema().get_response_schemas()

    def get_users(self):
        """
        Get all projects.

        Returns:
            A JSON response containing the serialized projects.
        """
        projects = UserModel.query.all()
        return jsonify([project.serialize() for project in projects])

    def get_user_by_id(self, user_id):
        """
        Get a project by its ID.

        Args:
            project_id (int): The ID of the project.

        Returns:
            A JSON response containing the serialized project if found, or a JSON response with an error message and status code 404 if not found.
        """
        data = self.request_schema['read'].load(request.get_json())

        project = UserModel.query.get(user_id)
        if project:
            return jsonify(project.serialize())
        else:
            return jsonify({"message": "Project not found"}), 404

    def create_user(self):
        """
        Creates a new user.

        Returns:
            A JSON response containing the created user's information.
        """
        data = self.request_schema['create']
        user = UserModel()

        user.session.add(data)
        user.session.commit()

        return jsonify(self.response_schema['create'].dump({
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "password": user.password
        })), 201

    def update_user(self, user_id):
        """
        Update a project by its ID.

        Args:
            user_id (int): The ID of the project.
        Returns:
            A JSON response containing the serialized project if found, or a JSON response with an error message and status code 404 if not found.
        """

        user = UserModel.query.get(user_id)
        if not user:
            return jsonify({"message": "Project not found"}), 404

        data = self.request_schema['update'].load(request.get_json())

        user.session.add(data)
        user.session.commit()

        return jsonify(self.response_schema['update'].dump({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "password": user.password
        })), 200

    def delete_user(self, user_id):
        """
        Delete a project by its ID.

        Args:
            user_id (int): The ID of the project.

        Returns:
            A JSON response with a message indicating the user was deleted if found, or a JSON response with an error message and status code 404 if not found.
        """
        user = UserModel.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404

        user.session.delete(user)
        user.session.commit()
        return jsonify({"message": "User deleted"}), 200

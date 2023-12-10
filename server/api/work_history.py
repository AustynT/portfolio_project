from typing import Literal
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.work_history_model import WorkHistoryModel
from server.schemas.work_history_schema import WorkHistorySchema


class WrokHistoryApi:

    def __init__(self):
        self.bp_work_history = Blueprint(
            'work_history', __name__, url_prefix='/work_history')
        self.bp_work_history.route(
            '/', methods=['GET'])(self.get_work_history)
        self.bp_work_history.route(
            '/<int:work_history_id>', methods=['GET'])(self.get_work_history_by_id)
        self.bp_work_history.route(
            '/', methods=['POST'])(jwt_required()(self.create_work_history))
        self.bp_work_history.route(
            '/<int:work_history_id>', methods=['PUT'])(jwt_required()(self.update_work_history))
        self.bp_work_history.route(
            '/<int:work_history_id>', methods=['DELETE'])(jwt_required()(self.delete_work_history))

        self.request_schema = WorkHistorySchema().get_request_schemas()
        self.response_schema = WorkHistorySchema().get_response_schemas()
        self.model = WorkHistoryModel()

    def get_work_history(self) -> Response:
        """
        Get all work history.

        Returns:
            A JSON response containing the serialized work history.
        """
        work_history = self.model.get_all_work_history()
        return jsonify([work_history.serialize() for work_history in work_history])

    def get_work_history_by_id(self, work_history_id) -> Response | tuple[Response, Literal[404]]:
        """
        Get a work history by its ID.

        Args:
            work_history_id (int): The ID of the work history.

        Returns:
            A JSON response containing the serialized work history if found, or a JSON response with an error message and status code 404 if not found.
        """
        work_history_instance = self.model.get_work_history_by_id(
            work_history_id)
        if work_history_instance:
            return jsonify(work_history_instance.serialize())
        else:
            return jsonify({"message": "Work History not found"}), 404

    def create_work_history(self) -> tuple[Response, Literal[201]] | tuple[Response, Literal[400]]:
        """
        Creates a new work history.

        Returns:
            A JSON response containing the serialized work history if successful, or a JSON response with an error message and status code 400 if unsuccessful.
        """
        request_data = request.get_json()
        validation_errors = self.request_schema.validate(request_data)
        if validation_errors:
            return jsonify(validation_errors), 400
        else:
            work_history_instance = self.model.create_work_history(
                request_data)
            return jsonify(work_history_instance.serialize()), 201

    def update_work_history(self, work_history_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[400]]:
        """
        Updates a work history.

        Args:
            work_history_id (int): The ID of the work history.

        Returns:
            A JSON response containing the serialized work history if successful, or a JSON response with an error message and status code 400 if unsuccessful.
        """
        request_data = request.get_json()
        validation_errors = self.request_schema.validate(request_data)
        if validation_errors:
            return jsonify(validation_errors), 400
        else:
            work_history_instance = self.model.update_work_history(
                work_history_id, request_data)
            return jsonify(work_history_instance.serialize()), 200

    def delete_work_history(self, work_history_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[404]]:
        """
        Deletes a work history.

        Args:
            work_history_id (int): The ID of the work history.

        Returns:
            A JSON response with status code 200 if successful, or a JSON response with an error message and status code 404 if unsuccessful.
        """
        work_history_instance = self.model.delete_work_history(
            work_history_id)
        if work_history_instance:
            return jsonify({"message": "Work History deleted"}), 200
        else:
            return jsonify({"message": "Work History not found"}), 404

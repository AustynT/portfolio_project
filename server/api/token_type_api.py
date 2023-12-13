from typing import Literal
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required

from server.models.token_type_model import TokenTypeModel
from server.schemas.token_type_schema import TokenTypeSchema


class TokenTypeApi:
    """
    API class for managing token types.
    """

    def __init__(self):
        self.bp_token_type = Blueprint(
            'token_type', __name__, url_prefix='/token_type')
        self.bp_token_type.route(
            '/', methods=['GET'])(jwt_required())(self.get_token_types)
        self.bp_token_type.route(
            '/', methods=['POST'])(jwt_required())(self.create_token_type)
        self.bp_token_type.route('/<int:token_type_id>', methods=[
                                 'GET'], endpoint='get_token_type_by_id')(self.get_token_type_by_id)
        self.bp_token_type.route('/<int:token_type_id>', methods=[
                                 'PUT'], endpoint='update_token_type')(jwt_required())(self.update_token_type)
        self.bp_token_type.route('/<int:token_type_id>', methods=[
                                 'DELETE'], endpoint='delete_token_type')(jwt_required()(self.delete_token_type))

        self.request_schema = TokenTypeSchema().get_request_schemas()
        self.response_schema = TokenTypeSchema().get_response_schemas()
        self.model = TokenTypeModel()

    def get_token_types(self):
        """
        Get all token_types.

        Returns:
            A JSON response containing the serialized token_types.
        """
        token_types = self.model.get_all_token_types()
        return jsonify([token_type.serialize() for token_type in token_types])

    def get_token_type_by_id(self, token_type_id):
        """
        Get a token_type by its ID.

        Args:
            token_type_id (int): The ID of the token_type.

        Returns:
            A JSON response containing the serialized token_type if found, or a JSON response with an error message and status code 404 if not found.
        """
        token_type_instance = self.model.get_token_type_by_id(token_type_id)
        if token_type_instance:
            return jsonify(token_type_instance.serialize())
        else:
            return jsonify({"message": "TokenType not found"}), 404

    def create_token_type(self):
        """
        Creates a new token_type.

        Returns:
            A JSON response containing the serialized token_type if successful, or a JSON response with an error message and status code 500 if unsuccessful.
        """
        request_data = request.get_json()
        errors = self.request_schema.validate(request_data)
        if errors:
            return jsonify(errors), 400
        else:
            token_type_instance = self.model.create_token_type(request_data)
            if token_type_instance:
                return jsonify(token_type_instance.serialize())
            else:
                return jsonify({"message": "TokenType could not be created"}), 500

    def update_token_type(self, token_type_id):
        """
        Updates a token_type.

        Args:
            token_type_id (int): The ID of the token_type.

        Returns:
            A JSON response containing the serialized token_type if successful, or a JSON response with an error message and status code 404 if unsuccessful.
        """
        request_data = request.get_json()
        errors = self.request_schema.validate(request_data)
        if errors:
            return jsonify(errors), 400
        else:
            token_type_instance = self.model.update_token_type(
                token_type_id, request_data)
            if token_type_instance:
                return jsonify(token_type_instance.serialize())
            else:
                return jsonify({"message": "TokenType not found"}), 404

    def delete_token_type(self, token_type_id):
        """
        Deletes a token_type.

        Args:
            token_type_id (int): The ID of the token_type.

        Returns:
            A JSON response with an error message and status code 404 if the token_type was not found, or a JSON response with a success message and status code 200 if successful.
        """
        if self.model.delete_token_type(token_type_id):
            return jsonify({"message": "TokenType deleted"}), 200
        else:
            return jsonify({"message": "TokenType not found"}), 404

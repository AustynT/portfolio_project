from typing import Any, Literal
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required

from server.models.token_type_model import TokenTypeModel
from server.schemas.token_type_schema import TokenTypeSchema


class TokenTypeApi:
    """
    API class for managing token types.
    """

    # def __init__(self) -> None:
    #     self.bp_token_type = Blueprint(
    #         'token_types', __name__, url_prefix='/token_type')
    #     self.bp_token_type.route(
    #         '/', methods=['GET'], endpoint="get_token_types")(jwt_required())(self.get_token_types)
    #     self.bp_token_type.route(
    #         '/', methods=['POST'])(jwt_required())(self.create_token_type)
    #     self.bp_token_type.route('/<int:token_type_id>', methods=[
    #                              'GET'], endpoint='get_token_type_by_id')(self.get_token_type_by_id)
    #     self.bp_token_type.route('/<int:token_type_id>', methods=[
    #                              'PUT'], endpoint='update_token_type')(jwt_required())(self.update_token_type)
    #     self.bp_token_type.route('/<int:token_type_id>', methods=[
    #                              'DELETE'], endpoint='delete_token_type')(jwt_required()(self.delete_token_type))

    #     self.request_schema: dict[str,
    #                               Any] = TokenTypeSchema().get_request_schemas()
    #     self.response_schema: dict[str, Any] = TokenTypeSchema(
    #     ).get_response_schemas()
    #     self.model = TokenTypeModel()

    # def get_token_types(self) -> Response:
    #     """
    #     Get all token_types.

    #     Returns:
    #         A JSON response containing the serialized token_types.
    #     """
    #     token_types = self.model.get()
    #     return jsonify([token_type.serialize() for token_type in token_types])

    # def get_token_type_by_id(self, token_type_id) -> Response | tuple[Response, Literal[404]]:
    #     """
    #     Get a token_type by its ID.

    #     Args:
    #         token_type_id (int): The ID of the token_type.

    #     Returns:
    #         A JSON response containing the serialized token_type if found, or a JSON response with an error message and status code 404 if not found.
    #     """
    #     token_type_instance = self.model.get(token_type_id)
    #     if token_type_instance:
    #         return jsonify(token_type_instance.serialize())
    #     else:
    #         return jsonify({"message": "TokenType not found"}), 404

    # def create_token_type(self) -> tuple[Response, Literal[400]] | Response | tuple[Response, Literal[500]]:
    #     """
    #     Creates a new token_type.

    #     Returns:
    #         A JSON response containing the serialized token_type if successful, or a JSON response with an error message and status code 500 if unsuccessful.
    #     """
    #     request_data = request.get_json()
    #     errors = self.request_schema.validate(request_data)
    #     if errors:
    #         return jsonify(errors), 400
    #     else:
    #         token_type_instance = self.model.create(request_data)
    #         if token_type_instance:
    #             return jsonify(token_type_instance.serialize())
    #         else:
    #             return jsonify({"message": "TokenType could not be created"}), 500

    # def update_token_type(self, token_type_id) -> tuple[Response, Literal[400]] | Response | tuple[Response, Literal[404]]:
    #     """
    #     Updates a token_type.

    #     Args:
    #         token_type_id (int): The ID of the token_type.

    #     Returns:
    #         A JSON response containing the serialized token_type if successful, or a JSON response with an error message and status code 404 if unsuccessful.
    #     """
    #     request_data = request.get_json()
    #     errors = self.request_schema.validate(request_data)
    #     if errors:
    #         return jsonify(errors), 400
    #     else:
    #         token_type_instance = self.model.update(
    #             token_type_id, request_data)
    #         if token_type_instance:
    #             return jsonify(token_type_instance.serialize())
    #         else:
    #             return jsonify({"message": "TokenType not found"}), 404

    # def delete_token_type(self, token_type_id) -> tuple[Response, Literal[200]] | tuple[Response, Literal[404]]:
    #     """
    #     Deletes a token_type.

    #     Args:
    #         token_type_id (int): The ID of the token_type.

    #     Returns:
    #         A JSON response with an error message and status code 404 if the token_type was not found, or a JSON response with a success message and status code 200 if successful.
    #     """

    #     if self.model.delete(token_type_id):
    #         return jsonify({"message": "TokenType deleted"}), 200
    #     else:
    #         return jsonify({"message": "TokenType not found"}), 404

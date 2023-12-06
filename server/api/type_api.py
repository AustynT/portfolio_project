from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.type_model import TypeModel
from server.schemas.type_schema import TypeSchema


class TypeApi:
    """
    API class for managing types.
    """

    def __init__(self):
        self.bp_type = Blueprint('type', __name__, url_prefix='/type')
        self.bp_type.route(
            '/', methods=['GET'])(self.get_types)
        self.bp_type.route('/<int:type_id>',
                           methods=['GET'])(self.get_type_by_id)
        self.bp_type.route(
            '/', methods=['POST'])(jwt_required())(self.create_type)
        self.bp_type.route('/<int:type_id>',
                           methods=['PUT'])(jwt_required())(self.update_type)
        self.bp_type.route(
            '/<int:type_id>', methods=['DELETE'])(jwt_required()(self.delete_type))

        self.request_schema = TypeSchema().get_request_schemas()
        self.response_schema = TypeSchema().get_response_schemas()
        self.model = TypeModel

    def get_types(self):
        """
        Get all types.

        Returns:
            A JSON response containing the serialized types.
        """
        types = self.model.query.all()
        return jsonify([type.serialize() for type in types])

    def get_type_by_id(self, type_id):
        """
        Get a type by its ID.

        Args:
            type_id (int): The ID of the type.

        Returns:
            A JSON response containing the serialized type if found, or a JSON response with an error message and status code 404 if not found.
        """
        type_instance = self.model.query.get(type_id)
        if type_instance:
            return jsonify(type_instance.serialize())
        else:
            return jsonify({"message": "Type not found"}), 404

    def create_type(self):
        """
        Creates a new type.

        Returns:
            A JSON response containing the serialized type if successful, or a JSON response with an error message and status code 500 if unsuccessful.
        """
        self.request_schema['create'].load(request.get_json())
        type_instance = self.model(**request.get_json())
        type_instance.save()

        if type_instance.id:
            return jsonify(type_instance.serialize()), 201

        return jsonify({"message": "Error creating type"}), 500

    def update_type(self, type_id):
        """
        Updates a type.

        Args:
            type_id (int): The ID of the type.

        Returns:
            A JSON response containing the serialized type if successful, or a JSON response with an error message and status code 500 if unsuccessful.
        """
        self.request_schema['update'].load(request.get_json())
        type_instance = self.model.query.get(type_id)

        if type_instance:
            type_instance.update(**request.get_json())
            return jsonify(type_instance.serialize()), 200

        return jsonify({"message": "Type not found"}), 404

    def delete_type(self, type_id):
        """
        Deletes a type.

        Args:
            type_id (int): The ID of the type.

        Returns:
            A JSON response with status code 204 if successful, or a JSON response with an error message and status code 404 if unsuccessful.
        """
        type_instance = self.model.query.get(type_id)

        if type_instance:
            type_instance.delete()
            return jsonify({}), 204

        return jsonify({"message": "Type not found"}), 404

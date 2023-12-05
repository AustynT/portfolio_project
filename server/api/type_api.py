from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from server.models.type_model import TypeModel
from server.schemas.type_schema import TypeSchema


class TypeApi:
    """
    API class for managing types.
    """

    def __init__(self):
        self.bp_type = Blueprint('type', __name__, url_prefix='/type')
        self.bp_type.route('/', methods=['GET']
                           )(jwt_required()(self.get_types))
        self.bp_type.route(
            '/<int:type_id>', methods=['GET'])(self.get_type_by_id)
        self.bp_type.route(
            '/', methods=['POST'])(jwt_required()(self.create_type))
        self.bp_type.route(
            '/<int:type_id>', methods=['PUT'])(jwt_required()(self.update_type))
        self.bp_type.route(
            '/<int:type_id>', methods=['DELETE'])(jwt_required()(self.delete_type))
        self.request_schema = TypeSchema().get_request_schemas()
        self.response_schema = TypeSchema().get_response_schemas()

    def get_types(self):
        types = TypeModel.query.all()
        return jsonify([type_.serialize() for type_ in types])

    def get_type_by_id(self, type_id):
        type_ = TypeModel.query.get(type_id)
        if type_:
            return jsonify(type_.serialize())
        else:
            return jsonify({"message": "Type not found"}), 404

    def create_type(self):
        # Add logic for creating a type with JWT authentication
        pass

    def update_type(self, type_id):
        # Add logic for updating a type with JWT authentication
        pass

    def delete_type(self, type_id):
        # Add logic for deleting a type with JWT authentication
        pass

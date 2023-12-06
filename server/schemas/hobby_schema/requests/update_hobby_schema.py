from marshmallow import Schema, fields


class UpdateHobbySchema(Schema):
    """
    Schema class for validating update type requests.
    """
    id = fields.Integer(required=True)
    name = fields.String
    description = fields.String
    user_id = fields.Integer(required=True)
    type_id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)

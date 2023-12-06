from marshmallow import Schema, fields


class CreateProjectRequest(Schema):
    """
    Schema class for validating create type requests.
    """
    name = fields.String(required=True)
    description = fields.String(required=True)
    user_id = fields.Integer(required=True)
    type_id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)

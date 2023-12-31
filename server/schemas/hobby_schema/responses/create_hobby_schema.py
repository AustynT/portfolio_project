from marshmallow import Schema, fields


class CreateHobbySchema(Schema):
    """
    Schema class for validating create type requests.
    """
    title = fields.String(required=True)
    description = fields.String(required=True)
    user_id = fields.Integer(required=True)
    type_id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    project_image = fields.String(required=True)

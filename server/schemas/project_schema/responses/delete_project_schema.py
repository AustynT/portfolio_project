from marshmallow import Schema, fields


class DeleteProjectSchema(Schema):
    """
    Schema class for validating delete type requests.
    """
    id = fields.Int(required=True)

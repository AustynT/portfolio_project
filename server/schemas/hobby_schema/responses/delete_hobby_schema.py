from marshmallow import Schema, fields


class DeleteHobbySchema(Schema):
    """
    Schema class for validating delete type requests.
    """
    id = fields.Int(required=True)

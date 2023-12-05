from marshmallow import Schema, fields


class ReadTypeRequestSchema(Schema):
    """
    Schema class for validating read type requests.
    """
    id = fields.Int(required=True)

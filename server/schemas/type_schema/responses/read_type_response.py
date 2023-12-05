from marshmallow import Schema, fields


class ReadTypeReponseSchema(Schema):
    """
    Schema class for validating create type requests.
    """
    name = fields.String(required=True)
    description = fields.String(required=True)

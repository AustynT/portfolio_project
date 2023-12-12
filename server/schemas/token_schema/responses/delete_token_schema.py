from marshmallow import Schema, fields


class DeleteTokenSchema(Schema):
    """
    Schema for the response of deleting a token.
    """
    message = fields.String(default="Token deleted successfully")

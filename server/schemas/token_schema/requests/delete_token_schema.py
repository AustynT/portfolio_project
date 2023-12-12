from marshmallow import Schema, fields


class DeleteTokenSchema(Schema):
    """
    Schema for the request to delete a token.
    """
    token_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    expires_at = fields.DateTime()

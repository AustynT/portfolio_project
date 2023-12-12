from marshmallow import Schema, fields


class CreateTokenSchema(Schema):
    """
    Schema for creating a token.

    Attributes:
        token_id (int): The ID of the token.
        token (str): The token value.
        token_type_id (int): The ID of the token type.
        user_id (int): The ID of the user associated with the token.
        expires_at (datetime): The expiration date and time of the token.
    """
    token_id = fields.Int(required=True)
    token = fields.Str(required=True)
    token_type_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    expires_at = fields.DateTime(required=True)

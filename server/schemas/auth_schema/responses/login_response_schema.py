from marshmallow import Schema, fields


class LoginResponseSchema(Schema):
    """
    Schema for validating login data.

    Attributes:
        id (int): The id of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        message (str): The message to be returned.
    """
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    jwt_token = fields.Str(required=True)
    fresh_jwt_token = fields.Str(required=True)
    message = fields.Str(default="user registered successfully")

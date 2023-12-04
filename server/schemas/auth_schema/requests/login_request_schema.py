from marshmallow import Schema, fields


class LoginRequestSchema(Schema):
    """
    Schema for validating login data.

    Attributes:
        username (str): The username of the user.
        password (str): The password of the user.
    """
    email = fields.Str(required=True)
    password = fields.Str(required=True)

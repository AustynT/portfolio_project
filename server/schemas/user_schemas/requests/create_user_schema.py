from marshmallow import Schema, fields


class CreateUserSchema(Schema):
    """
    Schema for validating and deserializing user data.

    Attributes:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
    """
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)

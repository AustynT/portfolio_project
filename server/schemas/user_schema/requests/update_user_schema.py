from marshmallow import Schema, fields


class UpdateUserSchema(Schema):
    """
    Schema for validating and deserializing user data.

    Attributes:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
    """
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()

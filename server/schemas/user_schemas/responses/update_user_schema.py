from marshmallow import Schema, fields


class UpdateUserSchema(Schema):
    """
    Schema for validating and deserializing user data.

    Attributes:
        id (int): The ID of the user.
        username (str): The username of the user.
        email (str): The email of the user.
    """
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()

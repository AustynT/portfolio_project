from marshmallow import Schema, fields


class ReadUserSchema(Schema):
    """
    Schema for validating and deserializing user data.

    Attributes:
        user_id (int): The ID of the user.
        email (str): The email of the user.
    """
    user_id = fields.Int()
    username = fields.Str()
    email = fields.Str()

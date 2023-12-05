from marshmallow import Schema, fields


class CreateUserSchema(Schema):
    """
    Schema for validating registration data.

    Attributes:
        id (int): The ID of the user.
        username (str): The username of the user.
        email (str): The email of the user.
        message (str): The message for the user.
    """
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    message = fields.Str(default="user registered successfully")

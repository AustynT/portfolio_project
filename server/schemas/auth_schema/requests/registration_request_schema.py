from marshmallow import Schema, fields


class RegistrationRequestSchema(Schema):
    """
    Schema for validating registration data.

    Attributes:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
    """
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

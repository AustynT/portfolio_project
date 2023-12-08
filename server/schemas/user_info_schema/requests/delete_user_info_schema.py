from marshmallow import Schema, fields


class DeleteUserInfoSchema(Schema):
    """
    Schema for validating and deserializing user data.

    Attributes:
        user_id (int): The ID of the user.
    """
    user_id = fields.Int(required=True)

from marshmallow import Schema, fields


class ReadUserInfoSchema(Schema):
    """
    Schema for validating and deserializing user data.

    Attributes:
        user_id (int): The ID of the user.
        firt_name (str): The first name of the user.
        last_name (str): The last name of the user.
        bio (str): The bio of the user.
        profile_picture (str): The profile picture of the user.
    """
    user_id = fields.Int(required=True)
    firt_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    bio = fields.Str(required=True)
    profile_picture = fields.Str(required=True)

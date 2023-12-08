from marshmallow import Schema, fields


class UpdateUserInfoSchema(Schema):
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
    firt_name = fields.Str()
    last_name = fields.Str()
    bio = fields.Str()
    profile_picture = fields.Str()

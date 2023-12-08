from marshmallow import Schema, fields


class CreateUserInfoSchema(Schema):
    """
    Schema for creating user information.
    """

    user_id = fields.Int(required=True)
    firt_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    bio = fields.Str(required=True)
    profile_picture = fields.Str(required=True)

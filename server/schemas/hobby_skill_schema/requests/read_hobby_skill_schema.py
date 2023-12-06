from marshmallow import Schema, fields


class ReadHobbySkillSchema(Schema):
    """
    Schema class for validating read type requests.
    """
    project_id = fields.Int(required=True)
    user_id = fields.Integer(required=True)

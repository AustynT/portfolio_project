from marshmallow import Schema, fields


class ReadHobbySkillSchema(Schema):
    """
    Schema class for validating read type requests.
    """
    hobby_id = fields.Integer()
    skill_id = fields.Integer()

from marshmallow import Schema, fields


class UpdateHobbySkillSchema(Schema):
    """
    Schema class for validating update type requests.
    """
    hobby_id = fields.Integer(required=True)
    skill_id = fields.Integer(required=True)

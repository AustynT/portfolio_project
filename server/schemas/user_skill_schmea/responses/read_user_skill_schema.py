from marshmallow import Schema, fields


class ReadUserSkillSchema(Schema):
    """
    Schema class for validating read type requests.
    """
    hobby_id = fields.Integer(required=True)
    skill_id = fields.Integer(required=True)

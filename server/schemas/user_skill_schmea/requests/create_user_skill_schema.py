from marshmallow import Schema, fields


class CreateUserSkillSchema(Schema):
    """
    Schema class for validating create type requests.
    """
    hobby_id = fields.Integer(required=True)
    skill_id = fields.Integer(required=True)

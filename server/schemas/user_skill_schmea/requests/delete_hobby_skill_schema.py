from marshmallow import Schema, fields


class DeleteHobbySkillSchema(Schema):
    """
    Schema class for validating delete type requests.
    """
    hobby_id = fields.Integer(required=True)
    skill_id = fields.Integer(required=True)

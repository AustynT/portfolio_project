from marshmallow import Schema, fields


class CreateSkillSchema(Schema):
    """
    Schema for creating a hobby skill.
    """

    skill_id = fields.Integer(required=True)
    skill_name = fields.String(required=True)

from marshmallow import Schema, fields


class UpdateSkillSchema(Schema):
    """
    Schema for updating a hobby skill.
    """

    skill_id = fields.Integer(required=True)
    skill_name = fields.String(required=True)

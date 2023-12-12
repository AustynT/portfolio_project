from marshmallow import Schema, fields


class DeleteSkillSchema(Schema):
    """
    Schema for deleting a hobby skill.
    """

    skill_id = fields.Integer(required=True)

from marshmallow import Schema, fields


class DeleteHobbySkillSchema(Schema):
    """
    Schema for deleting a hobby skill.
    """

    skill_id = fields.Integer(required=True)

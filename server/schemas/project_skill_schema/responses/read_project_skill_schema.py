from marshmallow import Schema, fields


class ReadProjectSkillSchema(Schema):
    """
    Schema class for validating read type requests.
    """
    project_id = fields.Integer(required=True)
    skill_id = fields.Integer(required=True)

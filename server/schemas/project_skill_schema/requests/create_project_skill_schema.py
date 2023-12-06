from marshmallow import Schema, fields


class CreateProjectSkillSchema(Schema):
    """
    Schema class for validating create type requests.
    """
    project_id = fields.Integer(required=True)
    skill_id = fields.Integer(required=True)

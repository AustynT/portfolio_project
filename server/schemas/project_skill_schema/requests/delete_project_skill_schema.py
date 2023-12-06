from marshmallow import Schema, fields


class DeleteProjectSkillSchema(Schema):
    """
    Schema class for validating delete type requests.
    """
    project_id = fields.Integer(required=True)
    skill_id = fields.Integer(required=True)

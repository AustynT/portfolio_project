from marshmallow import Schema, fields


class UpdateProjectSkillSchema(Schema):
    """
    Schema class for validating update type requests.
    """
    project_id = fields.Integer(required=True)
    skill_id = fields.Integer(required=True)

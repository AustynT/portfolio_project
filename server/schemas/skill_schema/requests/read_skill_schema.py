from marshmallow import Schema, fields


class ReadSkillSchema(Schema):

    skill_id = fields.Integer(required=True)
    skill_name = fields.String(required=True)

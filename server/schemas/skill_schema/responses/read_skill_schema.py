from marshmallow import Schema, fields


class ReadHobbySkillSchema(Schema):

    skill_id = fields.Integer(required=True)
    skill_name = fields.Sting(required=True)

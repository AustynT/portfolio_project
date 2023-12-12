from marshmallow import Schema, fields


class UpdateTokenTypeSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)

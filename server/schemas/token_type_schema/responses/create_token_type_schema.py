from marshmallow import Schema, fields


class CreateTokenTypeSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)

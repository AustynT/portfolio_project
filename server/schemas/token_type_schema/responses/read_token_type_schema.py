from marshmallow import Schema, fields


class ReadTokenTypeSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)

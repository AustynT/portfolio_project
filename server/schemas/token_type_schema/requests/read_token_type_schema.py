from marshmallow import Schema, fields
from marshmallow import Schema, fields


class CreateTokenTypeSchema(Schema):
    id = fields.Integer(required=True)

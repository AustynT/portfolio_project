from marshmallow import Schema, fields


class DeleteTokenTypeSchema(Schema):
    messasge = fields.String(default="Token type deleted successfully")

from marshmallow import Schema, fields


class DeleteTokenTypeSchema(Schema):
    message: fields.Str(default="Token type deleted successfully")

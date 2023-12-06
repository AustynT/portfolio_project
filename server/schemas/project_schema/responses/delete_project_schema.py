from marshmallow import Schema, fields


class DeleteProjectRequestSchema(Schema):
    """
    Schema class for validating delete type requests.
    """
    id = fields.Int(required=True)

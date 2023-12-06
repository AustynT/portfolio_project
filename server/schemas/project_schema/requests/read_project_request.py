from marshmallow import Schema, fields


class ReadProjectRequestSchema(Schema):
    """
    Schema class for validating read type requests.
    """
    project_id = fields.Int(required=True)

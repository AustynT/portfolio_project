from marshmallow import Schema, fields


class UpdateTypeSchemaRequest(Schema):
    """
    Schema class for validating update type requests.
    """
    id = fields.Int(required=True)
    name = fields.String()
    description = fields.String()

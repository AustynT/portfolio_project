from marshmallow import Schema, fields


class ReadWorkHistorySchema(Schema):
    """
    Schema for reading work history.
    """
    work_id = fields.Int(required=True)
    user_id = fields.Int(required=True)

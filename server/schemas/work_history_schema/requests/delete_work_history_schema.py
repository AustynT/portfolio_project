from marshmallow import Schema, fields


class DeleteWorkHistorySchema(Schema):
    """
    Schema for deleting work history.
    """

    work_id = fields.Int(required=True)
    user_id = fields.Int(required=True)

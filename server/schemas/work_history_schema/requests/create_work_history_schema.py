from marshmallow import Schema, fields


class CreateWorkHistorySchema(Schema):
    """
    This class implements a marshmallow schema for the request body of the create_work_history endpoint.
    """
    work_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    company_name = fields.Str(required=True)
    job_title = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    description = fields.Str(required=True)

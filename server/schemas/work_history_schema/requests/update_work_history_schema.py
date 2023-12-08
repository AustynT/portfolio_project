from marshmallow import Schema, fields


class UpdateWorkHistorySchema(Schema):
    """
    Schema for updating work history information.

    Attributes:
        work_id (int): The ID of the work history entry.
        user_id (int): The ID of the user associated with the work history entry.
        company_name (str): The name of the company.
        job_title (str): The job title.
        start_date (date): The start date of the job.
        end_date (date): The end date of the job.
        description (str): Additional description of the job.
    """
    work_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    company_name = fields.Str()
    job_title = fields.Str()
    start_date = fields.Date()
    end_date = fields.Date()
    description = fields.Str()

from server import db
from server.models.base_model import BaseModel


class WorkHistoryModel(BaseModel):
    """
    Represents a work history entry for a user.

    Attributes:
        work_id (int): The unique identifier for the work history entry.
        user_id (int): The foreign key referencing the user associated with the work history entry.
        company_name (str): The name of the company.
        job_title (str): The job title.
        start_date (datetime.date): The start date of the work history.
        end_date (datetime.date): The end date of the work history.
        description (str): Additional description for the work history.
    """

    __tablename__ = 'work_history'
    work_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    company_name = db.Column(db.String(100), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    description = db.Column(db.Text)

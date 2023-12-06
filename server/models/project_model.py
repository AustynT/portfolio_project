from server import db
from server.models.base_model import BaseModel


class ProjectModel(BaseModel):
    """
    Represents a project in the system.

    Attributes:
        project_id (int): The unique identifier for the project.
        user_id (int): The ID of the user who created the project.
        type_id (int): The ID of the type of the project.
        title (str): The title of the project.
        description (str): The description of the project.
        project_image (str): The image of the project.
        created_at (datetime): The date and time the project was created.
        project_skills (list): The skills associated with this project.
    """
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.type_id'))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    project_image = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    # Relationship for project skills
    project_skills = db.relationship('ProjectSkill', backref='project')

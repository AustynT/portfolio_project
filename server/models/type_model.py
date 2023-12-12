from server import db
from server.models.base_model import BaseModel


class TypeModel(BaseModel):
    """
    Represents a type in the system.

    Attributes:
        type_id (int): The unique identifier for the type.
        type_name (str): The name of the type.
        projects (list): The projects associated with this type.
        hobbies (list): The hobbies associated with this type.
    """
    __tablename__ = 'types'
    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), nullable=False, unique=True)

    # Relationships
    projects = db.relationship('ProjectModel', backref='type')
    hobbies = db.relationship('HobbyModel', backref='type')

from server import db
from server.models.base_model import BaseModel


class UserInfoModel(BaseModel):
    """
    Represents additional information about a user.

    Attributes:
        user_id (int): The unique identifier for the user.
        first_name (str): The first name of the user.
        last_name (str): The first name of the user.
        bio (str): The bio of the user.
        profile_picture (str): The profile picture of the user.
    """
    __tablename__ = 'user_info'
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), primary_key=True)
    firt_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    profile_picture = db.Column(db.String(255))

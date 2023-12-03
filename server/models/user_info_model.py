from server import db


class UserInfoModel(db.Model):
    """
    Represents additional information about a user.

    Attributes:
        user_id (int): The unique identifier for the user.
        full_name (str): The full name of the user.
        bio (str): The bio of the user.
        profile_picture (str): The profile picture of the user.
    """
    __tablename__ = 'user_info'
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), primary_key=True)
    full_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    profile_picture = db.Column(db.String(255))

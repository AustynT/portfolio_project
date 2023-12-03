from server import db


class User(db.Model):
    """
    Represents a user in the system.

    Attributes:
        user_id (int): The unique identifier for the user.
        username (str): The username of the user.
        password_hash (str): The hashed password of the user.
        email (str): The email address of the user.
        created_at (datetime): The timestamp when the user was created.
        user_info (UserInfo): The user's additional information.
        projects (list[Project]): The projects associated with the user.
        hobbies (list[Hobby]): The hobbies of the user.
        work_history (list[WorkHistory]): The work history of the user.
        user_skills (list[UserSkill]): The skills of the user.
    """

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    # Relationships
    user_info = db.relationship('UserInfo', backref='user', uselist=False)
    projects = db.relationship('Project', backref='user')
    hobbies = db.relationship('Hobby', backref='user')
    work_history = db.relationship('WorkHistory', backref='user')
    user_skills = db.relationship('UserSkill', backref='user')

    # Add other methods and representations as needed

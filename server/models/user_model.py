
import bcrypt
from server import db
from server.models.base_model import BaseModel


class UserModel(BaseModel):
    """
    Represents a user in the system.

    Attributes:
        user_id (int): The unique identifier for the user.
        username (str): The username of the user.
        password_hash (str): The hashed password of the user.
        email (str): The email address of the user.
        created_at (datetime): The timestamp when the user was created.
        user_info (UserInfo): The user's additional information.
        projects (List[Project]): The projects associated with the user.
        hobbies (List[Hobby]): The hobbies of the user.
        work_history (List[WorkHistory]): The work history of the user.
        user_skills (List[UserSkill]): The skills of the user.
    """
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    user_info = db.relationship('UserInfoModel', backref='user', uselist=False)
    projects = db.relationship('ProjectModel', backref='user')
    hobbies = db.relationship('HobbyModel', backref='user')
    work_history = db.relationship('WorkHistoryModel', backref='user')
    user_skills = db.relationship('UserSkillModel', backref='user')

    @classmethod
    def create(cls, **kwargs):
        """
        Create a new user instance.

        Args:
            **kwargs: Keyword arguments for the user attributes.

        Returns:
            instance: The created user instance.
        """
        if 'password' in kwargs:
            password = kwargs.pop('password')
            password_hash = cls.hash_password(password)
            kwargs['password_hash'] = password_hash

        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    # overwrite the parent update method to hash the password if it is updated
    def update(self, **kwargs):
        """
        Update the user instance.

        Args:
            **kwargs: Keyword arguments for the user attributes.
        """
        if 'password' in kwargs:
            password = kwargs.pop('password')
            password_hash = self.hash_password(password)
            kwargs['password_hash'] = password_hash

        super().update(**kwargs)

    @classmethod
    def hash_password(cls, password: str) -> str:
        """
        Hashes the password.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

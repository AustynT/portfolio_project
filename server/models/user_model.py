from server import db


class UserModel(db.Model):
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

    # create crud methods for user model
    @staticmethod
    def create(username, password_hash, email):
        """
        Create a new user.

        Args:
            username (str): The username of the user.
            password_hash (str): The hashed password of the user.
            email (str): The email address of the user.

        Returns:
            User: The newly created user object.
        """
        new_user = UserModel(username=username,
                             password_hash=password_hash, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get(user_id):
        """
        Get a user by its ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            User: The user object.
        """
        return UserModel.query.get(user_id)

    def update(self, user_data):
        """
        Update the user's information.

        Args:
            user_data (dict): The data to update the user with.
        """
        self.username = user_data['username']
        self.email = user_data['email']
        db.session.commit()

    def delete(self):
        """
        Delete the user from the database.
        """
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        """
        Serialize the user object.

        Returns:
            dict: The serialized user object.
        """
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
            'user_info': self.user_info.serialize() if self.user_info else None,
            'projects': [project.serialize() for project in self.projects],
            'hobbies': [hobby.serialize() for hobby in self.hobbies],
            'work_history': [work_history.serialize() for work_history in self.work_history],
            'user_skills': [user_skill.serialize() for user_skill in self.user_skills]
        }

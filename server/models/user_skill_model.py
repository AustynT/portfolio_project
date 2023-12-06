from server import db
from server.models.base_model import BaseModel


class UserSkillModel(BaseModel):
    """
    Represents the skills of a user.

    Attributes:
        user_id (int): The unique identifier for the user.
        skill_id (int): The unique identifier for the skill.
    """
    __tablename__ = 'user_skills'
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey(
        'skills.skill_id'), primary_key=True)

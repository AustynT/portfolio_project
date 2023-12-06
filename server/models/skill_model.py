from server import db
from server.models.base_model import BaseModel


class SkillModel(BaseModel):
    """
    Represents a skill in the system.

    Attributes:
        skill_id (int): The unique identifier for the skill.
        skill_name (str): The name of the skill.
        user_skills (list[UserSkill]): The list of user skills associated with this skill.
        project_skills (list[ProjectSkill]): The list of project skills associated with this skill.
        hobby_skills (list[HobbySkill]): The list of hobby skills associated with this skill.
    """
    __tablename__ = 'skills'
    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(50), nullable=False, unique=True)

    # Relationships
    user_skills = db.relationship('UserSkill', backref='skill')
    project_skills = db.relationship('ProjectSkill', backref='skill')
    hobby_skills = db.relationship('HobbySkill', backref='skill')

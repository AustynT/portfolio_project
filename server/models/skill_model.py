from server import db
from server.models.base_model import BaseModel


class SkillModel(BaseModel):
    __tablename__ = 'skills'
    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(50), nullable=False, unique=True)

    # Relationships
    user_skills = db.relationship('UserSkill', backref='skill')
    project_skills = db.relationship('ProjectSkill', backref='skill')
    hobby_skills = db.relationship('HobbySkill', backref='skill')

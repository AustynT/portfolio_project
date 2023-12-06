from server import db
from server.models.base_model import BaseModel


class HobbySkillModel(BaseModel):
    __tablename__ = 'hobby_skills'
    hobby_id = db.Column(db.Integer, db.ForeignKey(
        'hobbies.hobby_id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey(
        'skills.skill_id'), primary_key=True)

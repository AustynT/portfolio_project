from sqlalchemy import func
from server import db
from .base_model import BaseModel


class Token(BaseModel):
    __tablename__ = 'tokens'

    token_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False)
    token_type_id = db.Column(db.Integer, db.ForeignKey(
        'token_types.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)

    token_type = db.relationship(
        'TokenType', backref=db.backref('tokens', lazy=True))
    user = db.relationship('User', backref=db.backref('tokens', lazy=True))

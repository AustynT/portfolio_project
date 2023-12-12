from sqlalchemy import func
from server import db
from .base_model import BaseModel


class TokenType(BaseModel):
    __tablename__ = 'token_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

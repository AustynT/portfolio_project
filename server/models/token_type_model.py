from server import db
from .base_model import BaseModel


class TokenTypeModel(BaseModel):
    __tablename__ = 'token_types'

    id = db.Column(db.Integer, primary_key=True)
    toke_type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)

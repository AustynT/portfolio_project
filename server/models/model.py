"""
Base class for all models in the application.
"""
from server import db


class Model(db.Model):
    """
    Base class for all models in the application.
    """
    __abstract__ = True

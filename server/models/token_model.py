import datetime
from sqlalchemy import func
from server import db
from .base_model import BaseModel


class TokenModel(BaseModel):
    __tablename__ = 'tokens'

    token_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False)
    token_type_id = db.Column(db.Integer, db.ForeignKey(
        'token_types.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)

    token_type = db.relationship(
        'TokenTypeModel', backref=db.backref('tokens', lazy=True))
    user = db.relationship(
        'UserModel', backref=db.backref('tokens', lazy=True))

    @classmethod
    def get_by_token(cls, token: str) -> 'TokenModel':
        """
        Retrieve a token by its value.

        Args:
            token: The token to retrieve.

        Returns:
            The retrieved token.
        """
        token = cls.query.filter_by(token=token).first()
        return token

    @classmethod
    def create_token(self, user_id: int, token_type_id: int, token: str, expires_at: datetime) -> 'TokenModel':
        """
        Creates a new token.

        Args:
            user_id: The ID of the user.
            token_type_id: The ID of the token type.
            token: The token.
            expires_at: The expiration date of the token.

        Returns:
            The created token.
        """
        return TokenModel.create(user_id=user_id, token_type_id=token_type_id, token=token, expires_at=expires_at)

    @classmethod
    def refresh_token(cls, token: str, expires_at: datetime) -> 'TokenModel':
        """
        Refreshes a token.

        Args:
            token: The token to refresh.
            expires_at: The new expiration date.

        Returns:
            The refreshed token.
        """
        token = cls.get_by_token(token)
        token.expires_at = expires_at
        db.session.commit()
        return token

    @classmethod
    def update_by_token(cls, token: str, expires_at: datetime) -> 'TokenModel':
        """
        Updates a token's expiration date.

        Args:
            token: The token.
            expires_at: The new expiration date.
        """
        token = cls.get_by_token(token)
        token.expires_at = expires_at
        db.session.commit()
        return token

    @classmethod
    def delete_by_token(cls, token: str) -> None:
        """
        Deletes a token by its value.

        Args:
            token (str): The token value to be deleted.

        Returns:
            None
        """
        token: TokenModel = cls.get_by_token(token)
        token.delete()
        if token.id is not None:
            raise Exception('Token was not deleted.')

        return None

from server import db
from .base_model import BaseModel


class TokenTypeModel(BaseModel):
    """
        Model for token types.

        This class provides methods for creating, retrieving, updating, and deleting token types.

        Attributes:
            __tablename__ (str): The name of the database table.
            id (int): The ID of the token type.
            token_type (str): The token type.
            name (str): The name of the token type.
    """
    __tablename__ = 'token_types'

    id = db.Column(db.Integer, primary_key=True)
    toke_type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)

    @classmethod
    def get_by_type(cls, token_name: str) -> 'TokenTypeModel':
        """
            Retrieve a token type by its name.

            Args:
                token_name: The name of the token type to retrieve.

            Returns:
                The retrieved token type.
        """
        token_type = cls.get_all_by(token_name)
        return token_type

    @classmethod
    def create_token_type(cls, token_type: str, name: str) -> 'TokenTypeModel':
        """
            Creates a new token type.

            Args:
                token_type: The token type.
                name: The name of the token type.

            Returns:
                The created token type.
        """
        token_type = cls.create(token_type=token_type, name=name)
        return token_type

    @classmethod
    def update_token_type(cls, token_type: str, name: str) -> 'TokenTypeModel':
        """
            Updates a token type.

            Args:
                token_type: The token type.
                name: The name of the token type.

            Returns:
                The updated token type.
        """
        token_type = cls.get_by_name(token_type)
        token_type.name = name
        db.session.commit()
        return token_type

    @classmethod
    def delete_token_type(cls, token_type: str) -> None:
        """
            Deletes a token type.

            Args:
                token_type: The token type to be deleted.

            Returns:
                None
        """
        token_type: TokenTypeModel = cls.get_by_name(token_type)
        token_type.delete()
        if token_type.id is not None:
            raise Exception('Token type was not deleted.')

import datetime
from server.models.token_type_model import TokenTypeModel
from server.models.token_model import TokenModel


class JwtTokenResouce:
    """
    Resource class for managing JWT tokens.
    """
    access_token: str
    refresh_token: str

    def __init__(self):
        self.access_token = TokenTypeModel.get_by_name('JWT_ACCESS_TOKEN')
        self.refresh_token = TokenTypeModel.get_by_name('JWT_REFRESH_TOKEN')

    def create_token(self, user_id: int, token: str, expires_at: datetime) -> TokenModel:
        """
        Creates a new token.

        Args:
            user_id (int): The ID of the user.
            token (str): The token.
            expires_at (datetime): The expiration date of the token.

        Returns:
            The created token.
        """
        return TokenModel.create(token=token, token_type_id=self.token_type.id, user_id=user_id, expires_at=expires_at)

    def get_token(self, token: str) -> TokenModel:
        """
        Gets a token by its value.

        Args:
            token (str): The token.

        Returns:
            The token if found, or None if not found.
        """
        return TokenModel.get_by_token(token)

    def update_token(self, token: str, expires_at: datetime) -> None:
        """
        Updates a token's expiration date.

        Args:
            token (str): The token.
            expires_at (datetime): The new expiration date.
        """
        TokenModel.update_by_token(token, expires_at)

    def delete_token(self, token: str) -> None:
        """
        Deletes a token by its value.

        Args:
            token (str): The token.
        """
        instance = TokenModel.delete_by_token(token)

        if instance is not None:
            return Exception("Token not deleted")

    def create_tokens(self, user_id) -> tuple[str, str]:
        """
        Create access and refresh tokens for the given user ID.

        Parameters:
            user_id (str): The ID of the user.

        Returns:
            tuple: A tuple containing the access token and refresh token.
        """
        access_token: TokenModel = TokenModel.create_token(
            user_id, self.access_token.token_id, self.access_token.token, datetime.datetime.now() + datetime.timedelta(day=1))
        refresh_token: TokenModel = TokenModel.create_token(
            user_id, self.access_token.token_id, self.access_token.token, datetime.datetime.now() + datetime.timedelta(day=30))
        return access_token, refresh_token

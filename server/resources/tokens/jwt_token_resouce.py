import datetime
from server.models.token_type_model import TokenTypeModel
from server.models.token_model import TokenModel
from flask_jwt_extended import create_access_token, create_refresh_token
from .time_unit import TimeUnit


class JwtTokenResouce:
    """
    Resource class for managing JWT tokens.
    """

    def create_token(self, user_id: int, token_type: str) -> TokenModel:
        if token_type == 'access':
            expires_at = self.create_expiration_date(amount=1)
            token = self.create_access_token(user_id, expires_at=expires_at)
        elif token_type == 'refresh':
            expires_at = self.create_expiration_date(amount=30)
            token = self.create_refresh_token(user_id, expires_at)
        else:
            raise ValueError("Invalid token type")

        return self._create_and_save_token(user_id, token, expires_at)

    def _create_and_save_token(self, user_id: int, token: str, token_type: str, expires_at: datetime) -> TokenModel:
        """
        Creates and saves a token in the database.

        Args:
            user_id (int): The ID of the user associated with the token.
            token (str): The token value.
            expires_at (datetime): The expiration date of the token.

        Returns:
            TokenModel: The created token model object.
        """
        token_type: TokenTypeModel = TokenTypeModel.get_by_type(token_type)
        return TokenModel.create(
            user_id=user_id, token_type_id=token_type.id, token=token, expires_at=expires_at)

    def save_token(self, user_id: int, token: str) -> TokenModel:
        """
        Saves a token in the database.

        Args:
            user_id (int): The ID of the user associated with the token.
            token (str): The token value.

        Returns:
            TokenModel: The saved token model object.
        """
        expires_at: datetime.timedelta = self.create_expiration_date()
        return self._create_and_save_token(user_id, token, expires_at)

    def _get_token(self, token: str) -> TokenModel:
        """
        Retrieves a token from the database.

        Args:
            token (str): The token value.

        Returns:
            TokenModel: The retrieved token model object.
        """
        return TokenModel.get_by_token(token)

    def update_token(self, token: str, expires_at: datetime) -> None:
        """
        Updates the expiration date of a token in the database.

        Args:
            token (str): The token value.
            expires_at (datetime): The new expiration date of the token.
        """
        TokenModel.update_by_token(token, expires_at)

    def create_access_token(self, access_token: str, expires_at: datetime.timedelta) -> str:
        """
        Creates an access token with a given expiration date.

        Args:
            access_token (str): The access token value.
            expires_at (datetime.timedelta): The expiration duration of the access token.

        Returns:
            str: The created access token.
        """
        access_token = create_access_token(
            access_token, expires_delta=expires_at)
        return access_token

    def create_refresh_token(self, refresh_token: str, expires_at: datetime.timedelta) -> tuple[str, str]:
        """
        Creates a new refresh token with a given expiration date.

        Args:
            refresh_token (str): The refresh token value.
            expires_at (datetime.timedelta): The expiration duration of the refresh token.

        Returns:
            tuple[str, str]: The created refresh token.
        """
        refresh_token = create_refresh_token(
            refresh_token, expires_delta=expires_at)
        return refresh_token

    def create_expiration_date(self, time_unit: TimeUnit = TimeUnit.DAYS, amount: int = 1) -> datetime.timedelta:
        """
        Creates an expiration date based on the given time unit and amount.

        Args:
            time_unit (TimeUnit): The unit of time to use for expiration (default is TimeUnit.DAYS).
            amount (int): The amount of time units to add to the current date (default is 1).

        Returns:
            datetime.timedelta: The expiration date as a timedelta object.

        Raises:
            ValueError: If an invalid time_unit is provided.
        """
        if time_unit == TimeUnit.DAYS:
            date = datetime.datetime.now() + datetime.timedelta(days=amount)
        elif time_unit == TimeUnit.HOURS:
            date = datetime.datetime.now() + datetime.timedelta(hours=amount)
        elif time_unit == TimeUnit.MINUTES:
            date = datetime.datetime.now() + datetime.timedelta(minutes=amount)
        else:
            raise ValueError(f"Invalid time_unit: {time_unit}")
        return date

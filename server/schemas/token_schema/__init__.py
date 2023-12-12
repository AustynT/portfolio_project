from .requests.create_token_schema import CreateTokenSchema as CreateTokenRequestSchema
from .requests.read_token_schema import ReadTokenSchema as ReadTokenRequestSchema
from .requests.update_token_schema import UpdateTokenSchema as UpdateTokenRequestSchema
from .requests.delete_token_schema import DeleteTokenSchema as DeleteTokenRequestSchema

from .responses.create_token_schema import CreateTokenSchema as CreateTokenResponseSchema
from .responses.read_token_schema import ReadTokenSchema as ReadTokensResponseSchema
from .responses.update_token_schema import UpdateTokenSchema as UpdateTokenResponseSchema
from .responses.delete_token_schema import DeleteTokenSchema as DeleteTokensResponseSchema


class TokenSchema:
    """
    Schema class for validating token requests and responses.
    """

    def get_request_schemas(self):
        """
        Get all request schemas.

        Returns:
            dict: A dictionary containing all request schemas.
        """
        return {
            'create': CreateTokenRequestSchema(),
            'read': ReadTokenRequestSchema(),
            'update': UpdateTokenRequestSchema(),
            'delete': DeleteTokenRequestSchema()
        }

    def get_response_schemas(self):
        """
        Get all response schemas.

        Returns:
            dict: A dictionary containing all response schemas.
        """
        return {
            'create': CreateTokenResponseSchema(),
            'read': ReadTokensResponseSchema(),
            'update': UpdateTokenResponseSchema(),
            'delete': DeleteTokensResponseSchema()
        }

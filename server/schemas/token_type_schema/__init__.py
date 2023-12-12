from .requests.create_token_type_schema import CreateTokenTypeSchema as CreateTokenTypeRequestSchema
from .requests.read_token_type_schema import ReadTokenTypeSchema as ReadTokenTypeRequestSchema
from .requests.update_token_type_schema import UpdateTokenTypeSchema as UpdateTokenTypeRequestSchema
from .requests.delete_token_type_schema import DeleteTokenTypeSchema as DeleteTokenTypeRequestSchema

from .responses.create_token_type_schema import CreateTokenTypeSchema as CreateTokenTypeResponseSchema
from .responses.read_token_type_schema import ReadTokenTypeSchema as ReadTokenTypesResponseSchema
from .responses.update_token_type_schema import UpdateTokenTypeSchema as UpdateTokenTypeResponseSchema
from .responses.delete_token_type_schema import DeleteTokenTypeSchema as DeleteTokenTypesResponseSchema


class TokenTypeSchema:
    """
    Schema class for validating token type requests and responses.
    """

    def get_request_schemas(self):
        """
        Get all request schemas.

        Returns:
            dict: A dictionary containing all request schemas.
        """
        return {
            'create': CreateTokenTypeRequestSchema(),
            'read': ReadTokenTypeRequestSchema(),
            'update': UpdateTokenTypeRequestSchema(),
            'delete': DeleteTokenTypeRequestSchema()
        }

    def get_response_schemas(self):
        """
        Get all response schemas.

        Returns:
            dict: A dictionary containing all response schemas.
        """
        return {
            'create': CreateTokenTypeResponseSchema(),
            'read': ReadTokenTypesResponseSchema(),
            'update': UpdateTokenTypeResponseSchema(),
            'delete': DeleteTokenTypesResponseSchema()
        }

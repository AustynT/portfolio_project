from .requests.create_user_info_schema import CreateUserInfoSchema as CreateUserInfoRequestSchema
from .requests.read_user_info_schema import ReadUserInfoSchema as ReadUserInfoRequestSchema
from .requests.update_user_info_schema import UpdateUserInfoSchema as UpdateUserInfoRequestSchema
from .requests.delete_user_info_schema import DeleteUserInfoSchema as DeleteUserInfoRequestSchema

from .responses.create_user_info_schema import CreateUserInfoSchema as CreateUserInfoResponseSchema
from .responses.read_user_info_schema import ReadUserInfoSchema as ReadUserInfosResponseSchema
from .responses.update_user_info_schema import UpdateUserInfoSchema as UpdateUserInfoResponseSchema


class UserInfoSchema:
    """
    Schema class for validating user_info requests and responses.
    """

    def get_request_schemas(self):
        """
        Get all request schemas.

        Returns:
            dict: A dictionary containing all request schemas.
        """
        return {
            'create': CreateUserInfoRequestSchema(),
            'read': ReadUserInfoRequestSchema(),
            'update': UpdateUserInfoRequestSchema(),
            'delete': DeleteUserInfoRequestSchema()
        }

    def get_response_schemas(self):
        """
        Get all response schemas.

        Returns:
            dict: A dictionary containing all response schemas.
        """
        return {
            'create': CreateUserInfoResponseSchema(),
            'read': ReadUserInfosResponseSchema(),
            'update': UpdateUserInfoResponseSchema()
        }

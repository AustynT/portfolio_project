from .requests.read_user_schema import ReadUserSchema as ReadUserSchemaRequest
from .requests.create_user_schema import CreateUserSchema as CreateUserSchemaRequest
from .requests.update_user_schema import UpdateUserSchema as UpdateUserSchemaRequest
from .requests.delete_user_schema import DeleteUserSchema as DeleteUserSchemaRequest

from .responses.read_user_schema import ReadUserSchema as ReadUserSchemaResponse
from .responses.create_user_schema import CreateUserSchema as CreateUserSchemaResponse
from .responses.update_user_schema import UpdateUserSchema as UpdateUserSchemaResponse


class UserSchema:
    """
    Class for validating user data.

    Attributes:
        read_user_schema_request (ReadUserSchemaRequest): The schema for validating read user data.
        create_user_schema_request (CreateUserSchemaRequest): The schema for validating create user data.
        update_user_schema_request (UpdateUserSchemaRequest): The schema for validating update user data.
        delete_user_schema_request (DeleteUserSchemaRequest): The schema for validating delete user data.
        read_user_schema_response (ReadUserSchemaResponse): The schema for validating read user data.
        create_user_schema_response (CreateUserSchemaResponse): The schema for validating create user data.
        update_user_schema_response (UpdateUserSchemaResponse): The schema for validating update user data.
    """
    read_user_schema_request = ReadUserSchemaRequest()
    create_user_schema_request = CreateUserSchemaRequest()
    update_user_schema_request = UpdateUserSchemaRequest()
    delete_user_schema_request = DeleteUserSchemaRequest()
    create_user_schema_response = CreateUserSchemaResponse()
    read_user_schema_response = ReadUserSchemaResponse()
    update_user_schema_response = UpdateUserSchemaResponse()
    create_user_schema_response = CreateUserSchemaResponse()

    def get_request_schemas(self):
        """
        Return the request schemas.

        Returns:
            dict: The request schemas.
        """
        return {
            "read": self.read_user_schema_request,
            "create": self.create_user_schema_request,
            "update": self.update_user_schema_request,
            "delete": self.delete_user_schema_request
        }

    def get_response_schemas(self):
        """
        Return the response schemas.

        Returns:
            dict: The response schemas.
        """
        return {
            "read": self.read_user_schema_response,
            "create": self.create_user_schema_response,
            "update": self.update_user_schema_response
        }

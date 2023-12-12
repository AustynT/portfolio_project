from .requests.create_user_skill_schema import CreateUserSkillSchema as CreateUserSkillRequestSchema
from .requests.read_user_skill_schema import ReadUserSkillSchema as ReadUserSkillRequestSchema
from .requests.update_user_skill_schema import UpdateUserSkillSchema as UpdateUserSkillRequestSchema
from .requests.delete_user_skill_schema import DeleteUserSkillSchema as DeleteUserSkillRequestSchema

from .responses.create_user_skill_schema import CreateUserSkillSchema as CreateUserSkillResponseSchema
from .responses.read_user_skill_schema import ReadUserSkillSchema as ReadUserSkillsResponseSchema
from .responses.update_user_skill_schema import UpdateUserSkillSchema as UpdateUserSkillResponseSchema
from .responses.delete_user_skill_schema import DeleteUserSkillSchema as DeleteUserSkillsResponseSchema


class UserSkillSchema:
    """
    Schema class for validating User_skill requests and responses.
    """

    def get_request_schemas(self):
        """
        Get all request schemas.

        Returns:
            dict: A dictionary containing all request schemas.
        """
        return {
            'create': CreateUserSkillRequestSchema(),
            'read': ReadUserSkillRequestSchema(),
            'update': UpdateUserSkillRequestSchema(),
            'delete': DeleteUserSkillRequestSchema()
        }

    def get_response_schemas(self):
        """
        Get all response schemas.

        Returns:
            dict: A dictionary containing all response schemas.
        """
        return {
            'create': CreateUserSkillResponseSchema(),
            'read': ReadUserSkillsResponseSchema(),
            'update': UpdateUserSkillResponseSchema(),
            'delete': DeleteUserSkillsResponseSchema()
        }

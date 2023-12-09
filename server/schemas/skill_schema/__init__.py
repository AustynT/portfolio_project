from .requests.create_skill_schema import CreateSkillSchema as CreateSkillRequestSchema
from .requests.read_skill_schema import ReadSkillSchema as ReadSkillRequestSchema
from .requests.update_skill_schema import UpdateSkillSchema as UpdateSkillRequestSchema
from .requests.delete_skill_schema import DeleteSkillSchema as DeleteSkillRequestSchema

from .responses.create_skill_schema import CreateSkillSchema as CreateSkillResponseSchema
from .responses.read_skill_schema import ReadSkillSchema as ReadSkillsResponseSchema
from .responses.update_skill_schema import UpdateSkillSchema as UpdateSkillResponseSchema
from .responses.delete_skill_schema import DeleteSkillSchema as DeleteSkillsResponseSchema


class SkillSchema:
    """
    Schema class for validating skill requests and responses.
    """

    def get_request_schemas(self):
        """
        Get all request schemas.

        Returns:
            dict: A dictionary containing all request schemas.
        """
        return {
            'create': CreateSkillRequestSchema(),
            'read': ReadSkillRequestSchema(),
            'update': UpdateSkillRequestSchema(),
            'delete': DeleteSkillRequestSchema()
        }

    def get_response_schemas(self):
        """
        Get all response schemas.

        Returns:
            dict: A dictionary containing all response schemas.
        """
        return {
            'create': CreateSkillResponseSchema(),
            'read': ReadSkillsResponseSchema(),
            'update': UpdateSkillResponseSchema(),
            'delete': DeleteSkillsResponseSchema()
        }

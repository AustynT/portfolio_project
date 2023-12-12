from .requests.create_hobby_skill_schema import CreateHobbySkillSchema as CreateHobbySkillRequestSchema
from .requests.read_hobby_skill_schema import ReadHobbySkillSchema as ReadHobbySkillRequestSchema
from .requests.update_hobby_skill_schema import UpdateHobbySkillSchema as UpdateHobbySkillRequestSchema
from .requests.delete_hobby_skill_schema import DeleteHobbySkillSchema as DeleteHobbySkillRequestSchema

from .responses.create_hobby_skill_schema import CreateHobbySkillSchema as CreateHobbySkillResponseSchema
from .responses.read_hobby_skill_schema import ReadHobbySkillSchema as ReadHobbySkillsResponseSchema
from .responses.update_hobby_skill_schema import UpdateHobbySkillSchema as UpdateHobbySkillResponseSchema
from .responses.delete_hobby_skill_schema import DeleteHobbySkillSchema as DeleteHobbySkillsResponseSchema


class HobbySkillSchema:
    """
    Schema class for validating hobby_skill requests and responses.
    """

    def get_request_schemas(self):
        """
        Get all request schemas.

        Returns:
            dict: A dictionary containing all request schemas.
        """
        return {
            'create': CreateHobbySkillRequestSchema(),
            'read': ReadHobbySkillRequestSchema(),
            'update': UpdateHobbySkillRequestSchema(),
            'delete': DeleteHobbySkillRequestSchema()
        }

    def get_response_schemas(self):
        """
        Get all response schemas.

        Returns:
            dict: A dictionary containing all response schemas.
        """
        return {
            'create': CreateHobbySkillResponseSchema(),
            'read': ReadHobbySkillsResponseSchema(),
            'update': UpdateHobbySkillResponseSchema(),
            'delete': DeleteHobbySkillsResponseSchema()
        }

from .requests.create_project_skill_schema import CreateProjectSkillSchema as CreateProjectSkillRequestSchema
from .requests.read_project_skill_schema import ReadProjectSkillSchema as ReadProjectSkillRequestSchema
from .requests.update_project_skill_schema import UpdateProjectSkillSchema as UpdateProjectSkillRequestSchema
from .requests.delete_project_skill_schema import DeleteProjectSkillSchema as DeleteProjectSkillRequestSchema

from .responses.create_project_skill_schema import CreateProjectSkillSchema as CreateProjectSkillResponseSchema
from .responses.read_project_skill_schema import ReadProjectSkillSchema as ReadProjectSkillsResponseSchema
from .responses.update_project_skill_schema import UpdateProjectSkillSchema as UpdateProjectSkillResponseSchema
from .responses.delete_project_skill_schema import DeleteProjectSkillSchema as DeleteProjectSkillsResponseSchema


class ProjectSkillSchema:
    """
    Schema class for validating project_skill requests and responses.
    """

    def get_request_schemas(self):
        """
        Get all request schemas.

        Returns:
            dict: A dictionary containing all request schemas.
        """
        return {
            'create': CreateProjectSkillRequestSchema(),
            'read': ReadProjectSkillRequestSchema(),
            'update': UpdateProjectSkillRequestSchema(),
            'delete': DeleteProjectSkillRequestSchema()
        }

    def get_response_schemas(self):
        """
        Get all response schemas.

        Returns:
            dict: A dictionary containing all response schemas.
        """
        return {
            'create': CreateProjectSkillResponseSchema(),
            'read': ReadProjectSkillsResponseSchema(),
            'update': UpdateProjectSkillResponseSchema(),
            'delete': DeleteProjectSkillsResponseSchema()
        }

from .requests.create_project_schema import CreateProjectSchema as CreateProjectRequestSchema
from .requests.read_project_schema import ReadProjectSchema as ReadProjectRequestSchema
from .requests.update_project_schema import UpdateProjectSchema as UpdateProjectRequestSchema
from .requests.delete_project_schema import DeleteProjectSchema as DeleteProjectRequestSchema

from .responses.create_project_schema import CreateProjectSchema as CreateProjectResponseSchema
from .responses.read_project_schema import ReadProjectSchema as ReadProjectsResponseSchema
from .responses.update_project_schema import UpdateProjectSchema as UpdateProjectResponseSchema
from .responses.delete_project_schema import DeleteProjectSchema as DeleteProjectsResponseSchema


class ProjectSchema:
    """
    Schema class for validating project requests and responses.
    """

    def get_request_schemas(self):
        """
        Get all request schemas.

        Returns:
            dict: A dictionary containing all request schemas.
        """
        return {
            'create': CreateProjectRequestSchema(),
            'read': ReadProjectRequestSchema(),
            'update': UpdateProjectRequestSchema(),
            'delete': DeleteProjectRequestSchema()
        }

    def get_response_schemas(self):
        """
        Get all response schemas.

        Returns:
            dict: A dictionary containing all response schemas.
        """
        return {
            'create': CreateProjectResponseSchema(),
            'read': ReadProjectsResponseSchema(),
            'update': UpdateProjectResponseSchema(),
            'delete': DeleteProjectsResponseSchema()
        }

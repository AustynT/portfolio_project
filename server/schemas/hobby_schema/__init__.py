from .requests.create_hobby_schema import CreateHobbySchema as CreateHobbyRequestSchema
from .requests.read_hobby_schema import ReadHobbySchema as ReadHobbyRequestSchema
from .requests.update_hobby_schema import UpdateHobbySchema as UpdateHobbyRequestSchema
from .requests.delete_hobby_schema import DeleteHobbySchema as DeleteHobbyRequestSchema

from .responses.create_hobby_schema import CreateHobbySchema as CreateHobbyResponseSchema
from .responses.read_hobby_schema import ReadHobbySchema as ReadHobbiesResponseSchema
from .responses.update_hobby_schema import UpdateHobbySchema as UpdateHobbyResponseSchema
from .responses.delete_hobby_schema import DeleteHobbySchema as DeleteHobbiesResponseSchema


class HobbySchema:
    """
    Schema class for validating hobby requests and responses.
    """

    def get_request_schemas(self):
        """
        Get all request schemas.

        Returns:
            dict: A dictionary containing all request schemas.
        """
        return {
            'create': CreateHobbyRequestSchema(),
            'read': ReadHobbyRequestSchema(),
            'update': UpdateHobbyRequestSchema(),
            'delete': DeleteHobbyRequestSchema()
        }

    def get_response_schemas(self):
        """
        Get all response schemas.

        Returns:
            dict: A dictionary containing all response schemas.
        """
        return {
            'create': CreateHobbyResponseSchema(),
            'read': ReadHobbiesResponseSchema(),
            'update': UpdateHobbyResponseSchema(),
            'delete': DeleteHobbiesResponseSchema()
        }

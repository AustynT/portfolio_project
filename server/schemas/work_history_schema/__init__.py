from .requests.create_work_history_schema import CreateWorkHistorySchema as CreateWorkHistoryRequestSchema
from .requests.read_work_history_schema import ReadWorkHistorySchema as ReadWorkHistoryRequestSchema
from .requests.update_work_history_schema import UpdateWorkHistorySchema as UpdateWorkHistoryRequestSchema
from .requests.delete_work_history_schema import DeleteWorkHistorySchema as DeleteWorkHistoryRequestSchema

from .responses.create_work_history_schema import CreateWorkHistorySchema as CreateWorkHistoryResponseSchema
from .responses.read_work_history_schema import ReadWorkHistorySchema as ReadWorkHistoriesResponseSchema
from .responses.update_work_history_schema import UpdateWorkHistorySchema as UpdateWorkHistoryResponseSchema
from .responses.delete_work_history_schema import DeleteWorkHistorySchema as DeleteWorkHistoriesResponseSchema


class WorkHistorySchema:
    """
    Schema class for validating work_history requests and responses.
    """

    def get_request_schemas(self):
        """
        Get all request schemas.

        Returns:
            dict: A dictionary containing all request schemas.
        """
        return {
            'create': CreateWorkHistoryRequestSchema(),
            'read': ReadWorkHistoryRequestSchema(),
            'update': UpdateWorkHistoryRequestSchema(),
            'delete': DeleteWorkHistoryRequestSchema()
        }

    def get_response_schemas(self):
        """
        Get all response schemas.

        Returns:
            dict: A dictionary containing all response schemas.
        """
        return {
            'create': CreateWorkHistoryResponseSchema(),
            'read': ReadWorkHistoriesResponseSchema(),
            'update': UpdateWorkHistoryResponseSchema(),
            'delete': DeleteWorkHistoriesResponseSchema()
        }

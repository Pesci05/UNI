import logging
import uuid

logger = logging.getLogger(__name__)


class ResourceUtils:

    @staticmethod
    def internal_server_error(operation: str) -> tuple[dict[str, str], int]:
        error_id = uuid.uuid4().hex
        logger.exception("Internal Server Error [errorId: %s] while %s", error_id, operation)
        return {'error': "Internal Server Error ! An unexpected error occurred while " + operation,
                'errorId': error_id}, 500
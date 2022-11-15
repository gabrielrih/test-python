from resources.atlas.exception.default_exception import DefaultException

DETAIL_PREFIX='Mongo Exception: '

class MongoException(DefaultException):

    def __init__(self,
                 success: bool = False,
                 detail: str = None):

        super().__init__(detail=DETAIL_PREFIX + detail, success=success)

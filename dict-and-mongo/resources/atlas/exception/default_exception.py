from typing import Any, Dict, Optional, Union


class DefaultException(Exception):

    def __init__(self,
                 success: bool = False,
                 detail: str = None):
        self.detail = detail
        self.success = success

    def content(self) -> Dict[str, Union[Optional[bool], Any]]:
        return {'success': self.success, 'detail': self.detail}

    def __str__(self) -> str:
        return self.content()

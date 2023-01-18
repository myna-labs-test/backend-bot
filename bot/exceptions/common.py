from typing import Union


class CommonException(Exception):
    def __init__(self, message: str, error: Union[Exception,None]) -> None:
        super().__init__()
        self.error = error
        self.message = message

    def __str__(self):
        return self.message


class InternalServerError(CommonException):
    def __init__(self, message: str, error: Exception) -> None:
        super().__init__(message, error)

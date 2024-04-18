import typing as t
from apiflask import HTTPError
from apiflask.types import ResponseHeaderType
# from utils.constants import Constants


class CustomError(Exception):

    def __init__(self, message) -> None:
        self.message = message
        self.codes =  500
        super().__init__({"message": self.message, "codes": self.codes})

class BusinessValidationError(Exception):

    def __init__(self, message) -> None:
        self.message = message
        self.codes =  400 #Constants.httpConstants("BAD_REQUEST")
        super().__init__({"message": self.message, "codes": self.codes})


class NotFoundError(Exception):

    def __init__(self, message) -> None:
        self.message = message
        self.codes =  404
        super().__init__({"message": self.message, "codes": self.codes})
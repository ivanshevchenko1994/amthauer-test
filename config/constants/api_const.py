import os
from enum import Enum
from typing import Final


class ErrorKeys(Enum):
    MESSAGE = 'detail'


class HttpStatus(Enum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    SERVICE_UNAVAILABLE = 503


class ErrorResponse(Enum):
    INVALID_CREDENTIALS = 'Invalid credentials'
    INVALID_EMAIL = 'Invalid email'
    INVALID_PASSWORD = 'Invalid password'
    INVALID_ACCESS_TOKEN = 'Invalid access token'
    INVALID_REFRESH_TOKEN = 'Invalid refresh token'
    CREATE_NEW_DB_ENTRY_ERROR = 'Can not create new DB entry'
    SHOW_ALL_DB_ENTRY_ERROR = 'Can not show all entries'
    NOT_EXISTING_DB_ENTRY_ERROR = 'Entry dose not exist'
    SHOW_ONE_DB_ENTRY_ERROR = 'Can not show entry'
    DELETE_DB_ENTRY_ERROR = 'Can not delete entry'


class SuccessResponse(Enum):
    DELETE_ENTRY_SUCCESS = 'Entry was deleted successfully'


JWT_ALGORITHM: Final[str] = os.getenv('HS256', default='HS256')
TOKEN_TYPE: Final[str] = os.getenv('TOKEN_TYPE', default='Bearer')

ACCESS_TOKEN_LIFETIME_MINUTES: Final[int] = int(os.getenv('ACCESS_TOKEN_LIFETIME_MINUTES', default=50))
ACCESS_TOKEN_SUB: Final[str] = os.getenv('ACCESS_TOKEN_SUB', default='access')

REFRESH_TOKEN_LIFETIME_DAYS: Final[int] = int(os.getenv('REFRESH_TOKEN_LIFETIME_DAYS', default=10))
REFRESH_TOKEN_SUB: Final[str] = os.getenv('REFRESH_TOKEN_SUB', default='refresh')

API_VERSION_1: Final[str] = "1"

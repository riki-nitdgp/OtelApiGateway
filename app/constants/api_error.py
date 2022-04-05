from enum import Enum


class ApiError(Enum):
    REQUIRED_PARAMETERS = "{} is required."
    AUTH_TOKEN_MISSING = "Authorization Token is required"

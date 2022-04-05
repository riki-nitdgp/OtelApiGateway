from app.exception import BadRequestException
from app.constants import ApiError
import re


class DataValidator:

    @classmethod
    def validate_mandatory_params(cls, **kwargs):
        for key, value in kwargs.items():
            if value is None:
                raise BadRequestException(ApiError.REQUIRED_PARAMETERS.value.format(key))


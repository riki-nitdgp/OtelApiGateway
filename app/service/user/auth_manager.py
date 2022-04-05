from functools import wraps
from fastapi import Request
from app.constants import ApiError
from app.exception import UnAuthorizedException
from .user_manager import UserManager
from .user_info import User


class AuthenticationManager:

    @classmethod
    def authenticate_user(cls, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            auth_token = cls.get_auth_token_from_headers(kwargs.get("_request"))
            if not auth_token:
                raise UnAuthorizedException(ApiError.AUTH_TOKEN_MISSING.value)
            user = await UserManager.authenticate(auth_token)
            user_info = await cls.build_user_info(user)
            cls.set_global_user_hearers(kwargs.get("_request"), user_info)
            result = await func(*args, **kwargs)
            return result

        return wrapper

    @classmethod
    def get_auth_token_from_headers(cls, request: Request):
        return request.headers.get("x-authorization-token")

    @classmethod
    def set_global_user_hearers(cls, request: Request, user_headers: dict):

        request.headers.__dict__.update({"user_context": user_headers})

    @classmethod
    async def build_user_info(cls, user: dict):
        user_info = User.user_info(user)
        return user_info.__dict__

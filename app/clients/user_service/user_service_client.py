from app.config import AppConfig
from app.utils import BaseAPIClientRequestHandler
import json
config = AppConfig.config


class UserServiceClient(BaseAPIClientRequestHandler):
    _host = config["USER_SERVICE"]["HOST"]

    @classmethod
    async def login(cls, payload: dict):
        path = '/api/user/login'
        result = await cls.post(path, data=payload)
        return result

    @classmethod
    async def signup(cls, payload):
        path = '/api/user/sign-up'
        result = await cls.post(path, data=payload)
        return result

    @classmethod
    async def authenticate(cls, auth_token: str):
        path = '/api/v1/authenticate'
        headers = {"x-authorization-token": auth_token}
        result = await cls.post(path, data={}, headers=headers)
        return result.data

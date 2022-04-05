from app.clients import UserServiceClient
from fastapi import Request

class UserManager:

    @classmethod
    async def login(cls, payload: dict):
        return await UserServiceClient.login(payload)

    @classmethod
    async def signup(cls, payload: dict):
        return await UserServiceClient.signup(payload)

    @classmethod
    async def authenticate(cls, auth_token: str):
        return await UserServiceClient.authenticate(auth_token)

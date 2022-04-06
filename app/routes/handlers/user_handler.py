from fastapi import APIRouter, Request
from app.utils import HttpResponseBuilder
from app.config import AppConfig
from app.service import UserManager

routes = APIRouter()
config = AppConfig.config


@routes.post("/login")
async def login(_request: Request):
    payload = await _request.json()
    result = await UserManager.login(payload)
    return await HttpResponseBuilder.build_success_response(result.__dict__())


@routes.post("/signup")
async def signup(_request: Request):
    payload = await _request.json()
    result = await UserManager.signup(payload)
    return await HttpResponseBuilder.build_success_response(result.__dict__())

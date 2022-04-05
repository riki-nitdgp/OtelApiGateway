import asyncio
import json

from fastapi import status
from aiohttp import ClientSession
from app.exception import InternalServerError, ApiGatewayException
from .gateway_response_builder import BuildResponse

SESSION = None


class BaseAPIClientRequestHandler:
    _host = ''
    _timeout = 10

    @classmethod
    async def get_http_session(cls):
        global SESSION
        if SESSION is None:
            SESSION = ClientSession()
        return SESSION

    @classmethod
    async def get(cls, path: str, data: dict = None, params: dict = None, timeout=None, headers=None):
        result = await cls.http_request("GET", path, data=data, params=params,
                                        timeout=timeout, headers=headers)
        return result

    @classmethod
    async def post(cls, path: str, data: dict = None, params: dict = None, timeout: int = None, headers: dict = None):
        result = await cls.http_request("POST", path, data=data, params=params,
                                        timeout=timeout, headers=headers)
        return result

    @classmethod
    async def http_request(cls, method: str, path: str, data: dict = None, params: dict = None, timeout: int =None,
                           headers: dict = None):
        url = cls._host + path
        if not timeout:
            timeout = cls._timeout

        common_headers = cls.build_common_headers()
        if not headers:
            headers = common_headers
        else:
            headers = {**common_headers, **headers}

        if data:
            data = json.dumps(data)

        session = await cls.get_http_session()

        try:
            response = await session.request(method, str(url), data=data, headers=headers, params=params, timeout=timeout)

            payload = await response.json()

        except asyncio.TimeoutError as e:
            exception_message = 'Inter service timeout'
            raise InternalServerError(error=exception_message, status_code=status.HTTP_504_GATEWAY_TIMEOUT)
        except Exception as e:
            exception_message = str(e)

            raise InternalServerError(error=exception_message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response_data = cls.parse_http_response(payload, response.status)
        return response_data

    @classmethod
    def parse_http_response(cls, payload: dict, http_status: int) -> BuildResponse:

        if payload.get("success"):
            result = BuildResponse(payload["data"], meta=payload.get("meta", None),
                                   http_status_code=http_status, page_info=payload.get("page_info"))

            return result
        else:
            message = payload.get("message")
            raise ApiGatewayException(error=message, status_code=http_status)

    @classmethod
    def build_common_headers(cls):
        return {"Content-Type": "application/json"}

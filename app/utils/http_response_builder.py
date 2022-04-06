from fastapi.responses import JSONResponse
from fastapi import status


class HttpResponseBuilder:

    @classmethod
    async def build_success_response(cls, data: dict):
        meta = data.pop("meta", None)
        page_info = data.pop("page_info", None)
        response = {
            'data': data.get("data"),
            'success': True,
            'status': status.HTTP_200_OK
        }
        if meta:
            response['meta'] = meta
        if page_info:
            response["page_info"] = page_info
        return JSONResponse(response)

    @classmethod
    async def build_error_response(cls, message, status_code=400):
        response = {
            "error": [message],
            "message":  message,
            "success": False,
            "status": status_code,
        }
        return JSONResponse(response, status_code=status_code)

from fastapi import APIRouter, Request
from app.utils import HttpResponseBuilder
from app.service import ProductManager
from app.service.user import authenticate
from app.config import AppConfig

routes = APIRouter()
config = AppConfig.config


@routes.get("/by-id/{product_id}")
@authenticate
async def product_by_id(_request: Request, product_id: str):
    product_details = await ProductManager.product_by_id(product_id)
    return await HttpResponseBuilder.build_success_response(product_details.__dict__())


@routes.get("/all")
@authenticate
async def all_products(_request: Request):
    query_params = _request.query_params
    params = {"pageNo": query_params.get("pageNo"), "pageSize": query_params.get("pageSize")}
    all_products = await ProductManager.all_products(params)
    return await HttpResponseBuilder.build_success_response(all_products.__dict__())


@routes.get("/add-new")
@authenticate
async def create_product(_request: Request):
    payload = await _request.json()
    result = await ProductManager.create_product(payload)
    return await HttpResponseBuilder.build_success_response(result.__dict__())

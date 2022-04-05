from fastapi import APIRouter, Request
from app.utils import HttpResponseBuilder
from app.config import AppConfig
from app.service.user import authenticate
from app.service import RatingAndReviewManager

routes = APIRouter()
config = AppConfig.config


@routes.post("/rate-review-product")
@authenticate
async def rate_and_review_products(_request: Request):
    payload = await _request.json()
    result = await RatingAndReviewManager.rate_review_products(payload, _request)
    return await HttpResponseBuilder.build_success_response(result.__dict__())


@routes.get("/reviewed-product")
@authenticate
async def user_reviewed_product(_request: Request):
    result = await RatingAndReviewManager.user_reviewed_products(_request)
    return await HttpResponseBuilder.build_success_response(result.__dict__())

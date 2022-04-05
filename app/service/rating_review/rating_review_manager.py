from fastapi import Request
from app.clients import RatingReviewServiceClient

class RatingAndReviewManager:

    @classmethod
    async def rate_review_products(cls, payload: dict, _request: Request):
        user_context = _request.headers.user_context
        payload["userId"] = user_context.get("username")
        return await RatingReviewServiceClient.rate_and_review_products(payload)

    @classmethod
    async def user_reviewed_products(cls, _request: Request):
        user_context = _request.headers.user_context
        username = user_context.get("username")
        return await RatingReviewServiceClient.user_reviewed_products(username)



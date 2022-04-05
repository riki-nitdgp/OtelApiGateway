from app.config import AppConfig
from app.utils import BaseAPIClientRequestHandler

config = AppConfig.config


class RatingReviewServiceClient(BaseAPIClientRequestHandler):
    _host = config["RATING_REVIEW_SERVICE"]["HOST"]

    @classmethod
    async def rate_and_review_products(cls, payload):
        path = "/api/v1/rating-review"
        result = await cls.post(path, data=payload)
        return result

    @classmethod
    async def user_reviewed_products(cls, username: str):
        path = "/api/v1/rating-review/{username}".format(username=username)
        result = await cls.get(path)
        return result

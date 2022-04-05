from fastapi import APIRouter
from app.routes.handlers import (
    health,
    user_handler,
    rating_review_handler,
    product_handler
)

router = APIRouter()

router.include_router(health.routes, tags=["health-check"], prefix='/health')
router.include_router(user_handler.routes, tags=["user"], prefix='/user')
router.include_router(rating_review_handler.routes, tags=["rating-review"], prefix="/rating-review")
router.include_router(product_handler.routes, tags=["rating-review"], prefix="/product")
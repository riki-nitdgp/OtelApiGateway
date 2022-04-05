from app.config import AppConfig
from app.utils import BaseAPIClientRequestHandler

config = AppConfig.config


class InventoryServiceClient(BaseAPIClientRequestHandler):
    _host = config["INVENTORY_SERVICE"]["HOST"]

    @classmethod
    async def add_new_products(cls, payload):
        path = '/api/v1/product'
        result = await cls.post(path, data=payload)
        return result

    @classmethod
    async def all_products(cls, params: dict):
        path = '/api/v1/products'
        result = await cls.get(path, params=params)
        return result

    @classmethod
    async def product_by_id(cls, product_id: str):
        path = '/api/v1/product/{product_id}'.format(product_id=product_id)
        result = await cls.get(path)
        return result

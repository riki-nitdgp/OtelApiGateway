from app.clients import InventoryServiceClient


class ProductManager:

    @classmethod
    async def product_by_id(cls, product_id: str):
        return await InventoryServiceClient.product_by_id(product_id)

    @classmethod
    async def all_products(cls, params: dict):
        return await InventoryServiceClient.all_products(params)

    @classmethod
    async def create_product(cls, payload: dict):
        return await InventoryServiceClient.add_new_products(payload)

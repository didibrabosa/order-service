import logging
import httpx
from models.order_model import Product


class ProductClient:
    def __init__(self, httpx_client):
        self.httpx_client = httpx_client
        self.url = "http://localhost:8001/products"
        self.logger = logging.getLogger(__name__)

    def get_product_by_name(self, name: str):
        path = f"{self.url}/name/{name}"
        try:
            response = self.httpx_client.get(path)
            product_info = response.json()
            return Product(**product_info)

        except httpx.RequestError as ex:
            self.logger.error(
                f"An error occurred while making the request: {str(ex)}")
            raise

        except httpx.HTTPStatusError as ex:
            self.logger.error(f"HTTP error occurred: {str(ex)}")
            raise

        except Exception as ex:
            self.logger.error(f"An unexpected error occurred: {str(ex)}")
            raise

import logging
import httpx
from models.order_model import Customer


class CustomerClient:
    def __init__(self):
        self.url = "http://localhost:6789/customers"
        self.logger = logging.getLogger(__name__)

    def get_customer_by_email(self, email: str):
        path = f"{self.url}/email/{email}"
        try:
            response = httpx.get(path)
            customer_info = response.json()
            return Customer(**customer_info)

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

import logging
from models.order_model import OrderRequest
from clients.customer_client import CustomerClient
from clients.product_client import ProductClient
from storage.order_storage import OrderStorage


class OrderService:
    def __init__(self, storage: OrderStorage, customer: CustomerClient, product: ProductClient):
        self.logger = logging.getLogger(__name__)
        self.storage = storage
        self.customer_client = customer
        self.product_client = product

    def create_order(self, order: OrderRequest):
        try:
            self.logger.info("Creating order for customer %s...", order.email)
            self.logger.debug(f"Order received: {order}")
            customers = self.customer_client.get_customer_by_email(order.email)
            self.logger.debug(f"Customer retrieved: {customers}")
            products = []
            for product in order.products:
                product_data = self.product_client.get_product_by_name(product.name)
                products.append(product)
                self.logger.debug(f"Product retrieved: {product_data}")
            return self.storage.create_order(order)
        except Exception as ex:
            self.logger.error(f"Error to create order: {ex}")
            raise

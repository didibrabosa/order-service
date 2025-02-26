import logging
from models.order_model import Order, OrderRequest
from clients.customer_client import CustomerClient
from clients.product_client import ProductClient
from storage.order_storage import OrderStorage


class OrderService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.storage = OrderStorage()
        self.customer_client = CustomerClient()
        self.product_client = ProductClient()

    def create_order(self, order: OrderRequest):
        try:
            self.logger.info("Creating order for customer %s...", order.email)
            self.logger.debug(f"Order received: {order}")

            customer = self.customer_client.get_customer_by_email(order.email)
            self.logger.debug(f"Customer retrieved: {customer}")

            products = []
            for product in order.products:
                products_data = self.product_client.get_product_by_name(
                    product.name)
                products.append(products_data)
                self.logger.debug(f"Product retrieved: {products_data}")

            order_model = Order(customer=customer, products=products)
            return self.storage.create_order(order_model)
        except Exception as ex:
            self.logger.error(f"Error to create order: {ex}")
            raise

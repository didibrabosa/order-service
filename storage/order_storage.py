from pymongo.errors import PyMongoError
from models.order_model import Order
import logging
from configs.db_conn import get_database


class OrderStorage:
    def __init__(self, db_connection=get_database()):
        self.db = db_connection
        self.collection = db_connection.get_collection("orders")
        self.logger = logging.getLogger(__name__)

    def create_order(self, order: Order):
        self.logger.info("Creating a order by in DataBase")
        self.logger.debug(f"Order data: {order}")
        try:
            order_created = self.collection.insert_one(order.model_dump())
            self.logger.info("Order %s inserted Sucessufuly.", order_created.inserted_id)
            return str(order_created.inserted_id)

        except PyMongoError as ex:
            self.logger.error("Failed to create a order: %s", ex)
            raise
        except ValueError as ex:
            self.logger.error("Validation error: %s", ex)
            raise

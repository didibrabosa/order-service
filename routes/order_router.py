from fastapi import APIRouter, HTTPException
from services.order_service import OrderService
from storage.order_storage import OrderStorage
from clients.customer_client import CustomerClient
from clients.product_client import ProductClient
from models.order_model import OrderRequest, OrderResponse
from configs.db_conn import get_database
import logging

router = APIRouter()
logger = logging.getLogger("__name__")

order_storage = OrderStorage(db_connection=get_database())
customer_client = CustomerClient()
product_client = ProductClient()
service = OrderService(
    storage=order_storage,
    customer=customer_client,
    product=product_client
)


@router.post("/v1/orders", response_model=OrderResponse)
def create_order(order: OrderRequest):
    logger.debug(f"Order payload: {order}")
    try:
        logger.info("Creating order %s...", order)
        created_order = service.create_order(order)
        logger.info("Order created successfully: %s", created_order)
        return (created_order)
    except ValueError as ex:
        raise HTTPException(status_code=500, detail=f"Error to create order: {ex}")
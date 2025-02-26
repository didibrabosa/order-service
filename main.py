"""
This module initializes the FastAPI application.
"""
import logging
from contextlib import asynccontextmanager
import httpx
from fastapi import FastAPI
from routes.order_router import router
from clients.customer_client import CustomerClient
from clients.product_client import ProductClient
from configs.db_conn import get_database
from services.order_service import OrderService
from storage.order_storage import OrderStorage

logger = logging.getLogger(__name__)
logging.getLogger("pymongo").setLevel(logging.WARNING)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage the application's lifespan, setting up dependencies.
    """
    db_connection = get_database()
    order_storage = OrderStorage(db_connection)
    customer_client = CustomerClient(httpx)
    product_client = ProductClient(httpx)

    order_service = OrderService(
        order_storage, customer_client, product_client
    )

    yield {"order_service": order_service}
    logger.info("Shutdown Application")


app = FastAPI(lifespan=lifespan, title="Order Service")
app.include_router(router)


@app.get("/health")
def health_check():
    """
    Health check endpoint to verify if the application is running.
    """
    return {"status": "healthy"}

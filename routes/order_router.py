"""
This module defines the routes for managing orders in the Order Service API.
"""
import logging
from typing import Annotated
import httpx
from fastapi import APIRouter, HTTPException, Depends, Request
from models.order_model import OrderRequest, OrderResponse
from services.order_service import OrderService

router = APIRouter()
logger = logging.getLogger(__name__)


def get_order_service(request: Request) -> OrderService:
    """
    Retrieve the OrderService instance from the request's state.
    """
    return request.state.order_service


ServiceDep = Annotated[OrderService, Depends(get_order_service)]


@router.post("/v1/orders", response_model=OrderResponse)
def create_order(order: OrderRequest, service: ServiceDep) -> OrderResponse:
    """
    Handle the creation of a new order.
    """
    try:
        logger.info("Starting to create an order.")
        created_order = service.create_order(order)

        logger.info("Order created successfully: %s", created_order)
        return OrderResponse(created_order)

    except httpx.HTTPStatusError as ex:
        logger.error("Error creating order: %s", ex)
        raise HTTPException(
            status_code=500, detail=f"Error creating order: {ex}"
        ) from ex

"""
This layer deals with models, specifying what each model needs and uses.
"""
from typing import List
from datetime import datetime
import ulid
from pydantic import BaseModel, EmailStr, Field


class Product(BaseModel):
    """
    Represents a product with its details.
    """
    id: str = Field(
        default_factory=lambda: str(ulid.new()), description="Product ID")
    name: str = Field(description="Product Name")
    description: str = Field(description="Product Description")
    price: float = Field(gt=0, description="Product Price")
    quantity: int = Field(description="Product Quantity")


class Customer(BaseModel):
    """
    Represents a customer and their contact details.
    """
    id: str = Field(
        default_factory=lambda: str(ulid.new()), description="Customer ID")
    name: str = Field(description="Customer Name")
    email: EmailStr = Field(description="Customer Email")


class Order(BaseModel):
    """
    Represents an order placed by a customer.
    """
    id: str = Field(
        default_factory=lambda: str(ulid.new()), description="Order ID")
    customer: Customer
    products: List[Product]
    created_at: datetime = Field(
        default_factory=datetime.now, description="Create Order Timestamp")
    updated_at: datetime | None = Field(
        default=None, description="Update Order Timestamp")


class ProductRequest(BaseModel):
    """
    Represents a request to add or update a product.
    """
    name: str = Field(description="Product Name")
    quantity: int = Field(description="Product Quantity")


class OrderRequest(BaseModel):
    """
    Represents a request to create a new order.
    """
    email: EmailStr = Field(description="Customer Email")
    products: List[ProductRequest]


class OrderResponse(BaseModel):
    """
    Represents the response for an order operation.
    """
    id: str = Field(
        default_factory=lambda: str(ulid.new()), description="Order ID")

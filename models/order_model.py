from pydantic import BaseModel, Field
import ulid
from datetime import datetime


class Product(BaseModel):
    product_id: str
    product_name: str
    description: str
    price: float
    quantity: int


class Customer(BaseModel):
    customer_id: str
    customer_name: str
    customer_email: str


class Order(BaseModel):
    order_id: str = Field(default_factory=lambda: str(ulid.new()))
    customer_email: str
    products: list
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class ProductRequest(BaseModel):
    product_name: str
    quantity: int


class OrderRequest(BaseModel):
    customer_email: str
    products: list


class OrderResponse(BaseModel):
    order_id: str = Field(default_factory=lambda: str(ulid.new()))

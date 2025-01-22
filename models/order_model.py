from pydantic import BaseModel, Field
import ulid
from typing import List
from datetime import datetime


class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    quantity: int


class Customer(BaseModel):
    id: str
    name: str
    email: str


class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(ulid.new()))
    customer: Customer
    products: List[Product]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default=None)


class ProductRequest(BaseModel):
    name: str
    quantity: int


class OrderRequest(BaseModel):
    email: str
    products: list[ProductRequest]


class OrderResponse(BaseModel):
    order_id: str = Field(default_factory=lambda: str(ulid.new()))

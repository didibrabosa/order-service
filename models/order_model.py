from pydantic import BaseModel, EmailStr, Field
import ulid
from typing import List
from datetime import datetime


class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(ulid.new()))
    name: str
    description: str
    price: float
    quantity: int


class Customer(BaseModel):
    id: str = Field(default_factory=lambda: str(ulid.new()))
    name: str
    email: EmailStr


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
    email: EmailStr
    products: List[ProductRequest]


class OrderResponse(BaseModel):
    id: str = Field(default_factory=lambda: str(ulid.new()))

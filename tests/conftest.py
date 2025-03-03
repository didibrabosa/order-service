from pytest import fixture
from models.order_model import Order, Customer, Product


@fixture
def customer():
    return Customer(
        id="01F8MECHZX3TBDSZ7XD96VR2H5",
        name="Cleiton",
        email="cleitu@savana.com.br"
    )


@fixture
def product():
    return Product(
        id="01G8MECHZX3TBDSZ7XD96VR2H5",
        name="XBOX Series SSSSS",
        description="LA PUBG",
        price=12000,
        quantity=3
    )


@fixture
def order(customer, product):
    return Order(
        id="01H8MECHZX3TBDSZ7XD96VR2H5",
        customer=customer,
        products=[product],
        created_at="2025-02-26T19:48:46.352Z",
        updated_at=None
    )

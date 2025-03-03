from unittest.mock import MagicMock
from pytest import fixture, raises
from services.order_service import OrderService
from models.order_model import OrderRequest
from storage.order_storage import OrderStorage


@fixture
def storage():
    return MagicMock(OrderStorage)


@fixture
def customer_client():
    return MagicMock()


@fixture
def product_client():
    return MagicMock()


@fixture
def service(storage, customer_client, product_client):
    return OrderService(storage, customer_client, product_client)


@fixture
def order_request():
    return OrderRequest(
        email="cleitu@savana.com.br",
        products=[{
            "id": "01G8MECHZX3TBDSZ7XD96VR2H5",
            "name": "XBOX Series SSSSS",
            "description": "LA PUBG",
            "price": 12000,
            "quantity": 3
        }]
    )


def test_create_order_success(
        service,
        storage,
        customer_client,
        product_client,
        order_request,
        customer,
        product,
        order):

    customer_client.get_customer_by_email.return_value = customer
    product_client.get_product_by_name.return_value = product
    storage.create_order.return_value = order

    result = service.create_order(order_request)

    assert result == order

    customer_client.get_customer_by_email.assert_called_once_with(
        "cleitu@savana.com.br")
    product_client.get_product_by_name.assert_called_once_with(
        "XBOX Series SSSSS")
    storage.create_order.assert_called_once()


def test_create_order_database_error(
        service,
        storage,
        customer_client,
        product_client,
        order_request,
        customer,
        product):

    storage.create_order.side_effect = Exception("Database error")
    customer_client.get_customer_by_email.return_value = customer
    product_client.get_product_by_name.return_value = product

    with raises(Exception, match="Database error"):
        service.create_order(order_request)

    storage.create_order.assert_called_once()

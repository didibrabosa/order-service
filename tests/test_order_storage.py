from unittest.mock import MagicMock
import pytest
from pymongo.errors import PyMongoError
from pytest import fixture
from storage.order_storage import OrderStorage


@fixture
def collection():
    return MagicMock()


@fixture
def db_conn(collection):
    db = MagicMock()
    db.get_collection.return_value = collection
    return db


@fixture
def storage(db_conn):
    return OrderStorage(db_conn)


def test_create_order_success(storage, order, collection):
    order_id = "01F8MECHZX3TBDSZ7XD96VR2H5"
    collection.insert_one.return_value.inserted_id = order_id

    result = storage.create_order(order)

    assert result == order_id

    collection.insert_one.assert_called_once_with(order.model_dump())


def test_create_order_pymongo_error(storage, order, collection):
    collection.insert_one.side_effect = PyMongoError()

    with pytest.raises(PyMongoError):
        storage.create_order(order)

from fastapi.testclient import TestClient
import pytest
from ..controllers import orderController as controller
from ..main import app
from ..schemas import orderSchema as schema


client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    db = mocker.Mock()

    db.query.return_value.filter.return_value.first.return_value = mocker.Mock()

    return db


def test_create_order(db_session):
    order_data = {
        "customer_id": 1,
        "status": "Pending",
        "total_price": 12.50
    }

    order_object = schema.OrderCreate(**order_data)

    created_order = controller.create_order(
        db=db_session,
        order=order_object
    )

    assert created_order is not None
    assert created_order.customer_id == 1
    assert created_order.status == "Pending"
    assert created_order.total_price == 12.50

    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once()
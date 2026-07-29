from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import customers as customerModel
from ..models import orders as orderModel
from ..schemas import orderSchema


def create_order(
    db: Session,
    order: orderSchema.OrderCreate
):
    customer = (
        db.query(customerModel.Customer)
        .filter(customerModel.Customer.customer_id == order.customer_id)
        .first()
    )

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    new_order = orderModel.Order(
        customer_id=order.customer_id,
        status=order.status,
        total_price=order.total_price
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


def get_orders(db: Session):
    return db.query(orderModel.Order).all()


def get_order(db: Session, order_id: int):
    order = (
        db.query(orderModel.Order)
        .filter(orderModel.Order.order_id == order_id)
        .first()
    )

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    return order


def update_order(
    db: Session,
    order_id: int,
    order_update: orderSchema.OrderUpdate
):
    order = get_order(db, order_id)

    customer = (
        db.query(customerModel.Customer)
        .filter(
            customerModel.Customer.customer_id
            == order_update.customer_id
        )
        .first()
    )

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    order.customer_id = order_update.customer_id
    order.status = order_update.status
    order.total_price = order_update.total_price

    db.commit()
    db.refresh(order)

    return order


def delete_order(db: Session, order_id: int):
    order = get_order(db, order_id)

    db.delete(order)
    db.commit()

    return {"message": "Order deleted successfully"}
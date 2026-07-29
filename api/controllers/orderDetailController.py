from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import order_details as model
from ..schemas import orderDetailSchema as schema


def create(db: Session, order_detail: schema.OrderDetailCreate):
    new_order_detail = model.OrderDetail(
        order_id=order_detail.order_id,
        item_id=order_detail.item_id,
        quantity=order_detail.quantity
    )

    db.add(new_order_detail)
    db.commit()
    db.refresh(new_order_detail)

    return new_order_detail


def get_all(db: Session):
    return db.query(model.OrderDetail).all()


def get(db: Session, order_detail_id: int):
    order_detail = (
        db.query(model.OrderDetail)
        .filter(model.OrderDetail.order_detail_id == order_detail_id)
        .first()
    )

    if order_detail is None:
        raise HTTPException(
            status_code=404,
            detail="Order detail not found"
        )

    return order_detail


def update(
    db: Session,
    order_detail_id: int,
    order_detail_update: schema.OrderDetailUpdate
):
    order_detail = get(db, order_detail_id)

    order_detail.order_id = order_detail_update.order_id
    order_detail.item_id = order_detail_update.item_id
    order_detail.quantity = order_detail_update.quantity

    db.commit()
    db.refresh(order_detail)

    return order_detail


def delete(db: Session, order_detail_id: int):
    order_detail = get(db, order_detail_id)

    db.delete(order_detail)
    db.commit()

    return {"message": "Order detail deleted successfully"}
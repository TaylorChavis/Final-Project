from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import payments as model
from ..schemas import paymentSchema as schema


def create(db: Session, payment: schema.PaymentCreate):
    new_payment = model.Payment(
        order_id=payment.order_id,
        payment_type=payment.payment_type
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return new_payment


def get_all(db: Session):
    return db.query(model.Payment).all()


def get(db: Session, payment_id: int):
    payment = (
        db.query(model.Payment)
        .filter(model.Payment.payment_id == payment_id)
        .first()
    )

    if payment is None:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment


def update(
    db: Session,
    payment_id: int,
    payment_update: schema.PaymentUpdate
):
    payment = get(db, payment_id)

    payment.order_id = payment_update.order_id
    payment.payment_type = payment_update.payment_type

    db.commit()
    db.refresh(payment)

    return payment


def delete(db: Session, payment_id: int):
    payment = get(db, payment_id)

    db.delete(payment)
    db.commit()

    return {"message": "Payment deleted successfully"}
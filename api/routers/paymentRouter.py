from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import paymentController as controller
from ..dependencies.database import get_db
from ..schemas import paymentSchema as schema


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post("/")
def create(
    payment: schema.PaymentCreate,
    db: Session = Depends(get_db)
):
    return controller.create(
        db=db,
        payment=payment
    )


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return controller.get_all(db=db)


@router.get("/{payment_id}")
def get(
    payment_id: int,
    db: Session = Depends(get_db)
):
    return controller.get(
        db=db,
        payment_id=payment_id
    )


@router.put("/{payment_id}")
def update(
    payment_id: int,
    payment: schema.PaymentUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        payment_id=payment_id,
        payment_update=payment
    )


@router.delete("/{payment_id}")
def delete(
    payment_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        payment_id=payment_id
    )
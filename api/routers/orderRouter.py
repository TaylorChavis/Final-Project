from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import orderController as controller
from ..dependencies.database import get_db
from ..schemas import orderSchema


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/")
def create(
    order: orderSchema.OrderCreate,
    db: Session = Depends(get_db)
):
    return controller.create_order(
        db=db,
        order=order
    )


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return controller.get_orders(db=db)


@router.get("/{order_id}")
def get(
    order_id: int,
    db: Session = Depends(get_db)
):
    return controller.get_order(
        db=db,
        order_id=order_id
    )


@router.put("/{order_id}")
def update(
    order_id: int,
    order: orderSchema.OrderUpdate,
    db: Session = Depends(get_db)
):
    return controller.update_order(
        db=db,
        order_id=order_id,
        order_update=order
    )


@router.delete("/{order_id}")
def delete(
    order_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete_order(
        db=db,
        order_id=order_id
    )
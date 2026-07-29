from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import orderDetailController as controller
from ..dependencies.database import get_db
from ..schemas import orderDetailSchema as schema


router = APIRouter(
    prefix="/order-details",
    tags=["Order Details"]
)


@router.post("/")
def create(
    order_detail: schema.OrderDetailCreate,
    db: Session = Depends(get_db)
):
    return controller.create(
        db=db,
        order_detail=order_detail
    )


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return controller.get_all(db=db)


@router.get("/{order_detail_id}")
def get(
    order_detail_id: int,
    db: Session = Depends(get_db)
):
    return controller.get(
        db=db,
        order_detail_id=order_detail_id
    )


@router.put("/{order_detail_id}")
def update(
    order_detail_id: int,
    order_detail: schema.OrderDetailUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        order_detail_id=order_detail_id,
        order_detail_update=order_detail
    )


@router.delete("/{order_detail_id}")
def delete(
    order_detail_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        order_detail_id=order_detail_id
    )
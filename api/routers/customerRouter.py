from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import customerController as controller
from ..dependencies.database import get_db
from ..schemas import customerSchema

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/")
def create(customer: customerSchema.CustomerCreate,
           db: Session = Depends(get_db)):
    return controller.create_customer(db=db, customer=customer)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return controller.get_customers(db=db)


@router.get("/{customer_id}")
def get(customer_id: int,
        db: Session = Depends(get_db)):
    return controller.get_customer(db=db, customer_id=customer_id)


@router.put("/{customer_id}")
def update(customer_id: int,
           customer: customerSchema.CustomerUpdate,
           db: Session = Depends(get_db)):
    return controller.update_customer(
        db=db,
        customer_id=customer_id,
        customer_update=customer
    )


@router.delete("/{customer_id}")
def delete(customer_id: int,
           db: Session = Depends(get_db)):
    return controller.delete_customer(
        db=db,
        customer_id=customer_id
    )
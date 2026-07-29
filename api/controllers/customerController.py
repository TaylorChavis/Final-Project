from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import customers as customerModel
from ..schemas import customerSchema


def create_customer(
    db: Session,
    customer: customerSchema.CustomerCreate
):
    existing_customer = (
        db.query(customerModel.Customer)
        .filter(customerModel.Customer.email == customer.email)
        .first()
    )

    if existing_customer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A customer with this email already exists"
        )

    new_customer = customerModel.Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        email=customer.email,
        phone=customer.phone,
        address=customer.address
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


def get_customers(db: Session):
    return db.query(customerModel.Customer).all()


def get_customer(db: Session, customer_id: int):
    customer = (
        db.query(customerModel.Customer)
        .filter(customerModel.Customer.customer_id == customer_id)
        .first()
    )

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return customer


def update_customer(
    db: Session,
    customer_id: int,
    customer_update: customerSchema.CustomerUpdate
):
    customer = get_customer(db, customer_id)

    email_owner = (
        db.query(customerModel.Customer)
        .filter(
            customerModel.Customer.email == customer_update.email,
            customerModel.Customer.customer_id != customer_id
        )
        .first()
    )

    if email_owner:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A customer with this email already exists"
        )

    customer.first_name = customer_update.first_name
    customer.last_name = customer_update.last_name
    customer.email = customer_update.email
    customer.phone = customer_update.phone
    customer.address = customer_update.address

    db.commit()
    db.refresh(customer)

    return customer


def delete_customer(db: Session, customer_id: int):
    customer = get_customer(db, customer_id)

    db.delete(customer)
    db.commit()

    return {"message": "Customer deleted successfully"}
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    order_date = Column(DateTime, server_default=func.now())

    status = Column(String(50), default="Pending")

    total = Column(Float, nullable=False, default=0)

    customer = relationship("Customer")

    order_details = relationship("OrderDetail", back_populates="order")
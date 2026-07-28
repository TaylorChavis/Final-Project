from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)

    order_date = Column(DateTime, server_default=func.now())

    status = Column(String(50), default="Pending")

    total_price = Column(Float, nullable=False, default=0)
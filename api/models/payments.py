from sqlalchemy import Column, Integer, String, ForeignKey

from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)

    payment_type = Column(String(50), nullable=False)

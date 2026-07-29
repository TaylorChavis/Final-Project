from datetime import datetime
from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    customer_id: int
    status: str = "Pending"
    total_price: float = 0


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class OrderResponse(OrderBase):
    order_id: int
    order_date: datetime

    model_config = ConfigDict(from_attributes=True)
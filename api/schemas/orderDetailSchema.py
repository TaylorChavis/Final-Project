from pydantic import BaseModel, ConfigDict


class OrderDetailBase(BaseModel):
    order_id: int
    item_id: int
    quantity: int


class OrderDetailCreate(OrderDetailBase):
    pass


class OrderDetailUpdate(OrderDetailBase):
    pass


class OrderDetailResponse(OrderDetailBase):
    order_detail_id: int

    model_config = ConfigDict(from_attributes=True)
from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    order_id: int
    payment_type: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(PaymentBase):
    pass


class PaymentResponse(PaymentBase):
    payment_id: int

    model_config = ConfigDict(from_attributes=True)
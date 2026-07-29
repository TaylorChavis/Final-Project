from pydantic import BaseModel, ConfigDict


class InventoryBase(BaseModel):
    item_id: int
    quantity: int


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(InventoryBase):
    pass


class InventoryResponse(InventoryBase):
    inventory_id: int

    model_config = ConfigDict(from_attributes=True)
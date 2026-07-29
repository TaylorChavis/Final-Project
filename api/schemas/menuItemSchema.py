from pydantic import BaseModel, ConfigDict


class MenuItemBase(BaseModel):
    item_name: str
    category: str
    price: float
    available: bool = True


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(MenuItemBase):
    pass


class MenuItemResponse(MenuItemBase):
    item_id: int

    model_config = ConfigDict(from_attributes=True)
from sqlalchemy import Column, Integer, ForeignKey

from ..dependencies.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    item_id = Column(Integer, ForeignKey("menu_items.item_id"), nullable=False)

    quantity = Column(Integer, nullable=False)
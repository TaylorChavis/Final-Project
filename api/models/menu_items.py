from sqlalchemy import Column, Integer, String, Float, Boolean

from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    item_id = Column(Integer, primary_key=True, index=True)

    item_name = Column(String(100), nullable=False)

    category = Column(String(50), nullable=False)

    price = Column(Float, nullable=False)

    available = Column(Boolean, default=True)
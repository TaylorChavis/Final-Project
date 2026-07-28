from sqlalchemy import Column, Integer, ForeignKey

from ..dependencies.database import Base


class OrderDetail(Base):
    __tablename__ = "order_details"

    order_detail_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)

    item_id = Column(Integer, ForeignKey("menu_items.item_id"), nullable=False)

    quantity = Column(Integer, nullable=False)
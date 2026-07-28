from sqlalchemy import Column, Integer, String, ForeignKey

from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)

    item_id = Column(Integer, ForeignKey("menu_items.item_id"), nullable=False)

    rating = Column(Integer, nullable=False)
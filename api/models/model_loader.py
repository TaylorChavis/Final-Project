from . import (
    customers,
    menu_items,
    orders,
    order_details,
    inventory,
    payments,
    reviews,
)

from ..dependencies.database import Base, engine


def index():
    Base.metadata.create_all(bind=engine)
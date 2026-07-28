from . import (
    customers,
    menu_items,
    orders,
    order_details,
    inventory,
    payments,
    reviews,
)

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(bind=engine)
    menu_items.Base.metadata.create_all(bind=engine)
    orders.Base.metadata.create_all(bind=engine)
    order_details.Base.metadata.create_all(bind=engine)
    inventory.Base.metadata.create_all(bind=engine)
    payments.Base.metadata.create_all(bind=engine)
    reviews.Base.metadata.create_all(bind=engine)
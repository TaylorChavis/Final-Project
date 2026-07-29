from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import menu_items as menuItemModel
from ..schemas import menuItemSchema


def create_menu_item(
    db: Session,
    menu_item: menuItemSchema.MenuItemCreate
):
    new_menu_item = menuItemModel.MenuItem(
        item_name=menu_item.item_name,
        category=menu_item.category,
        price=menu_item.price,
        available=menu_item.available
    )

    db.add(new_menu_item)
    db.commit()
    db.refresh(new_menu_item)

    return new_menu_item


def get_menu_items(db: Session):
    return db.query(menuItemModel.MenuItem).all()


def get_menu_item(db: Session, item_id: int):
    menu_item = (
        db.query(menuItemModel.MenuItem)
        .filter(menuItemModel.MenuItem.item_id == item_id)
        .first()
    )

    if menu_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu item not found"
        )

    return menu_item


def update_menu_item(
    db: Session,
    item_id: int,
    menu_item_update: menuItemSchema.MenuItemUpdate
):
    menu_item = get_menu_item(db, item_id)

    menu_item.item_name = menu_item_update.item_name
    menu_item.category = menu_item_update.category
    menu_item.price = menu_item_update.price
    menu_item.available = menu_item_update.available

    db.commit()
    db.refresh(menu_item)

    return menu_item


def delete_menu_item(db: Session, item_id: int):
    menu_item = get_menu_item(db, item_id)

    db.delete(menu_item)
    db.commit()

    return {"message": "Menu item deleted successfully"}
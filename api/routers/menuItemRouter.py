from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import menuItemController as controller
from ..dependencies.database import get_db
from ..schemas import menuItemSchema


router = APIRouter(
    prefix="/menu-items",
    tags=["Menu Items"]
)


@router.post("/")
def create(
    menu_item: menuItemSchema.MenuItemCreate,
    db: Session = Depends(get_db)
):
    return controller.create_menu_item(
        db=db,
        menu_item=menu_item
    )


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return controller.get_menu_items(db=db)


@router.get("/{item_id}")
def get(
    item_id: int,
    db: Session = Depends(get_db)
):
    return controller.get_menu_item(
        db=db,
        item_id=item_id
    )


@router.put("/{item_id}")
def update(
    item_id: int,
    menu_item: menuItemSchema.MenuItemUpdate,
    db: Session = Depends(get_db)
):
    return controller.update_menu_item(
        db=db,
        item_id=item_id,
        menu_item_update=menu_item
    )


@router.delete("/{item_id}")
def delete(
    item_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete_menu_item(
        db=db,
        item_id=item_id
    )
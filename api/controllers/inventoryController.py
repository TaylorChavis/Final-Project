from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import inventory as model
from ..schemas import inventorySchema as schema


def create(db: Session, inventory: schema.InventoryCreate):
    new_inventory = model.Inventory(
        item_id=inventory.item_id,
        quantity=inventory.quantity
    )

    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)

    return new_inventory


def get_all(db: Session):
    return db.query(model.Inventory).all()


def get(db: Session, inventory_id: int):
    inventory = (
        db.query(model.Inventory)
        .filter(model.Inventory.inventory_id == inventory_id)
        .first()
    )

    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail="Inventory record not found"
        )

    return inventory


def update(
    db: Session,
    inventory_id: int,
    inventory_update: schema.InventoryUpdate
):
    inventory = get(db, inventory_id)

    inventory.item_id = inventory_update.item_id
    inventory.quantity = inventory_update.quantity

    db.commit()
    db.refresh(inventory)

    return inventory


def delete(db: Session, inventory_id: int):
    inventory = get(db, inventory_id)

    db.delete(inventory)
    db.commit()

    return {"message": "Inventory record deleted successfully"}
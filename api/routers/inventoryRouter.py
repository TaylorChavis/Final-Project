from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import inventoryController as controller
from ..dependencies.database import get_db
from ..schemas import inventorySchema as schema


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.post("/")
def create(
    inventory: schema.InventoryCreate,
    db: Session = Depends(get_db)
):
    return controller.create(
        db=db,
        inventory=inventory
    )


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return controller.get_all(db=db)


@router.get("/{inventory_id}")
def get(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    return controller.get(
        db=db,
        inventory_id=inventory_id
    )


@router.put("/{inventory_id}")
def update(
    inventory_id: int,
    inventory: schema.InventoryUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        inventory_id=inventory_id,
        inventory_update=inventory
    )


@router.delete("/{inventory_id}")
def delete(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        inventory_id=inventory_id
    )
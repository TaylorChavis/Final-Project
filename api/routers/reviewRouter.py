from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import reviewController as controller
from ..dependencies.database import get_db
from ..schemas import reviewSchema as schema


router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.post("/")
def create(
    review: schema.ReviewCreate,
    db: Session = Depends(get_db)
):
    return controller.create(
        db=db,
        review=review
    )


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return controller.get_all(db=db)


@router.get("/{review_id}")
def get(
    review_id: int,
    db: Session = Depends(get_db)
):
    return controller.get(
        db=db,
        review_id=review_id
    )


@router.put("/{review_id}")
def update(
    review_id: int,
    review: schema.ReviewUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        review_id=review_id,
        review_update=review
    )


@router.delete("/{review_id}")
def delete(
    review_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        review_id=review_id
    )
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import reviews as model
from ..schemas import reviewSchema as schema


def create(db: Session, review: schema.ReviewCreate):
    new_review = model.Review(
        customer_id=review.customer_id,
        item_id=review.item_id,
        rating=review.rating
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review


def get_all(db: Session):
    return db.query(model.Review).all()


def get(db: Session, review_id: int):
    review = (
        db.query(model.Review)
        .filter(model.Review.review_id == review_id)
        .first()
    )

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return review


def update(
    db: Session,
    review_id: int,
    review_update: schema.ReviewUpdate
):
    review = get(db, review_id)

    review.customer_id = review_update.customer_id
    review.item_id = review_update.item_id
    review.rating = review_update.rating

    db.commit()
    db.refresh(review)

    return review


def delete(db: Session, review_id: int):
    review = get(db, review_id)

    db.delete(review)
    db.commit()

    return {"message": "Review deleted successfully"}
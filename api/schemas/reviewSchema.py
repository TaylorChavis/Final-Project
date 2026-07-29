from pydantic import BaseModel, ConfigDict, Field


class ReviewBase(BaseModel):
    customer_id: int
    item_id: int
    rating: int = Field(ge=1, le=5)


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(ReviewBase):
    pass


class ReviewResponse(ReviewBase):
    review_id: int

    model_config = ConfigDict(from_attributes=True)
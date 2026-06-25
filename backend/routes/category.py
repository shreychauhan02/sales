from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Category
from schemas import CategoryCreate
from crud import *

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/")
def create_category(category: CategoryCreate,
                    db: Session = Depends(get_db)):
    return create_record(db, Category, category)


@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return get_all(db, Category)


@router.get("/{cat_id}")
def get_category(cat_id: int,
                 db: Session = Depends(get_db)):

    category = get_by_id(
        db,
        Category,
        Category.cat_id,
        cat_id
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


@router.delete("/{cat_id}")
def delete_category(cat_id: int,
                    db: Session = Depends(get_db)):

    category = get_by_id(
        db,
        Category,
        Category.cat_id,
        cat_id
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    delete_record(db, category)

    return {"message": "Category deleted"}
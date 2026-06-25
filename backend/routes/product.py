from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Product
from schemas import ProductCreate
from crud import *

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/")
def create_product(product: ProductCreate,
                   db: Session = Depends(get_db)):
    return create_record(db, Product, product)


@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return get_all(db, Product)


@router.get("/{product_id}")
def get_product(product_id: int,
                db: Session = Depends(get_db)):

    product = get_by_id(
        db,
        Product,
        Product.p_id,
        product_id
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.delete("/{product_id}")
def delete_product(product_id: int,
                   db: Session = Depends(get_db)):

    product = get_by_id(
        db,
        Product,
        Product.p_id,
        product_id
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    delete_record(db, product)

    return {"message": "Product deleted"}
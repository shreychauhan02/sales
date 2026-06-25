from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Orders
from schemas import OrderCreate
from crud import *

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):
    return create_record(db, Orders, order)


@router.get("/")
def get_orders(
    db: Session = Depends(get_db)
):
    return get_all(db, Orders)


@router.get("/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = get_by_id(
        db,
        Orders,
        Orders.o_id,
        order_id
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = get_by_id(
        db,
        Orders,
        Orders.o_id,
        order_id
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    delete_record(db, order)

    return {"message": "Order deleted"}
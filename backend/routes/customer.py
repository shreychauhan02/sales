from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Customer
from schemas import CustomerCreate
from crud import *

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/")
def create_customer(customer: CustomerCreate,
                    db: Session = Depends(get_db)):
    return create_record(db, Customer, customer)


@router.get("/")
def get_customers(db: Session = Depends(get_db)):
    return get_all(db, Customer)


@router.get("/{customer_id}")
def get_customer(customer_id: int,
                 db: Session = Depends(get_db)):

    customer = get_by_id(
        db,
        Customer,
        Customer.id,
        customer_id
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.delete("/{customer_id}")
def delete_customer(customer_id: int,
                    db: Session = Depends(get_db)):

    customer = get_by_id(
        db,
        Customer,
        Customer.id,
        customer_id
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    delete_record(db, customer)

    return {"message": "Customer deleted"}
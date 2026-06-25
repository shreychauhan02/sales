from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Employee
from schemas import EmployeeCreate
from crud import *

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return create_record(db, Employee, employee)


@router.get("/")
def get_employees(
    db: Session = Depends(get_db)
):
    return get_all(db, Employee)


@router.get("/{emp_id}")
def get_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    employee = get_by_id(
        db,
        Employee,
        Employee.emp_id,
        emp_id
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@router.delete("/{emp_id}")
def delete_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    employee = get_by_id(
        db,
        Employee,
        Employee.emp_id,
        emp_id
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    delete_record(db, employee)

    return {
        "message": "Employee deleted"
    }
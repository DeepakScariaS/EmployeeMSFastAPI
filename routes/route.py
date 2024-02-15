from http.client import HTTPException

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import update
from sqlalchemy.orm import Session

from config.database import SessionLocal
from models.employee import Employee

from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Depends(get_db)


class CreateEmployeeRequest(BaseModel):
    employee_name: str
    phone_number: str
    age: int


# POST
@router.post("/")
async def post_employee(employee: CreateEmployeeRequest, db: Session = db_dependency):
    create_employee_model = Employee(
        employee_name=employee.employee_name,
        phone_number=employee.phone_number,
        age=employee.age
    )
    db.add(create_employee_model)
    db.commit()
    return {"Success": "Employee created!"}


@router.get("/getAll")
async def get_all_employee(db: Session = db_dependency):
    employees = db.query(Employee).all()
    return employees


@router.put("/{id}")
async def update_employee(id: int, employee: CreateEmployeeRequest, db: Session = db_dependency):
    existing_employee = db.query(Employee).filter(Employee.id == id).first()
    if not existing_employee:
        return {"error": "Employee not found"}

    existing_employee.student_name = employee.employee_name
    existing_employee.phone_number = employee.phone_number
    existing_employee.age = employee.age

    db.commit()
    return {"Employee updated successfully!"}


@router.delete("/{id}")
async def delete_employee(id: int, db: Session = db_dependency):
    employee = db.query(Employee).filter(Employee.id == id).first()
    if not employee:
        return {"error": "Student not found"}

    db.delete(employee)
    db.commit()
    return {"Item deleted Successfully!"}

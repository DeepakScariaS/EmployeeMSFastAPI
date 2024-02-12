from fastapi import APIRouter

from models.employee import Employee

from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


# GET Request Method
@router.get("/")
async def get_todos():
    employees = list_serial(collection_name.find())
    return employees


# POST
@router.post("/")
async def post_todo(emp: Employee):
    collection_name.insert_one(dict(emp))


# PUT
@router.put("/{id}")
async def put_todo(id: str, emp: Employee):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(emp)})


# DELETE
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})

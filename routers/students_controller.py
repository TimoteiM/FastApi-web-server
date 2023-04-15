from fastapi import APIRouter, HTTPException, Depends, Request
from config.config import collection
from models.student_model import BaseStudentModel, SaveStudentModel, ObjectId
from fastapi.encoders import jsonable_encoder
# from auth.Auth import generate_token, verify_token
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from models.user_model import User
from typing import List

router = APIRouter(prefix='/students',
                    tags=['students'])



@router.post("/students", response_model=BaseStudentModel)
async def create_student(student: SaveStudentModel):
    result = collection.insert_one(student.dict())
    found_student = collection.find_one({"_id": result.inserted_id})
    if found_student:
        return found_student
    raise HTTPException(status_code=404, detail="Student was not created!")

@router.get("/", response_model=list[BaseStudentModel])
async def get_all_students():
    found_students = collection.find()
    all_students = []
    for x in found_students:
        all_students.append(x)
    return all_students
    
# find = {"f_name": {"$regex": "^A"}}
# collection.delete_one(find)

@router.get("/{student_id}", response_model=BaseStudentModel)
async def get_student(student_id: str):
    found_student = collection.find_one({"_id": ObjectId(student_id)})
    print(f"L-am gasit pe {found_student}")
    if found_student:
        return found_student
    raise HTTPException(status_code=404, detail=f"Student with id {student_id} has not been found")
    

@router.put("/{student_id}")
async def update_student(student_id: str, student: SaveStudentModel):
    found_student = collection.replace_one({"_id": ObjectId(student_id)}, student.dict())
    print(student.dict())
    if found_student.modified_count == 1:
        return {"message": "Student was updated succesfully"}
    raise HTTPException(status_code=404, detail="Student was not found")



@router.delete("/{student_id}")
async def delete_student(student_id: str):
    found_student = collection.delete_one({"_id": ObjectId(student_id)})
    if found_student.deleted_count == 1:
        return {"message": "Student was deleted succesfully"}
    #raise HTTPException(status_code=404, detail="Student was not found")
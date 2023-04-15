from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from config.config import grades_collection
from models.grades_model import Grade, SavedGrade, GradeBody, ObjectId


router = APIRouter(prefix='/grades',
                    tags=['grades'])

@router.post('/{student_id}', response_model=Grade)
async def evaluate_student(student_id: str, grade: GradeBody):
   
    full_grade = {
        'value': grade.value,
        'materie': grade.materie,
        'student_id': student_id
    }
    
    result = grades_collection.insert_one(full_grade)
    found_grade = grades_collection.find_one({"_id": result.inserted_id})
    if found_grade:
        return found_grade
    else:
        raise HTTPException(status_code=500)
    
@router.get('/{student_id}', response_model=list[Grade])
async def get_grade_allDisciplines(student_id: str):
    found_grades = grades_collection.find({"student_id": student_id})
    all_grades =[]
    for x in found_grades:
        all_grades.append(x)
    if len(all_grades) > 0:
        return all_grades
    else:
        raise HTTPException(status_code=404, detail="Student or grades are not in the database!") 
    
@router.get('/{student_id}/{disciplina}', response_model=list[Grade])
async def Get_grade_byDiscipline(student_id: str, disciplina: str):
    found_grades = grades_collection.find({'student_id': student_id, 'materie': disciplina})
    all_grades = []
    for x in found_grades:
        all_grades.append(x)
    if len(all_grades) > 0:
        return all_grades
    else:
        raise HTTPException(status_code=404, detail="Grades were not found!")
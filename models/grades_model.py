from pydantic import BaseModel, Field
from typing import Optional
from bson.objectid import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

class Grade(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    value: float
    materie: str
    student_id: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class SavedGrade(BaseModel):
    value: Optional[float]
    materie: Optional[str]
    student_id: Optional[str]


class GradeBody(BaseModel):
    value: float
    materie: str
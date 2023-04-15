from pydantic import BaseModel, Field
from typing import Optional
import uuid 
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


class BaseStudentModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    f_name: str
    l_name: str
    active: bool
    media: Optional[float] = None
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class SaveStudentModel(BaseModel):
    f_name: str
    l_name: str
    active: bool
    media: Optional[float] = None

    # def __init__(self, f_name, l_name, active, media):
    #     self.f_name = f_name
    #     self.l_name = l_name
    #     self.active = active
    #     self.media = media
    
    
    

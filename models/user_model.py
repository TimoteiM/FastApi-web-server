from pydantic import BaseModel, EmailStr
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
class User(BaseModel):
    fullname: str
    email: EmailStr
    password: str
    role: str
    class Config:
        the_model = {
            "user_demo": {
            "name": 'Timothy',
            "email": "moscaliuc_timotei@yahoo.com",
            "password": '1234'
            }
        }

class UserLogin(BaseModel):
     email: EmailStr
     password: str
     class Config:
        the_model = {
            "user_demo": {
            "email": "moscaliuc_timotei@yahoo.com",
            "password": '1234'
            }
        }

class UserInfo(BaseModel):
    fullname: str
    role: str
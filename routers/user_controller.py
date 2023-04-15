# from fastapi import APIRouter, HTTPException, status, Depends, Request, Body
# from models.user_model import User, UserLogin, UserInfo, ObjectId
# from auth.Auth import generate_token, verify_token
# from config.config import user_collection
# import json 
# import bson.json_util as json_util

# router = APIRouter(prefix='/user',
#                     tags=['user'])


# @router.post('/login', response_model=UserInfo)
# async def login(user: UserLogin):
#         searched_user = user_collection.find_one({'email': user.email,
#                                                   'password': user.password})
        
#         if searched_user == None:
#                 raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="The email or password is incorrect!")
#         else:
#                 # raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail="Acces granted")
#                 user_id = searched_user['_id']
#                 token = generate_token(user_id)
#                 return token
        
    
# @router.post('/signup', status_code=status.HTTP_201_CREATED)
# async def create_user(user_info : User):
#         find_user = user_collection.find_one({'email': user_info.email})
        
#         if find_user == None:
#                 verified_user = user_collection.insert_one(user_info.dict())
#                 user_id = ObjectId(verified_user.inserted_id)
#                 # token = generate_token(user_id)
#                 # print(token)
#                 # return {"token": token}
#         else:
#                 raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="A user with this email already exist!")
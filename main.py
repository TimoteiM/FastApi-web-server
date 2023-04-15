from fastapi import FastAPI, HTTPException, Depends
from routers import students_controller, grades_controller, user_controller


import uuid

app = FastAPI()



app.include_router(students_controller.router)
app.include_router(grades_controller.router)
# app.include_router(user_controller.router)

@app.get("/")
async def hello():
    return "hello, type: /docs at the end of the url!"




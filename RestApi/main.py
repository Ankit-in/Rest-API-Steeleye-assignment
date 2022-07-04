import datetime as dt
from typing import List
from fastapi import FastAPI, HTTPException
from models import Role, User,Gender, UserUpdateRequest
from uuid import uuid4, UUID


app=FastAPI()


db: List[User]=[
    User(
        id=UUID("b26814a4-b4b3-4268-a687-1e66bf1fedb3"),
        first_name="Ankit",
        last_name="Singh",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("342c354e-bc16-4e32-94c5-3d72abfd59a6"),
        first_name="Singh",
        last_name="Ankit",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )

]

@app.get("/")
async def root():
    return {"Hello": "Ankit"}


@app.get("/api/v1/User")
async def fetch_users():
    return db;

@app.post("/api/v1/User")
async def register_user(user:User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/User{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(User)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )

@app.put("/api/v1/User/{user_id}")
async def update_user(user_update: UserUpdateRequest,user_id:UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )
from typing import Union
from fastapi import FastAPI
from models.user import User

app=FastAPI()
users=[]

@app.get("/")
async def home():
    return {"message":"Hello World"}

@app.post("/accounts/create/")
async def create_user(user: User):
    users.append(user)
    return {"User":user}

@app.get("/accounts/lists/")
async def get_users():
    usernames=[]
    for user in users:
        usernames.append(user.username)
    return {"Users":usernames}


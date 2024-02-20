from fastapi import FastAPI
from models.user import User
from pydantic import SecretStr,ValidationError
import uuid

app=FastAPI()
users=[]

@app.get("/")
async def home():
    return {"message":"Hello World"}

@app.post("/accounts/create/")
async def signup(user: User):
    try:
        user.uuid=uuid.uuid4()
        users.append(user)
    except ValidationError as password_error:
        return {"Error":password_error}
    
    print(user)
    return {"User":user}

@app.get("/accounts/lists/")
async def get_users():
    usernames=[]
    for user in users:
        usernames.append(user.uuid)
    return {"Users":usernames}

@app.post("/accounts/login/")
async def login(username: str,password: SecretStr):
    for user in users:
        print()
        if user.username==username and user.password==password:
            return {
                "User Id":user.uuid,
                "Username":user.username,
                "Status":"Logged In Successfully"
            }
    return {"Status":"Please provide valid credentials!!"}



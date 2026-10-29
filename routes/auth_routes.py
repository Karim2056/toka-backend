from fastapi import APIRouter
from models.SignUp_models import SignUpForm
from models.Login_models import LoginForm
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from database import users

auth_router = APIRouter()

@auth_router.post("/signup")
def signup(signup_data: SignUpForm):

    # 1. check for duplicated users
    # insert a new user
    # check if a duplicated user exists
    # if non existent then return a success message

    try:
        users.insert_one({
            "email": signup_data.email,
            "username": signup_data.username,
            "password": signup_data.password,
            "tier": signup_data.tier,
        })
    except DuplicateKeyError:
        raise HTTPException(
            status_code=409,
            detail="account already exists",
        )


    # 2. hash password

    # 3. save to database

    # 4. return a response message

    return {"status": "success"}



@auth_router.post("/login")
def login(login_data: LoginForm):
    return {
        
    }
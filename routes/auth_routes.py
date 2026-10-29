from fastapi import APIRouter
from models.SignUp_models import SignUpForm
from models.Login_models import LoginForm
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from database import users
import bcrypt

auth_router = APIRouter()

@auth_router.post("/signup")
def signup(signup_data: SignUpForm):

    # 1. check for duplicated users
    # insert a new user
    # check if a duplicated user exists
    # if non existent then return a success message

    # 2. hashing
    # convert pass to bytes, then hash it using bcrypt
    password_bytes = signup_data.password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt).decode("utf-8")

    try:
        users.insert_one({
            "email": signup_data.email,
            "username": signup_data.username,
            "password": hashed_password,
            "tier": signup_data.tier,
        })
    except DuplicateKeyError:
        raise HTTPException(
            status_code=409,
            detail="account already exists",
        )

    return {"account": "created"}



@auth_router.post("/login")
def login(login_data: LoginForm):
    return {
        
    }
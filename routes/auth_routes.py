from fastapi import APIRouter
from models.SignUp_models import SignUpForm
from models.Login_models import LoginForm
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from database import users
from database import db
from datetime import datetime
import bcrypt

auth_router = APIRouter()

@auth_router.post("/signup")
def signup(signup_data: SignUpForm):

    # 1. hashing
    # convert pass to bytes, then hash it using bcrypt
    password_bytes = signup_data.password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt).decode("utf-8")

    workouts_collection = db["workouts"]
    meals_collection = db["meals"]
    today_date = datetime.now().strftime("%Y-%m-%d")

    try:
        users.insert_one({
            "email": signup_data.email,
            "username": signup_data.username,
            "password": hashed_password,
            "tier": signup_data.tier,
        })
        
        # Initialize default workout preferences
        workouts_collection.insert_one({
            "username": signup_data.username,
            "selected_goal": "Muscle Gain",
            "days": {
                "Mon": False, "Tue": False, "Wed": False, 
                "Thu": False, "Fri": False, "Sat": False, "Sun": False
            }
        })

        # Initialize default empty meal log for today
        meals_collection.insert_one({
            "username": signup_data.username,
            "date": today_date,
            "meals": []
        })

    except DuplicateKeyError:
        raise HTTPException(
            status_code=409,
            detail="account already exists",
        )

    return {"account": "created"}



@auth_router.post("/login")
def login(login_data: LoginForm):

    # finds user based on existing username
    user = users.find_one({
        "username": login_data.username
    })

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="account not found, try again",
        )

    # convert pass into bytes
    pass_bytes = login_data.password.encode("utf-8")

    # convert hashed pass from database into bytes
    stored_pass_bytes = user["password"].encode("utf-8")

    # compare if they match using bcrypt.checkpw()
    if not bcrypt.checkpw(pass_bytes, stored_pass_bytes):
        raise HTTPException(
            status_code=401,
            detail="invalid password, try again"
        )

    return {"logged": "in",
            "tier": user["tier"]
            }
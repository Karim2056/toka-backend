from fastapi import APIRouter
from models.SignUp_models import SignUpForm
from models.Login_models import LoginForm

auth_router = APIRouter()

@auth_router.post("/signup")
def signup(signup_data: SignUpForm):
    data = signup_data.model_dump()
    return {
        
    }

@auth_router.post("/login")
def login(login_data: LoginForm):
    return {
        
    }
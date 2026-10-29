from pydantic import BaseModel

class SignUpForm(BaseModel):
    email: str
    username: str
    password: str
    tier: str
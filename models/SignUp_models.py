from pydantic import BaseModel, EmailStr, Field

class SignUpForm(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=2, max_length=20)
    password: str = Field(..., min_length=8)
    tier: str
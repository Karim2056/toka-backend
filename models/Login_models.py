from pydantic import BaseModel, Field

class LoginForm(BaseModel):
    username: str = Field(..., min_length=2, max_length=20)
    password: str = Field(..., min_length=8)
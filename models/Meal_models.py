from pydantic import BaseModel
from typing import List

class MealItem(BaseModel):
    id: int
    name: str
    calories: int

class UserMealPreferences(BaseModel):
    username: str
    date: str  # Format: "YYYY-MM-DD" to handle daily resets
    meals: List[MealItem] = []
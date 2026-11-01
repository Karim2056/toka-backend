from pydantic import BaseModel

class WorkoutDaysModel(BaseModel):
    Mon: bool = False
    Tue: bool = False
    Wed: bool = False
    Thu: bool = False
    Fri: bool = False
    Sat: bool = False
    Sun: bool = False

class UserWorkoutPreferences(BaseModel):
    username: str
    selected_goal: str
    days: WorkoutDaysModel
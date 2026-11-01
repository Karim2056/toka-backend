from fastapi import APIRouter
from models.Workout_models import UserWorkoutPreferences
from database import db

workout_router = APIRouter()
workouts_collection = db["workouts"]

@workout_router.get("/{username}", response_model=UserWorkoutPreferences)
def get_workout_preferences(username: str):
    record = workouts_collection.find_one({"username": username})
    if record:
        record["_id"] = str(record["_id"])
        return record

    return {
        "username": username,
        "selected_goal": "Muscle Gain",
        "days": {
            "Mon": False,
            "Tue": False,
            "Wed": False,
            "Thu": False,
            "Fri": False,
            "Sat": False,
            "Sun": False,
        }
    }

@workout_router.post("", response_model=UserWorkoutPreferences)
def save_workout_preferences(preferences: UserWorkoutPreferences):
    workouts_collection.update_one(
        {"username": preferences.username},
        {"$set": preferences.model_dump()},
        upsert=True
    )
    return preferences
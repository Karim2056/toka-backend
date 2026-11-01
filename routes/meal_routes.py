from fastapi import APIRouter
from models.Meal_models import UserMealPreferences
from database import db
from datetime import datetime

meal_router = APIRouter()
meals_collection = db["meals"]

@meal_router.get("/{username}", response_model=UserMealPreferences)
def get_meals(username: str):
    today_date = datetime.now().strftime("%Y-%m-%d")
    record = meals_collection.find_one({"username": username, "date": today_date})
    
    if record:
        record["_id"] = str(record["_id"])
        return record

    return {
        "username": username,
        "date": today_date,
        "meals": []
    }

@meal_router.post("", response_model=UserMealPreferences)
def save_meals(preferences: UserMealPreferences):
    meals_collection.update_one(
        {"username": preferences.username, "date": preferences.date},
        {"$set": preferences.model_dump()},
        upsert=True
    )
    return preferences
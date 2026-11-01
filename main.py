from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import auth_router
from routes.workout_routes import workout_router
from routes.meal_routes import meal_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", "http://localhost:5174", "http://localhost:5175",
        "http://127.0.0.1:5173", "http://127.0.0.1:5174", "http://127.0.0.1:5175",
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
    allow_credentials=True,
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    workout_router,
    prefix="/workout",
    tags=["Workout"]
)

app.include_router(
    meal_router,
    prefix="/meal",
    tags=["Meal"]
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
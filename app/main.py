from fastapi import FastAPI
from app.routes import auth, admin, user
from app.config import engine, Base
from app.models import *

app = FastAPI()

# Create Tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(user.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Restaurant Table Booking System!"}
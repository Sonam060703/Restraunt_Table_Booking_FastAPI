from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import UserCreate, UserResponse
from app.models import User
from app.utils import get_password_hash, verify_password, create_access_token
from app.config import SessionLocal
from sqlalchemy.orm import Session
from app.utils import authenticate_user, create_access_token, get_current_user, oauth2_scheme
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password , is_admin=user.is_admin)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

# Logout (Optional JWT Blacklist)
blacklisted_tokens = set()

@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    blacklisted_tokens.add(token)
    return {"message": "Successfully logged out"}

@router.get("/protected-route")
def protected_route(user = Depends(get_current_user)):
    return {"message": f"Hello, {user.username}!"}
from fastapi import Depends, HTTPException
from app.utils import get_current_user
from app.models import User
from sqlalchemy.orm import Session
from app.config import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_admin_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user
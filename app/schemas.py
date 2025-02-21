from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_admin: bool

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_admin: bool

class TableCreate(BaseModel):
    seats: int

class TableResponse(BaseModel):
    id: int
    seats: int
    is_available: bool

class BookingCreate(BaseModel):
    table_id: int

class BookingResponse(BaseModel):
    id: int
    user_id: int
    table_id: int
    booking_time: datetime
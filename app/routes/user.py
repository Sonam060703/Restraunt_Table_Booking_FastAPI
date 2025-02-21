from fastapi import APIRouter, Depends, HTTPException
from app.schemas import TableResponse,BookingCreate, BookingResponse
from app.models import Table, Booking
from app.utils import get_current_user
from app.config import SessionLocal 

router = APIRouter(prefix="/tables", tags=["User"])

@router.get("/", response_model=list[TableResponse])
def view_available_tables():
    db = SessionLocal()
    tables = db.query(Table).filter(Table.is_available == True).all()
    return tables

@router.post("/{id}/reserve", response_model=BookingResponse)
def reserve_table(id: int, current_user=Depends(get_current_user)):
    db = SessionLocal()
    table = db.query(Table).filter(Table.id == id, Table.is_available == True).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not available")
    
    table.is_available = False
    Booking = Booking(user_id=current_user.id, table_id=id)
    db.add(Booking)
    db.commit()
    db.refresh(Booking)
    return Booking

@router.delete("/{id}/cancel")
def cancel_Booking(id: int, current_user=Depends(get_current_user)):
    db = SessionLocal()
    Booking = db.query(Booking).filter(Booking.table_id == id, Booking.user_id == current_user.id).first()
    if not Booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    table = db.query(Table).filter(Table.id == id).first()
    table.is_available = True
    db.delete(Booking)
    db.commit()
    return {"message": "Booking cancelled"}

@router.get("/history", response_model=list[BookingResponse])
def view_Booking_history(current_user=Depends(get_current_user)):
    db = SessionLocal()
    Bookings = db.query(Booking).filter(Booking.user_id == current_user.id).all()
    return Bookings

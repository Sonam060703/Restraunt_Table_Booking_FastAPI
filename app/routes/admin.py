from fastapi import APIRouter, Depends, HTTPException
from app.schemas import TableCreate, TableResponse
from app.models import Table, Booking
from app.config import SessionLocal
from app.dependencies import get_admin_user

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/tables", response_model=TableResponse)
def add_table(table: TableCreate, _: dict = Depends(get_admin_user)):
    db = SessionLocal()
    new_table = Table(seats=table.seats, is_available=True)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table

@router.put("/tables/{id}", response_model=TableResponse)
def update_table(id: int, table: TableCreate, _: dict = Depends(get_admin_user)):
    db = SessionLocal()
    db_table = db.query(Table).filter(Table.id == id).first()
    if not db_table:
        raise HTTPException(status_code=404, detail="Table not found")
    db_table.seats = table.seats
    db.commit()
    db.refresh(db_table)
    return db_table

@router.delete("/tables/{id}")
def delete_table(id: int, _: dict = Depends(get_admin_user)):
    db = SessionLocal()
    db_table = db.query(Table).filter(Table.id == id).first()
    if not db_table:
        raise HTTPException(status_code=404, detail="Table not found")
    db.delete(db_table)
    db.commit()
    return {"message": "Table deleted"}

@router.get("/tables", response_model=list[TableResponse])
def view_all_tables(_: dict = Depends(get_admin_user)):
    db = SessionLocal()
    tables = db.query(Table).all()
    return tables

@router.get("/bookings")
def view_all_bookings(_: dict = Depends(get_admin_user)):
    db = SessionLocal()
    bookings = db.query(Booking).all()
    return bookings

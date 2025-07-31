from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import bookings as booking_model
from app.schemas import booking as booking_schema
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=booking_schema.Booking)
def create_booking(booking: booking_schema.BookingCreate, db: Session = Depends(get_db)):
    # Check for overlapping bookings
    overlapping_bookings = db.query(booking_model.Booking).filter(
        booking_model.Booking.roomid == booking.roomid,
        booking_model.Booking.status != "cancelled",  # Consider only active bookings
        booking_model.Booking.checkindate < booking.checkoutdate,
        booking_model.Booking.checkoutdate > booking.checkindate
    ).first()

    if overlapping_bookings:
        raise HTTPException(status_code=400, detail="Room is already booked for the specified dates.")

    try:
        db_booking = booking_model.Booking(**booking.model_dump())
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create booking: {e}")

@router.get("/{booking_id}", response_model=booking_schema.Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = db.query(booking_model.Booking).filter(booking_model.Booking.bookingid == booking_id).first()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@router.get("", response_model=List[booking_schema.Booking])
def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = db.query(booking_model.Booking).offset(skip).limit(limit).all()
    return bookings

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import guests as guest_model
from app.schemas import guest as guest_schema
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=guest_schema.Guest)
def create_guest(guest: guest_schema.GuestCreate, db: Session = Depends(get_db)):
    try:
        db_guest = guest_model.Guest(
            firstname=guest.firstname,
            lastname=guest.lastname,
            email=guest.email,
            phonenumber=guest.phonenumber,
            address=guest.address,
            age=guest.age,
            gender=guest.gender
        )
        db.add(db_guest)
        db.commit()
        db.refresh(db_guest)
        return db_guest
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create guest: {e}")

@router.get("/{guest_id}", response_model=guest_schema.Guest)
def read_guest(guest_id: int, db: Session = Depends(get_db)):
    db_guest = db.query(guest_model.Guest).filter(guest_model.Guest.guestid == guest_id).first()
    if db_guest is None:
        raise HTTPException(status_code=404, detail="Guest not found")
    return db_guest

@router.get("", response_model=List[guest_schema.Guest])
def read_guests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    guests = db.query(guest_model.Guest).offset(skip).limit(limit).all()
    return guests

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import hotels as hotel_model
from app.schemas import hotel as hotel_schema
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=hotel_schema.Hotel)
def create_hotel(hotel: hotel_schema.HotelCreate, db: Session = Depends(get_db)):
    try:
        db_hotel = hotel_model.Hotel(**hotel.model_dump())
        db.add(db_hotel)
        db.commit()
        db.refresh(db_hotel)
        return db_hotel
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create hotel: {e}")

@router.get("/{hotel_id}", response_model=hotel_schema.Hotel)
def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    db_hotel = db.query(hotel_model.Hotel).filter(hotel_model.Hotel.hotelid == hotel_id).first()
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return db_hotel

@router.get("", response_model=List[hotel_schema.Hotel])
def read_hotels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hotels = db.query(hotel_model.Hotel).offset(skip).limit(limit).all()
    return hotels

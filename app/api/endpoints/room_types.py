from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import room_types as room_type_model
from app.schemas import room_type as room_type_schema
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=room_type_schema.RoomType)
def create_room_type(room_type: room_type_schema.RoomTypeCreate, db: Session = Depends(get_db)):
    try:
        db_room_type = room_type_model.RoomType(**room_type.model_dump())
        db.add(db_room_type)
        db.commit()
        db.refresh(db_room_type)
        return db_room_type
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create room type: {e}")

@router.get("/{room_type_id}", response_model=room_type_schema.RoomType)
def read_room_type(room_type_id: int, db: Session = Depends(get_db)):
    db_room_type = db.query(room_type_model.RoomType).filter(room_type_model.RoomType.room_type_id == room_type_id).first()
    if db_room_type is None:
        raise HTTPException(status_code=404, detail="Room type not found")
    return db_room_type

@router.get("", response_model=List[room_type_schema.RoomType])
def read_room_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    room_types = db.query(room_type_model.RoomType).offset(skip).limit(limit).all()
    return room_types

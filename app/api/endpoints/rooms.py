from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.core.database import SessionLocal
from app.models import rooms as room_model
from app.schemas import room as room_schema
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=room_schema.Room)
def create_room(room: room_schema.RoomCreate, db: Session = Depends(get_db)):
    try:
        db_room = room_model.Room(**room.model_dump())
        db.add(db_room)
        db.commit()
        db.refresh(db_room)
        return db_room
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create room: {e}")

@router.get("/{room_id}", response_model=room_schema.Room)
def read_room(room_id: int, db: Session = Depends(get_db)):
    db_room = db.query(room_model.Room).options(joinedload(room_model.Room.room_type)).filter(room_model.Room.roomid == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

@router.get("", response_model=List[room_schema.Room])
def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = db.query(room_model.Room).options(joinedload(room_model.Room.room_type)).offset(skip).limit(limit).all()
    return rooms

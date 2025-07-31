from pydantic import BaseModel
from typing import Optional
from .room_type import RoomType

class RoomBase(BaseModel):
    hotelid: int
    roomnumber: str
    room_type_id: Optional[int] = None
    pricepernight: float
    isavailable: bool

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    roomid: int
    room_type: Optional[RoomType] = None

    class Config:
        from_attributes = True

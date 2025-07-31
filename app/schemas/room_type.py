from pydantic import BaseModel

class RoomTypeBase(BaseModel):
    name: str

class RoomTypeCreate(RoomTypeBase):
    pass

class RoomType(RoomTypeBase):
    room_type_id: int

    class Config:
        from_attributes = True

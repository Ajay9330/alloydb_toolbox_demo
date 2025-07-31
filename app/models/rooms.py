from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Room(Base):
    __tablename__ = "rooms"

    roomid = Column(Integer, primary_key=True, index=True)
    hotelid = Column(Integer, ForeignKey("hotels.hotelid"))
    roomnumber = Column(String)
    room_type_id = Column(Integer, ForeignKey("room_types.room_type_id"), nullable=True)
    pricepernight = Column(Float)
    isavailable = Column(Boolean, default=True)

    hotel = relationship("Hotel")
    room_type = relationship("RoomType")

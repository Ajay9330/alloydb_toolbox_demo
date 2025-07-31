from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    bookingid = Column(Integer, primary_key=True, index=True)
    guestid = Column(Integer, ForeignKey("guests.guestid"))
    roomid = Column(Integer, ForeignKey("rooms.roomid"))
    checkindate = Column(Date)
    checkoutdate = Column(Date)
    totalprice = Column(Float)
    status = Column(String)

    guest = relationship("Guest")
    room = relationship("Room")

from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Payment(Base):
    __tablename__ = "payments"

    paymentid = Column(Integer, primary_key=True, index=True)
    bookingid = Column(Integer, ForeignKey("bookings.bookingid"))
    amount = Column(Float)
    paymentdate = Column(Date)
    paymentmethod = Column(String)

    booking = relationship("Booking")

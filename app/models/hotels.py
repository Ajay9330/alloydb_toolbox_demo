from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Hotel(Base):
    __tablename__ = "hotels"

    hotelid = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    phonenumber = Column(String)
    email = Column(String, unique=True, index=True)
    rating = Column(Float)

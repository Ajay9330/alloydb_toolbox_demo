from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Guest(Base):
    __tablename__ = "guests"

    guestid = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)
    phonenumber = Column(String)
    address = Column(String)
    age = Column(Integer)
    gender = Column(String)


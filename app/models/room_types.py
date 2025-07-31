from sqlalchemy import Column, Integer, String
from app.core.database import Base

class RoomType(Base):
    __tablename__ = "room_types"

    room_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

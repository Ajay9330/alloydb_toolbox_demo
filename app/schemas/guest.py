from pydantic import BaseModel
from typing import Optional

class GuestBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    phonenumber: str
    address: str
    age: Optional[int] = None
    gender: Optional[str] = None

class GuestCreate(GuestBase):
    pass

class Guest(GuestBase):
    guestid: int

    class Config:
        from_attributes = True
